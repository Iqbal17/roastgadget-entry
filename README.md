# One-Line Roast: The Gadget You Use Every Day

## The line

> "My smartwatch congratulated me for walking to the fridge — apparently my cardio is a snack run."

Character count: 95

## Run

```sh
python3 main.py
```

Stdlib only. Writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`).

## Validation

Before writing, `main.py` checks the roast against the competition
gate and refuses to write it if it fails:

- not blank or whitespace-only
- a single line (no line breaks)
- 1–200 characters long

A failed check raises a `ValueError` naming the exact rule that
failed, so a bad line can never be submitted silently.
