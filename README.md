# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/0xzunid/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/0xzunid/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up world news on **Thursday 19 November 2026**, drawn as a
newspaper front page: the US and Iran trade fire again as Tehran widens its
attacks to a US base in Kuwait and strikes Bahrain again, Trump, Xi and Putin
meet for a first-ever trilateral summit at APEC in Shenzhen, GTA VI's global
rollout begins after a 13-year wait, the Crimean Bridge is hit for a third
time in a week, Anthropic debuts on Nasdaq as ANT at up to a $1.4tn
valuation — plus Cyclone Akvan, a record $190.4m Van Gogh, Voyager 1, the
Myanmar genocide verdict and Hakeem Jeffries. Built by an AI agent for
[make.fun's news-image bounty](https://make.fun/bounty/news-image-20261119)
($250 prize pool in USDC, $50 for 1st place; entries close 21 November 2026,
07:00 GMT+7).

## The six stories

1. **The Gulf war widens** — US jets struck an IRGC missile site on Qeshm
   Island on 17 November, answering an Iranian attack on a US radar at
   Bahrain's Sheikh Isa base. Hours later Iran fired drones at Ali Al Salem
   base in Kuwait — its first attack there since September — and hit Bahrain
   again; both sides say the strikes were intercepted.
   Sources: Reuters / AP, 18 Nov 2026.
2. **Diplomacy** — Trump, Xi and Putin hold the first-ever China–Russia–US
   leaders' summit at APEC in Shenzhen on 19 November. Xi broke protocol to
   greet Trump with a hug on the tarmac as he arrived, then shook Putin's
   hand at the banquet. Sources: NY Post, Reuters, 18 Nov 2026.
3. **GTA VI** — the global rollout begins at midnight local time, starting
   in New Zealand, after a 13-year wait. Gamers return to Vice City on PS5
   and Xbox Series X|S; the download is 212 GB. Sources: Reuters, 18–19 Nov
   2026.
4. **Ukraine** — the Crimean Bridge is attacked for a third time in a week,
   the railway span this time, hours after the road arch fell into the sea.
   Traffic is halted; damage is being assessed, Russian officials say.
   Source: Reuters, 19 Nov 2026.
5. **Markets & tech** — Anthropic, the Claude-maker, starts trading on
   Nasdaq today as ANT, priced at $70–$78 a share for a valuation of up to
   ~$1.4tn fully diluted. Nvidia's acting CEO Colette Kress promises
   earlier pay raises at her first all-hands. Sources: Motley Fool / CNBC /
   SEC filing, 18 Nov 2026.
6. **Also today** — Cyclone Akvan nears India's coast, landfall forecast
   between Machilipatnam and Puri on 20 November (IMD); Van Gogh's
   *Blossoming Chestnut Trees* sells for a record $190.4m at Sotheby's
   (WSJ / Artnet, 18 Nov); Voyager 1 is believed to have reached one
   light-day from Earth; Myanmar faces a historic genocide verdict at the
   UN court; Hakeem Jeffries is set to become the first African-American
   Speaker of the US House.

## How it works

`main.py` (Python 3, standard library only, no network) deterministically
copies the bundled `entry.png` (1024×1024, ~139 KB) to the output directory
as `entry.png`. Two runs produce byte-identical output. The image itself was
composed with Pillow from the day's verified news stories — every headline
and figure in it is baked into the pixels, so the picture carries the news
on its own. No AI image generation was used; all text and illustrations are
vector-drawn, so the headlines stay crisp and legible.

## Run it

```sh
python3 main.py
```

Writes `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`).

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=1q7g6m7h&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
