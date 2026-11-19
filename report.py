# Prints the Sunny Days Lemonade Stand's forecast with your four functions from forecast.py, so you can see them at
# work. Ready to use. Run it with: python report.py
import pandas as pd

from forecast import mean_error, predict_cups, split_days, train_model

days = pd.read_csv("lemonade_days.csv")
X_train, X_test, y_train, y_test = split_days(days, 42)
model = train_model(X_train, y_train)
test_guesses = predict_cups(model, list(X_test["temp_f"]))

print("Sunny Days Lemonade Stand: the forecast")
print("Learned from", len(X_train), "days; tested on", len(X_test), "days it never saw")
print("Cups per degree:", round(model.coef_[0], 2))
print("Off by", mean_error(list(y_test), test_guesses), "cups a day on average, on the days it never saw")
print()

forecast = [72, 81, 90]
guesses = predict_cups(model, forecast)
for i in range(len(forecast)):
    print("At", forecast[i], "degrees: about", guesses[i], "cups")
