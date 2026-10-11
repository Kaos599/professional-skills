# Cold opens: fact list → human story

Each example shows the same opening twice. The first version is a fact list (what a first
draft tends to produce). The second is the human version the standard asks for: a scene
with stakes, the one hard fact, a person, then scale. Every scene is illustrative and
framed with "Picture…". Real numbers in a real post need FACTS rows.

## 1. Monitoring (the kit's running example)

**Fact list.** Large retailers handle millions of requests per minute during sales events.
Outages as short as a few seconds can cost revenue. Monitoring systems scrape metrics at
fixed intervals, typically 15 to 60 seconds, which can miss short incidents.

**Human.** Picture 9:02 on the biggest sales morning of the year. The payment service stops
answering for four seconds. The dashboard scrapes every fifteen, so on the graph nothing
happened. Somewhere a customer's card was declined at the last step, and they closed the
tab. Someone has to notice that, find those four seconds in a day of logs, and wake the
right person, and the sale doesn't pause while they look.

## 2. Video highlights (sports media)

**Fact list.** Leagues play thousands of games per season. Each broadcast runs for hours.
Highlights must be clipped, reframed and published quickly.

**Human.** Picture the last over of a final, with 10 needed off 2 balls. The batter swings,
and bat meets ball for about a millisecond, which is shorter than one frame of the
broadcast. Somewhere a fan missed it because their stream buffered at the wrong second. They
want it on their phone before the next over, and someone has to find it, cut it and frame it
while the match keeps going.

## 3. Payments

**Fact list.** Card networks process thousands of transactions per second. Fraud models must
score each one within a strict latency budget.

**Human.** Picture a nurse buying fuel at 6 a.m. after a night shift. The terminal waits,
then declines. The fraud model needed 40 milliseconds it didn't have, and the network
timed out first. She tries again, it works, and she never knows a model just made a
decision about her. Now make that decision correctly, in time, for every swipe on every
card.

## 4. Search / RAG

**Fact list.** Retrieval-augmented generation systems retrieve documents to ground model
answers. Retrieval quality strongly affects answer accuracy.

**Human.** Picture a support agent with a customer on hold, asking the internal assistant how
refunds work for annual plans. It answers confidently from last year's policy, because the
new one sits in a PDF that was never re-indexed. The agent reads it out. The customer is
right to be annoyed, and nothing in the logs says anything went wrong.

## 5. ML training

**Fact list.** Large training runs use thousands of GPUs. Hardware failures are common and
checkpointing is expensive.

**Human.** Picture day nine of a twelve-day training run. At 3:14 a.m. one GPU out of two
thousand starts returning garbage, quietly. Loss doesn't spike, it just stops improving. The
engineer on call finds out at standup, and nine hours of a very expensive cluster have
gone into learning nothing.

## What the human versions have in common

- A specific moment (a time, a place, a stake) in the present tense.
- One hard physical or system fact, given as a comparison the reader can feel.
- A person affected, with a detail from the medium (buffered stream, declined terminal,
  confident wrong answer). No assumed feelings.
- A pivot to the job ("someone has to…") and to scale ("now do that for every…").
- No statistics inside the scene. They belong in the scale paragraph, with sources.
