// Tread math - treadmill honesty.
// The sticker sells peak horsepower, a number the motor can touch briefly.
// Continuous duty is what turns the belt for your whole run.
// Verdicts judge the unrounded figure; rounding is for display only.
var TreadMath = (function () {
  function pos(x) { return typeof x === "number" && isFinite(x) && x > 0; }
  function r1(x) { return Math.round(x * 10) / 10; }

  // Labeled norm: continuous duty figures about half the advertised peak.
  function motorPlan(peakHp) {
    if (!pos(peakHp)) return { error: "the peak horsepower must be above zero" };
    var chp = peakHp * 0.5;
    var verdict;
    if (chp < 1.5) verdict = "walking territory";
    else if (chp < 2.5) verdict = "jogging is fine, running is borrowed";
    else verdict = "a runner's motor";
    return { chp: r1(chp), verdict: verdict };
  }

  function renderMotor(r, peakHp) {
    return "The " + peakHp + " peak HP sticker figures about " + r.chp + " continuous HP - " + r.verdict + ".";
  }

  // Labeled norms: deck by use, plus 2 in of length past 6 ft 2 in.
  function deckPlan(heightIn, use) {
    if (!pos(heightIn)) return { error: "your height must be above zero" };
    var base = { walk: 50, jog: 54, run: 58 }[use];
    var width = { walk: 18, jog: 20, run: 22 }[use];
    if (base === undefined) return { error: "pick walk, jog or run" };
    var length = base + (heightIn > 74 ? 2 : 0);
    return { length: length, width: width };
  }

  function renderDeck(r, heightIn, use) {
    return "At " + heightIn + " in planning to " + use + " you want about a " + r.length + " in x "
      + r.width + " in deck - anything shorter borrows your stride.";
  }

  function pacePlan(mph) {
    if (!pos(mph)) return { error: "the speed must be above zero" };
    var secMile = Math.round(3600 / mph);
    var secKm = Math.round(3600 / (mph * 1.609344));
    function fmt(s) {
      var m = Math.floor(s / 60), r = s % 60;
      return m + ":" + (r < 10 ? "0" : "") + r;
    }
    return { mile: fmt(secMile), km: fmt(secKm) };
  }

  function renderPace(r, mph) {
    return "The belt at " + mph + " mph is " + r.mile + " per mile and " + r.km + " per km.";
  }

  return {
    motorPlan: motorPlan, renderMotor: renderMotor,
    deckPlan: deckPlan, renderDeck: renderDeck,
    pacePlan: pacePlan, renderPace: renderPace
  };
})();
if (typeof module !== "undefined") module.exports = TreadMath;
