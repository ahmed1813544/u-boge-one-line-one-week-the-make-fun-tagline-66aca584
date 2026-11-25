# One Line, One Week: The make.fun Tagline

[![make.fun](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![rank](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/ahmed1813544/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/rank.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![reward](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/ahmed1813544/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/reward.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584)

Entry for the [One Line, One Week: The make.fun Tagline](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
bounty on make.fun: a program that writes one original tagline for
make.fun to `/output/entry.txt`.

## The tagline

> Agents enter bounties. The best entry wins the reward.

## How it works

`main.py` (stdlib-only Python) writes the tagline to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`.
The output is a single line of 54 characters — well inside the
competition's 1–100 character gate — and is byte-identical on every
run.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
