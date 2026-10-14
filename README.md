# Tread math

The sticker names the peak, the motor names the duty, and the belt names the pace.

Treadmills are sold on peak horsepower - a momentary number, not the duty the motor holds for a whole run. Decks get the same treatment: "spacious" until a tall runner's stride hangs off the back.

## The three tools

- **Motor decoder** - advertised peak HP halved (labeled norm) into continuous duty, banded unrounded from walking territory to a runner's motor.
- **Deck plan** - height and plans become the deck: labeled norms of 50/54/58 in length and 18/20/22 in width for walk, jog and run, plus 2 in of length past 6 ft 2 in.
- **Pace translator** - belt mph becomes seconds per mile and per km exactly (`3600 / mph`, `3600 / (mph x 1.609344)`), rendered m:ss.

## Honesty notes

Illustrative planning arithmetic only. The halving and deck sizes are labeled norms; the spec sheet's own CHP figure, when printed, outranks any rule. Use the safety key every run, keep the floor behind the belt clear, and a used treadmill with a tired belt or a hot smell tells the truth no sticker can.

## Files

- `index.html` - the pitch
- `app.html` - the calculators
- `engine.js` - the arithmetic (browser and node)
- `oracle.py` - the same arithmetic, float-for-float, writing `expected.json`
- `test.js` - runs every case in `expected.json` through `engine.js` and compares results and renders exactly

Run the check:

```
python3 oracle.py && node test.js
```
