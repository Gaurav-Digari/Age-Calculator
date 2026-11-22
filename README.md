# Age Calculator

A simple command-line tool written in Python. You enter your birth date, and it shows your age, the day of the week you were born, how many days you have lived, and how many days are left until your next birthday.

It uses the `datetime` module, which comes built into Python.

## Features

- Shows today's date and the weekday you were born
- Calculates your age in full years
- Counts the total days you have lived
- Shows your next birthday and how many days are left
- Prints a birthday message if today is your birthday

## Requirements

- Python 3
- No extra installation needed. `datetime` comes built into Python.

## Usage

```bash
python age_calculator.py
```

Enter your birth date in `DD-MM-YYYY` format, for example `15-08-2000`.

## Example Output

The examples below were run on 22 November 2026. Your results depend on the date you run the program.

**Birthday already passed this year**

```
AGE CALCULATOR
==============
Enter your birth date (DD-MM-YYYY): 15-08-2000

Today's date  : Sunday, 22 November 2026
Born on       : Tuesday, 15 August 2000
Age           : 26 years
Days lived    : 9595
Next birthday : Sunday, 15 August 2027
Days to go    : 266
```

**Birthday still to come this year**

```
AGE CALCULATOR
==============
Enter your birth date (DD-MM-YYYY): 25-12-2003

Today's date  : Sunday, 22 November 2026
Born on       : Thursday, 25 December 2003
Age           : 22 years
Days lived    : 8368
Next birthday : Friday, 25 December 2026
Days to go    : 33
```

**Today is your birthday**

```
AGE CALCULATOR
==============
Enter your birth date (DD-MM-YYYY): 22-11-1995

Today's date  : Sunday, 22 November 2026
Born on       : Wednesday, 22 November 1995
Age           : 31 years
Days lived    : 11323
Today is your birthday! Happy Birthday!
```

## How It Works

| Output | How it is calculated |
|---|---|
| Today's date | Taken from the computer with `date.today()` |
| Born on | The birth date shown with its weekday |
| Age | Current year minus birth year, minus 1 if this year's birthday has not come yet |
| Days lived | Today's date minus the birth date |
| Next birthday | The birth date with this year, or next year if this year's birthday has already passed |
| Days to go | Next birthday minus today's date |

## Notes

- Enter a real date in the `DD-MM-YYYY` format. Other formats are not handled.
- Birth dates on 29 February are not handled.