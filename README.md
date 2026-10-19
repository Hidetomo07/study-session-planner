# Study Session Planner

## Purpose

Study Session Planner is a simple Python command-line application.

It calculates the total study time based on the number of study blocks and the duration of each block.

It also suggests whether to plan a break.

## Requirements

- Python 3
- No external Python packages are required.

## How to Run

1. Open a terminal.
2. Navigate to the project directory.
3. Run the program using Python 3.

Example:

```bash
python3 planner.py --blocks 3 --minutes 25
```

Output:

```text
Total minutes: 75
Plan a break.
```

## Command-Line Arguments

| Argument | Description | Required | Default |
|---|---|---|---|
| `--blocks` | Number of study blocks | Yes | None |
| `--minutes` | Minutes per block | No | 25 |
| `--help` | Display the help message | No | None |

Both `--blocks` and `--minutes` must be positive integers.

## Examples

### Example 1: Standard study session

```bash
python3 planner.py --blocks 3 --minutes 25
```

Output:

```text
Total minutes: 75
Plan a break.
```

### Example 2: Default minutes

```bash
python3 planner.py --blocks 1
```

Output:

```text
Total minutes: 25
Short study session.
```

### Example 3: Exactly 60 minutes

```bash
python3 planner.py --blocks 2 --minutes 30
```

Output:

```text
Total minutes: 60
Plan a break.
```

## Input Validation

The program rejects zero or negative values.

For example:

```bash
python3 planner.py --blocks 0
```

Error:

```text
planner.py: error: Use positive numbers.
```

Non-integer inputs are also rejected by argparse.

## Help Menu

To display the help menu:

```bash
python3 planner.py --help
```

## How It Works

1. `argparse` reads the command-line arguments.
2. `total_minutes()` validates the input values.
3. The function calculates the total study time.
4. The program displays the total number of minutes.
5. An `if-else` statement determines the break recommendation.

If the total is 60 minutes or more, the program displays "Plan a break."

Otherwise, it displays "Short study session."

## Development

This project was created during the Pre-MSc Git and Python laboratory.

Git was used for version control, including commits, branches, merging, and pushing changes to GitHub.