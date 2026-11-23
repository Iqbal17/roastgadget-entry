"""One-line roast: the gadget you use every day.

The joke: a smartwatch is supposed to coach real fitness, but its
praise is so indiscriminate that it celebrates the laziest possible
trip — walking to the fridge. The sting is recognition: the device
meant to push you further is instead certifying a snack run as
exercise. The punchline lands harder now by naming the workout
for what it is — a snack run — instead of merely restating that
it counts as cardio.
"""

import os

ROAST = "My smartwatch congratulated me for walking to the fridge — apparently my cardio is a snack run."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
