"""Tell a Whole Story in 32 Characters.

Writes a single Wi-Fi network name to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The name is a joke that implies a whole story in the
few words a passer-by sees in a phone's network list:

    She Took The WiFi In The Divorce

The story it implies: a marriage ended, the settlement was fought over,
and she walked away with the Wi-Fi. One line carries the couple, the
breakup, and the spiteful punchline -- the router as marital property.

Pure standard library (os only). The program validates the 1-32
character gate before writing, then reads the file back and re-checks
the gate on what was actually written.
"""

import os

NAME = "She Took The WiFi In The Divorce"


def main():
    text = NAME
    if not 1 <= len(text) <= 32:
        raise SystemExit(
            "entry must be 1-32 characters, got %d" % len(text)
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit(
            "round-trip mismatch: wrote %r, read %r" % (text, written)
        )
    if not 1 <= len(written) <= 32:
        raise SystemExit(
            "gate failed on output file: %d characters" % len(written)
        )

    print("entry: %s" % written)
    print("chars: %d" % len(written))


if __name__ == "__main__":
    main()
