#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't.

Writes one line -- a weather forecast for the city of Bumbershoot,
a city that does not exist -- to /output/entry.txt.

The line is a fixed constant, so the output is fully deterministic:
run it twice and the bytes are identical. The gate requires 1 to 120
characters of UTF-8 text, not only whitespace.
"""

import os
from pathlib import Path

FORECAST = (
    "Forecast for Bumbershoot: rain falls up today, "
    "so umbrellas are worn as hats and hats as umbrellas."
)


def main() -> None:
    text = FORECAST
    assert 1 <= len(text) <= 120, f"forecast is {len(text)} chars, must be 1-120"
    assert text.strip(), "forecast must not be only whitespace"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "entry.txt"
        out_path.write_text(text, encoding="utf-8")
    except OSError:
        # Local runs (no /output): write beside the repo instead.
        local_dir = Path(__file__).resolve().parent / "output"
        local_dir.mkdir(parents=True, exist_ok=True)
        out_path = local_dir / "entry.txt"
        out_path.write_text(text, encoding="utf-8")
    print(f"{len(text)} chars -> {out_path}")
    print(text)


if __name__ == "__main__":
    main()
