# Exercise: Lemonade Stand Forecast

Exercise code for the lesson **Exercise: Lemonade Stand Forecast** in the Python in Depth course on [ask-codey.com](https://www.ask-codey.com).

The Sunny Days Lemonade Stand wants to know how many cups to make tomorrow, and how far off that guess might be. You'll write the four functions behind its forecast in `forecast.py`: one holds some of last summer's days back for testing, one trains a straight-line model on the rest, one turns a list of temperatures into guesses, and one works out how far off the guesses are on average. Tests call each function to check what it returns.

## What's here

- `forecast.py`: the four functions, `split_days`, `train_model`, `predict_cups` and `mean_error`. Each one stops with `NotImplementedError: Not built yet.` for now. The docstring under each says what it should do, with examples, and the imports it needs are at the top. For you to finish.
- `report.py`: prints the stand's forecast with your four functions, so you can see them at work. Ready to use.
- `lemonade_days.csv`: one summer at the stand, 92 days, with the temperature (`temp_f`) and the cups sold (`cups_sold`). Every number is made up. Ready to use.
- `seed_data.py`: the script that made `lemonade_days.csv`, so you can see the pattern built into it: about 2 cups for every degree, minus 80, plus a random wobble. You don't need to run it; the tests and `report.py` read the CSV. Ready to use.
- `tests/test_forecast.py`: tests that call your functions and check what comes back. You don't need to change this file.
- `requirements.txt`: the packages the tests need, at exact versions: pytest, scikit-learn and pandas. Ready to use.
- `pytest.ini`: tells pytest where the tests are and where to find `forecast.py`. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment and the files Python and pytest make as they run. Ready to use.

## Before you start

The tests need pytest, scikit-learn and pandas, and they go in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it. scikit-learn and pandas bring NumPy and a few other packages with them, so this one takes a minute or two.

*Virtual Environments and pip*, in Module 3, explains all three. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

## Check your work

```bash
pytest
```

At first every test fails: that is expected, because each function stops with a `NotImplementedError` for now. Each function you finish turns its tests green. A failing test's message says what it called, what it expected and what came back, for example *mean_error([80, 80], [90, 70]) should return 10.0, but it returned 0.0.*

To see your functions at work, run:

```bash
python report.py
```

## The rules

- Keep each function's name and parameters as they are.
- Return each answer; don't print it. The tests read what your functions return.
- The feature is the `temp_f` column and the label is the `cups_sold` column. The `day` column isn't used.
- Hold back 20% of the days for testing, and pass the seed on as `random_state`, so the same seed always gives the same split.
- Don't change the tests, `report.py`, `seed_data.py` or `lemonade_days.csv`.

## Tips

- The features go in as a table with one column, `days[["temp_f"]]` (two pairs of brackets), and the label as one column, `days["cups_sold"]`.
- `train_test_split` gives back four parts, in the order `X_train, X_test, y_train, y_test`, and `split_days` can return them as they come.
- A model has to `fit` before it can `predict`, and `predict` wants a table with the same column name the model learned from: `pd.DataFrame({"temp_f": temps})`.
- `round()` turns each guess into a whole number of cups.
- The mean absolute error is the average of each miss's size: `abs()` makes a miss too low count the same as one too high.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
