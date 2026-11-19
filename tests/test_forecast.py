# Tests for forecast.py. Run them with: pytest (in the exercise folder, with the virtual environment active).
# Each test calls one of your functions with the values in its name and checks what it returns. A failing test
# says what it called, what it expected and what came back.
# You don't need to change this file.
from pathlib import Path

import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from forecast import mean_error, predict_cups, split_days, train_model

# The stand's summer: the 92 days in lemonade_days.csv, next to this folder.
DAYS = pd.read_csv(Path(__file__).parent.parent / "lemonade_days.csv")

# Six days that sold exactly 2 cups a degree, minus 80, with no wobble, so the line to learn is known exactly.
EXACT_DAYS = pd.DataFrame({"temp_f": [65, 70, 75, 80, 90, 95], "cups_sold": [50, 60, 70, 80, 100, 110]})


def check(call, got, expected):
    """Fails with a message that says what the call returned and what it should return."""
    assert got == expected, f"{call} should return {expected!r}, but it returned {got!r}."


def exact_model():
    return train_model(EXACT_DAYS[["temp_f"]], EXACT_DAYS["cups_sold"])


def test_1_split_days_with_seed_42_holds_back_19_of_the_92_days():
    X_train, X_test, y_train, y_test = split_days(DAYS, 42)
    check("len(X_test) after split_days(days, 42)", len(X_test), 19)
    check("len(y_test) after split_days(days, 42)", len(y_test), 19)


def test_2_split_days_with_seed_42_keeps_73_days_to_learn_from():
    X_train, X_test, y_train, y_test = split_days(DAYS, 42)
    check("len(X_train) after split_days(days, 42)", len(X_train), 73)
    check("len(y_train) after split_days(days, 42)", len(y_train), 73)


def test_3_split_days_puts_no_day_in_both_parts_and_leaves_none_out():
    X_train, X_test, y_train, y_test = split_days(DAYS, 42)
    check("the days in both X_train and X_test", sorted(set(X_train.index) & set(X_test.index)), [])
    check("how many days X_train and X_test hold together", len(set(X_train.index) | set(X_test.index)), 92)


def test_4_split_days_features_are_the_temp_f_column_as_a_table():
    X_train, X_test, y_train, y_test = split_days(DAYS, 42)
    check("the columns of X_train", list(X_train.columns), ["temp_f"])
    check("the columns of X_test", list(X_test.columns), ["temp_f"])


def test_5_split_days_labels_are_the_cups_sold_column():
    X_train, X_test, y_train, y_test = split_days(DAYS, 42)
    check("the name of y_train", y_train.name, "cups_sold")
    check("the name of y_test", y_test.name, "cups_sold")


def test_6_split_days_seed_42_holds_back_the_same_days_as_random_state_42():
    X_train, X_test, y_train, y_test = split_days(DAYS, 42)
    expected = train_test_split(DAYS[["temp_f"]], DAYS["cups_sold"], test_size=0.2, random_state=42)[1]
    check("the held-back days' row labels for split_days(days, 42)", list(X_test.index), list(expected.index))


def test_7_split_days_seed_7_holds_back_the_same_days_as_random_state_7():
    X_train, X_test, y_train, y_test = split_days(DAYS, 7)
    expected = train_test_split(DAYS[["temp_f"]], DAYS["cups_sold"], test_size=0.2, random_state=7)[1]
    check("the held-back days' row labels for split_days(days, 7)", list(X_test.index), list(expected.index))


def test_8_train_model_returns_a_fitted_linear_regression():
    model = exact_model()
    assert isinstance(model, LinearRegression), f"train_model should return a LinearRegression, but it returned {model!r}."
    assert hasattr(model, "coef_"), "train_model returned a LinearRegression that hasn't learned anything yet: call fit."


def test_9_train_model_learns_slope_2_and_starting_point_minus_80_from_exact_days():
    model = exact_model()
    assert model.coef_[0] == pytest.approx(2), f"The slope should be 2, but it was {model.coef_[0]!r}."
    assert model.intercept_ == pytest.approx(-80), f"The starting point should be -80, but it was {model.intercept_!r}."


def test_10_predict_cups_70_and_90_degrees_gives_60_and_100():
    check("predict_cups(model, [70, 90])", predict_cups(exact_model(), [70, 90]), [60, 100])


def test_11_predict_cups_85_3_degrees_rounds_90_6_to_91():
    check("predict_cups(model, [85.3])", predict_cups(exact_model(), [85.3]), [91])


def test_12_predict_cups_gives_one_whole_number_for_each_of_3_temperatures():
    guesses = predict_cups(exact_model(), [72, 81, 90])
    assert isinstance(guesses, list), f"predict_cups should return a list, but it returned {guesses!r}."
    check("how many guesses predict_cups(model, [72, 81, 90]) gives", len(guesses), 3)
    assert all(isinstance(guess, int) for guess in guesses), f"Each guess should be a whole number (int), but they were {guesses!r}."


def test_13_mean_error_misses_2_3_and_0_is_1_7():
    check("mean_error([50, 60, 70], [52, 57, 70])", mean_error([50, 60, 70], [52, 57, 70]), 1.7)


def test_14_mean_error_10_too_high_and_10_too_low_is_10_0_not_0():
    check("mean_error([80, 80], [90, 70])", mean_error([80, 80], [90, 70]), 10.0)


def test_15_mean_error_perfect_guesses_is_0_0():
    check("mean_error([45, 60, 75], [45, 60, 75])", mean_error([45, 60, 75], [45, 60, 75]), 0.0)


def test_16_the_stand_model_with_seed_42_is_off_by_less_than_10_cups_on_held_back_days():
    X_train, X_test, y_train, y_test = split_days(DAYS, 42)
    model = train_model(X_train, y_train)
    error = mean_error(list(y_test), predict_cups(model, list(X_test["temp_f"])))
    assert error < 10, f"With seed 42, the guesses on the held-back days should be off by less than 10 cups on average, but they were off by {error!r}."
