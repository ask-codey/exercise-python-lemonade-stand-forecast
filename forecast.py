"""Sunny Days Lemonade Stand: four functions for you to finish.

The docstring under each function says what it should do, with examples.
Replace each raise NotImplementedError("Not built yet.") line with your own
code. Return each answer: the tests read what comes back, not what's printed.

days is a pandas table (a DataFrame) with the columns day, temp_f and
cups_sold, one row per day, like the one pd.read_csv("lemonade_days.csv")
gives you. The imports below are everything the four functions need.
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


def split_days(days, seed):
    """Split the days into training days and test days, and return all four parts.

    The feature is the temp_f column, as a one-column table: days[["temp_f"]].
    The label is the cups_sold column: days["cups_sold"].
    Hold back 20% of the days for testing (test_size=0.2), and pass seed on as
    random_state, so the same seed always gives the same split.

    Return what train_test_split returns, in its order:
    X_train, X_test, y_train, y_test

    With the stand's 92 days: 73 training days and 19 test days.
    """
    raise NotImplementedError("Not built yet.")


def train_model(X, y):
    """Make a LinearRegression model, fit it to X and y, and return the fitted model.

    X is a one-column table of temperatures, y the cups sold on those days.
    For days that sold exactly 2 cups a degree minus 80, the model learns a
    slope of 2 and an intercept of -80.
    """
    raise NotImplementedError("Not built yet.")


def predict_cups(model, temps):
    """Return the model's guesses for a list of temperatures, as a list of whole cups.

    Put the temperatures in a one-column table with the column temp_f (the
    name the model learned from), ask the model to predict, and round each
    guess to a whole number with round().

    With a model that learned 2 cups a degree minus 80:
    predict_cups(model, [70, 90]) -> [60, 100]
    predict_cups(model, [85.3]) -> [91]   (90.6, rounded)
    """
    raise NotImplementedError("Not built yet.")


def mean_error(actual, guesses):
    """Return the mean absolute error: how many cups a guess is off by, on average.

    Each guess's miss is how far it is from the actual cups, counted as a
    positive number whether the guess was too high or too low. The mean
    absolute error is the average of those misses. Round it to 1 decimal place.

    mean_error([50, 60, 70], [52, 57, 70]) -> 1.7   (misses 2, 3 and 0: 5 / 3 = 1.666...)
    mean_error([80, 80], [90, 70]) -> 10.0          (one 10 too high, one 10 too low)
    """
    raise NotImplementedError("Not built yet.")
