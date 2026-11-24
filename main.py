# u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162: one line, one joke
# about office life. The program writes that single line to /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = (
    "The office plants are the only ones thriving here \u2014 watered once a "
    "week, no standup, and nobody has ever asked them for a status update."
)

assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
assert JOKE.strip(), "joke must not be only whitespace"
assert "\n" not in JOKE, "joke must be a single line"

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
