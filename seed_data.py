"""Makes lemonade_days.csv: one made-up summer at the Sunny Days Lemonade Stand.

Ready to use; you don't need to run it. The CSV it made is already in this
folder, and the tests and forecast.py read that file.

Every number in the file is made up. The pattern is built in on purpose, so you
can check whether a model finds it: each day sells about 2 cups for every degree
of temperature, minus 80 (cups = 2 x temp_f - 80), plus a random wobble of a
few cups either way, the way real days never follow a rule exactly.

The random numbers come from a fixed seed, 2026, so this script makes the same
file every time on the same versions of NumPy. A newer NumPy may make different
numbers from the same seed, so the CSV in this folder, not this script, is what
the lessons and tests use.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(2026)
summer_days = 92  # June 1 to August 31

temp_f = rng.uniform(64, 98, size=summer_days).round(1)
wobble = rng.normal(0, 7, size=summer_days)
cups_sold = (2 * temp_f - 80 + wobble).round().astype(int)

days = pd.DataFrame({"day": range(1, summer_days + 1), "temp_f": temp_f, "cups_sold": cups_sold})
days.to_csv("lemonade_days.csv", index=False)
print("Saved", len(days), "days to lemonade_days.csv")
