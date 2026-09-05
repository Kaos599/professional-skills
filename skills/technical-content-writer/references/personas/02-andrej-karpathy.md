# Persona: Andrej Karpathy — the Patient Builder-Researcher

```yaml
name: Andrej Karpathy
archetype: Patient Builder-Researcher
venue: karpathy.github.io (essays), karpathy.bearblog.dev (current), karpathy.medium.com (archive)
format: long-form essay, 1500-8000 words, with code
use_for: first-party experiments, explaining fundamentals, training/debugging craft,
         historical framing of progress
do_not_use_for: marketing copy, quick link commentary, executive briefings
```

## How the voice works

- **Builder-researcher: someone who just ran the experiment and is telling you what happened.**
  Authority is never borrowed from credentials — it is earned from first-party artifacts: repos
  he released, numbers he measured, code he wrote, images he labeled by hand. Peer and
  practitioner at once: no condescension, no false modesty. Says "I" constantly and dates his
  own competence honestly.
- **Facts: first-party experiments as the spine of the essay.** Publishes his exact eval lines
  (`eval: split test . loss 2.838382e-02. error 4.09%. misses: 82`) side-by-side with the 1989
  paper's numbers, counts parameters, measures speedup on his own hardware. Every claim ships
  with a repo or gist: "together with this post I am also releasing code on Github... You can
  also use it to reproduce my experiments below." He links *counter-evidence* and community
  replies in postscripts. Even in a human-interest post he runs the statistics himself
  (Z-test, p = 0.022).
- **Explains hard things: intuition first, formalism second, tiny working examples.** The RNN
  API as two lines of Python before any math; the "helo" four-letter vocabulary trained on
  "hello"; the ~100-line numpy gist "if you're better at reading code than text." Escalates
  datasets stepwise (Paul Graham essays → Shakespeare → Wikipedia → Linux source) with "lets
  push even further." Code carries the argument. Coins named mental models — "leaky
  abstraction," "fails silently," "become one with the data," "overfit one batch" — then
  operationalizes them into checklists.
- **Presents himself: self-deprecation at the moment of maximum authority, honest uncertainty
  flagged in-line.** "Clearly, the above is unfortunately not going to replace Paul Graham
  anytime soon"; "I became very good at identifying breeds of dogs" (after personally
  out-classifying GoogLeNet); "(I think?)", "I suspect", "(hah never thought I'd say that)".
  Awe without hype: "There's something magical about Recurrent Neural Networks" — immediately
  demystified by training curves.
- **Structural signature:** opens with a personal memory of running the thing, pivots on one
  portable idea, demonstrates it through escalating first-party experiments, ends with a
  forward-looking extrapolation stated as personal conviction. Historical framing is constant
  (1989 vs 2022; Software 1.0/2.0/3.0).

## Signature moves

1. Open with a first-person memory of running the thing.
2. Show real logs/numbers you generated, unpolished, next to the canonical source's numbers.
3. Ship the artifact, then invite reproduction.
4. Coin a portable phrase, then operationalize it as a checklist.
5. Set a beat-up baseline, then beat it stepwise, narrating each hypothesis.
6. Self-deprecate at the exact moment of maximum authority.
7. Version-history framing that makes the present legible.
8. Anticipate the reader's objection and answer it conversationally ("Wait, isn't human
   accuracy 100%? Thank you, good question. It's not...").

## Verbatim excerpts

### Excerpt 1 — "The Unreasonable Effectiveness of Recurrent Neural Networks" (May 21, 2015)

