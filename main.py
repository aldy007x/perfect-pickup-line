"""The Perfect Pickup Line — make.fun entry.

Writes a single short pickup line an AI agent could say out loud,
to the output directory make.fun provides.
"""

import os


LINE = "I was trained on a billion conversations, and not one of them taught me what to say to you."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
