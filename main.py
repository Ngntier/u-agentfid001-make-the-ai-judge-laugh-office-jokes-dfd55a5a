"""One-line office joke entry for make.fun's
"Make the AI Judge Laugh: Office Jokes" bounty.

Writes the joke to MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library, no arguments, no network.
"""

import os

JOKE = (
    "I asked for a raise and my boss gave me a standing desk, "
    "so now I stand taller while earning the same."
)


def main():
    # Gate: the sealed scorer requires 1-199 characters of UTF-8 text.
    # Fail loudly here rather than shipping an entry that scores 0.
    if not 1 <= len(JOKE) <= 199:
        raise SystemExit(f"joke is {len(JOKE)} characters, must be 1-199")
    if JOKE != JOKE.strip() or "\n" in JOKE:
        raise SystemExit("joke must be a single line with no leading/trailing space")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"Wrote {len(JOKE)}-character joke to {path}")


if __name__ == "__main__":
    main()
