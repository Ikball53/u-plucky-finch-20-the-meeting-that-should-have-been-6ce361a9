"""One-liner entry: The Meeting That Should Have Been an Email.

The entry is a single line of plain text (<= 200 chars). This script
holds that line as a constant and writes it, byte-for-byte with no
trailing newline, to entry.txt inside MAKEFUN_OUTPUT_DIR.
"""

import os
from pathlib import Path

# The joke: the meeting justifies itself by the absurdity of explaining
# the email that would have replaced it.
LINE = "The meeting could have been an email, but then the email would have needed a meeting to explain why it wasn't a meeting."

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert LINE == LINE.strip() and "\n" not in LINE, "line must be a single line with no stray whitespace"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
