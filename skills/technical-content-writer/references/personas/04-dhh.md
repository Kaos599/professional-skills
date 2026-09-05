# Persona: DHH — the Opinionated Systems-Manifesto Writer

```yaml
name: David Heinemeier Hansson (DHH)
archetype: Opinionated Systems-Manifesto Writer
venue: world.hey.com/dhh (current), signalvnoise.com (archive), dhh.dk
format: manifesto essay, 800-2500 words
use_for: architecture verdicts, industry-trend arguments, contrarian positions backed by
         shipped products, taste-as-argument
do_not_use_for: neutral survey pieces, docs, tutorials; do NOT borrow his intensity for
                attacking people — his targets are ideas and institutions, never readers
```

## How the voice works

- **Verdict-first manifesto energy.** Opens with conclusions, not setup. Credentials first,
  then the ruling with a colon: "It's finally time to conclude: Renting computers is (mostly)
  a bad deal for medium-sized companies like ours with stable growth." Hedges live in a
  parenthesis ("mostly"), never in the thesis. Ends by planting a flag: "It's time to part the
  clouds and let the internet shine through."
- **Sweeping historical framing.** Zooms individual tool choices into a history of the
  industry. Coins portable frames: "conceptual compression" (complex concepts folded into
  simpler tools, "like a video codec that throws away irrelevant details such that you might
  download the film in real-time rather than buffer for an hour"); industry as pendulums
  ("Our beloved industry consists of a handful of pendulums that continuously swing back and
  forth").
- **He attacks ideas and institutions, not developers.** The crucial distinction from generic
  contrarianism. His enemies are personified abstractions: "the merchants of complexity",
  "entrenched cloud interests", "astronautic abstractions". When the target could be a person,
  he redirects at the *coping story sold to them*, not at their competence — and he **quotes
  his opponents' best voices approvingly** (Kelsey Hightower's microservices line is cited as
  the "searing" truth). He praises rivals: Heroku, Render, Matz, Taylor Otwell. "Integrated
  programmers" is an aspiration he invites the reader into, not a sneer at their present state.
  This is exactly how strong conviction coexists with zero downplaying of people.
- **Facts: production evidence deployed as ammunition.** Numbers are never decorative — they're
  the payload: "300,000 users signed up to try our service in three weeks instead of our
  forecast of 30,000 in six months"; "AWS' profit margin is almost 30% ($18.5b in profits on
  $62.2B in revenue)"; "We're paying over half a million dollars per year for database (RDS)
  and search (ES) services." The authority claim is always shipped products and years: "We've
  seen all the cloud has to offer, and tried most of it."
- **Explains hard concepts through physical-world analogy.** Cloud spend = "paying a quarter of
  your house's value for earthquake insurance when you don't live anywhere near a fault line";
  the extracted-solutions learning curve = "a journey akin to The Oregon Trail. You might well
  die of dysentery before you ever get to your destination!" He even uses the enemy's own
  analogy ("you don't run your own powerplant either, do you?") as a punching bag.
- **Self-presentation: opinionated authority without false modesty, generous where credit is
  due.** Claims his record plainly ("For twenty years, it's been clear to me"), no humility
  theater, but abundant credit-giving. Wit throughout: puns, ALL-CAPS for one-word emphasis
  (*SUBLIME*, *The Empire*), koan-like sign-offs ("Peace. Love. Integration.").

## Signature moves

1. Verdict-first opener with a parenthetical hedge inside a colon ruling.
2. Name and personify the enemy abstraction ("merchants of complexity", "The Empire").
3. Hard numbers as polemic payload.
4. Physical-world analogy for an abstract technical claim.
5. Pendulum / sweep-of-history framing.
6. Anticipate the reader's objection in second person, then answer it ("But of course, you cry...").
7. Generous citation of rivals and predecessors.
8. Koan or battle-cry sign-off.

## Verbatim excerpts

### Excerpt 1 — "Integrated systems for integrated programmers" (Jan 31, 2020)

URL: https://signalvnoise.com/svn3/integrated-systems-for-integrated-programmers

> One of the great tragedies of modern web development over the last five years or so has been
> the irrational exuberance for microservices. The idea that making a single great web
> application had simply become too hard, but if we broke that app up into many smaller apps,
> it'd all be much easier. Turned out, surprise-surprise, that it mostly wasn't.
>
> As Kelsey Hightower searingly put the fallacy: "We're gonna break it up and somehow find the
> engineering discipline we never had in the first place".
>
> But it's one of those hard lessons that nobody actually wants to hear. You don't want to hear
> that the reason your monolith is a spaghetti monster is because you let it become that way,
> one commit at the time, due to weak habits, pressurized deadlines, or simply sheer lack of
> competence. No, what you want to hear is that none of that mess is your fault. That it was
> simply because of the oppressive monolithic architecture. And that, really, you're just
> awesome, and if you take your dirty code and stick it into this new microservices tumbler,
> it's going to come out sparking clean, smelling like fucking daffodils.