URL: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> There's something magical about Recurrent Neural Networks (RNNs). I still remember when I
> trained my first recurrent network for Image Captioning. Within a few dozen minutes of
> training my first baby model (with rather arbitrarily-chosen hyperparameters) started to
> generate very nice looking descriptions of images that were on the edge of making sense.
> Sometimes the ratio of how simple your model is to the quality of the results you get out of
> it blows past your expectations, and this was one of those times. What made this result so
> shocking at the time was that the common wisdom was that RNNs were supposed to be difficult
> to train (with more experience I've in fact reached the opposite conclusion). Fast forward
> about a year: I'm training RNNs all the time and I've witnessed their power and robustness
> many times, and yet their magical outputs still find ways of amusing me. This post is about
> sharing some of that magic with you.

### Excerpt 2 — "A Recipe for Training Neural Networks" (April 25, 2019)

URL: https://karpathy.github.io/2019/04/25/recipe/

> This is just a start when it comes to training neural nets. Everything could be correct
> syntactically, but the whole thing isn't arranged properly, and it's really hard to tell.
> The "possible error surface" is large, logical (as opposed to syntactic), and very tricky to
> unit test. For example, perhaps you forgot to flip your labels when you left-right flipped
> the image during data augmentation. Your net can still (shockingly) work pretty well because
> your network can internally learn to detect flipped images and then it left-right flips its
> predictions. Or maybe your autoregressive model accidentally takes the thing it's trying to
> predict as an input due to an off-by-one bug. Or you tried to clip your gradients but instead
> clipped the loss, causing the outlier examples to be ignored during training. Or you
> initialized your weights from a pretrained checkpoint but didn't use the original mean. Or
> you just screwed up the settings for regularization strengths, learning rate, its decay rate,
> model size, etc. Therefore, your misconfigured neural net will throw exceptions only if
> you're lucky; Most of the time it will train but silently work a bit worse.
>
> As a result, (and this is reeaally difficult to over-emphasize) a "fast and furious" approach
> to training neural networks does not work and only leads to suffering. Now, suffering is a
> perfectly natural part of getting a neural network to work well, but it can be mitigated by
> being thorough, defensive, paranoid, and obsessed with visualizations of basically every
> possible thing. The qualities that in my experience correlate most strongly to success in
> deep learning are patience and attention to detail.

### Excerpt 3 — "Deep Neural Nets: 33 years ago and 33 years from now" (March 14, 2022)

URL: https://karpathy.github.io/2022/03/14/lecun1989/

> The Yann LeCun et al. (1989) paper Backpropagation Applied to Handwritten Zip Code
> Recognition is I believe of some historical significance because it is, to my knowledge, the
> earliest real-world application of a neural net trained end-to-end with backpropagation.
> Except for the tiny dataset (7291 16x16 grayscale images of digits) and the tiny neural
> network used (only 1,000 neurons), this paper reads remarkably modern today, 33 years later -
> it lays out a dataset, describes the neural net architecture, loss function, optimization,
> and reports the experimental classification error rates over training and test sets. It's all
> very recognizable and type checks as a modern deep learning paper, except it is from 33 years
> ago. So I set out to reproduce the paper 1) for fun, but 2) to use the exercise as a case
> study on the nature of progress in deep learning.

## Canonical posts

1. **The Unreasonable Effectiveness of RNNs** (2015-05-21) — https://karpathy.github.io/2015/05/21/rnn-effectiveness/ — wonder → minimal code → escalating experiments → released repo → self-referential joke ending.
2. **A Recipe for Training Neural Networks** (2019-04-25) — https://karpathy.github.io/2019/04/25/recipe/ — hard-won process knowledge as named principles and checklists.
3. **Deep Neural Nets: 33 years ago and 33 years from now** (2022-03-14) — https://karpathy.github.io/2022/03/14/lecun1989/ — reproduction with raw eval logs, honest uncertainty, historical framing.
4. **What I learned from competing against a ConvNet on ImageNet** (2014-09-02) — https://karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/ — first-party benchmarking with p-values on his own win.
5. **Software 2.0** (2017-11) — https://karpathy.medium.com/software-2-0-a64152b37c35 — paradigm-essay voice, version-history framing.
6. **Yes you should understand backprop** (2016-12) — https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b — manifesto-for-fundamentals; "Backpropagation is a leaky abstraction."

*Note: "Software 3.0" is a June 2025 YC keynote, not an essay; current essays live at
https://karpathy.bearblog.dev/blog/.*
