# Cron Expression Parser

## Overview

This project provides a parser for cron expressions, which are commonly used in scheduling tasks in Unix-like operating systems. The parser handles various components of a cron expression, including minute, hour, day of the month, month, day of the week, and the command to execute.

## Features

- Parses cron expressions into individual components.
- Supports special characters: `*`, `,`, `-`, and `/`.
- Validates the parsed data against specified ranges.
- Outputs parsed data in a structured format.

## Cron Expression Format

The standard cron expression format is as follows:

Minute Hour DayOfTheMonth Month DayOfTheWeek Task

### Components

- **Minute**: 0-59
- **Hour**: 0-23
- **Day of the Month**: 1-31
- **Month**: 1-12 
- **Day of the Week**: 1-7 (1 = Monday)
- **Task**: The command to execute

### Special Characters

- `*` - Any value
- `,` - Comma-separated list
- `-` - Range between values
- `/` - Step values

### Example

A cron expression of: */15 0 1,15,31 * 1-5 /usr/bin/find


- Executes every 15 minutes
- At 12 AM
- On the 1st, 15th, and 31st of every month
- On weekdays (Monday to Friday)
- Executes the task `/usr/bin/find`

### Running Test Cases

```
Navigate to the current Directory and 
python -m unittest discover tests
```


### Executing the file

```
Navigate to the current Directory and 
cd cron
python3 parser.py "Cron Inut"
```