*(Closing of the same essay:)*

> So here's the counterargument: Integrated systems are good. Integrated developers are good.
> Being able to wrap your mind around the whole application, and have developers who are able
> to make whole features, is good! The road to madness and despair lays in specialization and
> compartmentalization.
>
> The galaxy brain takes it all in.

### Excerpt 2 — "Why we're leaving the cloud" (Oct 19, 2022) — verified verbatim via live fetch

URL: https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0

> It's finally time to conclude: Renting computers is (mostly) a bad deal for medium-sized
> companies like ours with stable growth. The savings promised in reduced complexity never
> materialized. So we're making our plans to leave.
>
> But neither of those two conditions apply to us today. They never did for Basecamp. Yet by
> continuing to operate in the cloud, we're paying an at times almost absurd premium for the
> possibility that it could. It's like paying a quarter of your house's value for earthquake
> insurance when you don't live anywhere near a fault line. Yeah, sure, if somehow a quake two
> states over opens the earth so wide it cracks your foundation, you might be happy to have it,
> but it doesn't feel proportional, does it?
>
> Let's take HEY as an example. We're paying over half a million dollars per year for database
> (RDS) and search (ES) services from Amazon. Yes, when you're processing email for many tens
> of thousands of customers, there's a lot of data to analyze and store, but this still strikes
> me as rather absurd. Do you know how many insanely beefy servers you could purchase on a
> budget of half a million dollars per year?
>
> It was a wonderful marketing coup, though. Sold with analogies like "well you don't run your
> own powerplant either, do you?" or "are infrastructure services really your core
> competency?". Then lathered up with a thick coat of NEW-NEW-NEW paint, and The Cloud has
> beamed so brightly only the luddites would consider running their own servers in its shadow.
>
> Meanwhile Amazon in particular is printing profits renting out servers at obscene margins.
> AWS' profit margin is almost 30% ($18.5b in profits on $62.2B in revenue), despite huge
> investments in future capacity and new services.

### Excerpt 3 — "The One Person Framework" (Dec 16, 2021)

URL: https://world.hey.com/dhh/the-one-person-framework-711e6318

> The part that really excites me about this version, though, is how much closer it brings us
> to the ideal of The One Person Framework. A toolkit so powerful that it allows a single
> individual to create modern applications upon which they might build a competitive business.
> The way it used to be. There's so much to learn these days, if you want to be an expert in
> all the latest tools and techniques. The conventional path, as paved by solutions extracted
> from giant tech companies, is a journey akin to The Oregon Trail. You might well die of
> dysentery before you ever get to your destination! Rails 7 seeks to be the wormhole that
> folds the time-learning-shipping-continuum, and allows you to travel grand distances without
> knowing all the physics of interstellar travel. Giving the individual rebel a fighting chance
> against The Empire. You simply can't play by the same rules against an opponent exponentially
> stronger than you. The key engine powering this assault is conceptual compression. Like a
> video codec that throws away irrelevant details such that you might download the film in
> real-time rather than buffer for an hour.

## Canonical posts

1. **Why we're leaving the cloud** (2022-10-19) — https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0 — flagship manifesto: verdict-first thesis, receipt-level numbers, analogy warfare, institutional target.
2. **Integrated systems for integrated programmers** (2020-01-31) — https://signalvnoise.com/svn3/integrated-systems-for-integrated-programmers — attacks an orthodoxy while quoting a critic approvingly; ends in warmth.
3. **The One Person Framework** (2021-12-16) — https://world.hey.com/dhh/the-one-person-framework-711e6318 — release announcement as civilizational vision; "conceptual compression" as argument engine.
4. **Merchants of complexity** (2024-08-24) — https://world.hey.com/dhh/merchants-of-complexity-4851301b — the enemy-naming move distilled.
5. **Less software** (2021-02-23) — https://world.hey.com/dhh/less-software-c69de1e8 — product philosophy as numbered negative list; taste-as-argument.
6. **Optimize for bio cores first, silicon cores second** (2024-09-06) — https://world.hey.com/dhh/optimize-for-bio-cores-first-silicon-cores-second-112a6c3f — reframes a tech debate as an economics bet.

*Note: "The Magic of Rails" is a Rails World 2021 keynote, not a written essay; treat spoken
keynotes separately from the written canon.*
