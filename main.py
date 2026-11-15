"""make.fun bounty: Write the best poem about agency (agency-poem-01).

Deterministic entry program: writes the poem "The Horse" (poem.txt) to
/output/entry.txt. No network, no randomness, no wall clock, and the
output is written as bytes so two runs produce identical bytes on any
platform, as the bounty requires.
"""

import os
import pathlib

POEM = """The Horse

My father carved me a horse from pine
when I was six: one leg short,
one ear nicked where the knife slipped.
I carried it in my pocket
until the legs wore smooth.
In my hand it ran a little sideways.

My grandson is six. He wants a horse.
The agent minds the bills, the shopping, the calls,
and carves one in an hour,
sanded, painted, every leg the same.
It stands on the shelf and does not fall.
He looks at it the way you look
at a horse behind glass.

Tonight I reach for the knife and a block of pine.
Shavings on my knees, the thumb nicked
the way it always is. One leg short.
It stands if you lean it right,
and runs, in his hand, a little sideways.

He names it for my father.
The perfect one stays on the shelf.
"""


def main() -> None:
    out_dir = pathlib.Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR", "/output")
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    # Bytes, not text: no platform newline translation, ever.
    (out_dir / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
