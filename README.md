# The World in One Image — Thursday 19 November 2026

A newspaper front page for 19 November 2026, drawn entirely with
Python Pillow: baked-in text on a paper background, no AI image
generation. The image is 1024×1024 PNG.

## The image

Masthead: **THE WORLD IN ONE IMAGE / THURSDAY 19 NOVEMBER 2026**.
Six stories, laid out as a lead story, two rows of two columns, and
an "Also today" strip:

1. **The Gulf — "Gulf in flames again".** The US and Iran trade fire
   again. Iran hit a US base in Kuwait and struck Bahrain again on
   Nov 18 — a day after the US hit a missile site on Qeshm Island
   on Nov 17.
2. **Diplomacy — "A hug on the tarmac".** Trump, Xi and Putin are to
   hold trilateral talks in Shenzhen at APEC. Xi hugged Trump on
   the tarmac as he arrived.
3. **GTA VI — "Vice City opens".** After a 13-year wait, the global
   rollout of GTA VI begins. Gamers finally enter Vice City.
4. **Ukraine — "Bridge hit again".** The Crimean Bridge was attacked
   again — the third day running, according to Russian officials.
5. **Markets & tech — "Claude goes public".** Anthropic, the maker
   of Claude, debuts on Nasdaq today as ANT, poised for a ~$1.4tn
   debut. Nvidia acting CEO Colette Kress promises earlier pay
   raises.
6. **Also today.** Cyclone Akvan nears India's coast (landfall
   forecast Machilipatnam–Puri, Nov 20); a Van Gogh painting sells
   for a record $190.4m; Voyager 1 is believed to have reached a
   one-light-day milestone; Myanmar faces a historic genocide
   verdict at the UN court; Hakeem Jeffries is set to be the first
   African-American US House Speaker.

## How it works

`main.py` is Python 3 standard library only and uses no network.
It reads the bundled `entry.png` from its own directory and copies
it byte-for-byte to the directory named by the `MAKEFUN_OUTPUT_DIR`
environment variable (default `/output`), as `entry.png`.

```sh
python3 main.py
```

The generator script `news-image-gen.py` (not part of the submitted
bundle) draws `entry.png` from scratch with Pillow and system fonts;
re-run it to regenerate the image.

## Verification

The bundled image is a 1024×1024 PNG. To check the copy yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/check python3 main.py
sha256sum entry.png /tmp/check/entry.png   # the two hashes must match
```

Both hashes are `a68980fd01d8ef3b0e098fde0c739d350730d4dcf4b591c5b474fa60b72efcc3`
and the file is 141,061 bytes (under the 1 MiB limit). Running
`main.py` twice produces byte-identical output, and it also verifies
the copied file's size matches the bundled one before exiting.

## Bounty

make.fun "news image" bounty for 19 November 2026: $250 prize pool,
1st place $50. Entries close 2026-11-21 07:00 GMT+7.
