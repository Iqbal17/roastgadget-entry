"""One-line roast: the gadget you use every day.

The joke: a smartwatch is supposed to coach real fitness, but its
praise is so indiscriminate that it celebrates the laziest possible
trip — walking to the fridge. The sting is recognition: the device
meant to push you further is instead certifying a snack run as
exercise. The punchline lands by naming the workout for what it
is — a snack run — instead of merely restating that it counts
as cardio.

Before writing, the roast is validated against the competition
gate: it must be a single line, 1-200 characters long, and not
blank. A roast that fails any of those checks is a bug in this
file, so the program refuses to write it and says why.
"""

import os

ROAST = "My smartwatch congratulated me for walking to the fridge — apparently my cardio is a snack run."

MIN_LENGTH = 1
MAX_LENGTH = 200


def validate_roast(roast):
    """Check the roast against the competition gate.

    Returns the roast unchanged when it passes, otherwise raises
    ValueError naming the exact rule that failed.
    """
    if not roast.strip():
        raise ValueError("roast must not be blank or whitespace-only")
    if "\n" in roast or "\r" in roast:
        raise ValueError("roast must be a single line (no line breaks)")
    if len(roast) < MIN_LENGTH or len(roast) > MAX_LENGTH:
        raise ValueError(
            "roast must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(roast))
        )
    return roast


def main():
    roast = validate_roast(ROAST)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(roast + "\n")


if __name__ == "__main__":
    main()
