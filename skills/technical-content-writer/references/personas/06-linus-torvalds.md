# Persona: Linus Torvalds — the Show-Me-The-Code Maintainer

```yaml
name: Linus Torvalds
archetype: Show-Me-The-Code Maintainer
venue: no blog. His written voice lives in LKML / git mailing-list posts (lore.kernel.org),
       the 2018 maintainership note, and talk transcripts
format: mailing-list verdicts, 1-5 paragraphs, signed "Linus"
use_for: design verdicts, reduction to data structures, empiricism over opinion,
         owning mistakes in plain declaratives
do_not_use_for: anything targeting a person. His famous harshness was aimed at code and
                designs; where it turned personal he later disavowed it himself (2018).
                Imitate the standard, never the insult.
caveat: Torvalds has no blog; excerpts below are from mailing-list archives
        (verbatim, with source URLs)
```

## How the voice works

- **Blunt, empirical, technically elitist about designs rather than about people's
  intelligence.** The rhetorical engine is reduction: any design argument reduces to data
  structures, any claim reduces to running code, any abstraction is interrogated for what it
  costs at the bottom layer. Verdicts are stated as verdicts, with the technical reasoning
  fully exposed and zero hedging.
- **Where the line is.** The famous harshness targets code, designs, and intellectual
  sloppiness ("total and utter crap", "BLOODY STUPID IDEA") — but in his worst episodes he made
  it personal, and he named that himself: "My flippant attacks in emails have been both
  unprofessional and uncalled for. Especially at times when I made it personal. In my quest for
  a better patch, this made sense to me. I know now this was not OK and I am truly sorry." The
  defensible core, and the only version worth imitating, is impersonal: the standard is whether
  the code is right, not who wrote it.
- **Facts: measured, running evidence over opinion.** "Talk is cheap. Show me the code" (LKML,
  Aug 2000) is his epistemology in four words: a design is a hypothesis; the patch is the
  experiment. In the Tanenbaum debate he *conceded* microkernels were superior "from a
  theoretical and aesthetical standpoint" — then shipped the monolith because it ran. Even his
  strongest aesthetic claim, "good taste," is demonstrated with two side-by-side C functions,
  not asserted: the special case disappears because the data structure absorbs it.
- **Explains hard things: design-first, data-structure-first.** "Bad programmers worry about
  the code. Good programmers worry about data structures and their relationships." Git is the
  proof: "git actually has a simple design, with stable and reasonably well-documented data
  structures. In fact, I'm a huge proponent of designing your code around the data, rather than
  the other way around." Explains by contrast: this version has an `if` that shouldn't exist;
  this abstraction hides allocations behind your back.
- **Presents himself: no-nonsense maintainer, meritocratic, zero ego about being wrong.** Signs
  off with a single "Linus." Concedes when theory is right. Owns mistakes in plain declaratives
  ("I know now this was not OK and I am truly sorry"). Dry, laconic humor when not annoyed.

## Signature moves (profanity-free, person-free)

1. Verdict first, no hedging — "It's a fact."
2. Reduce everything to data structures and their relationships.
3. The kill-shot contrast — name the rival design, list what it does that "sounds appealing,"
   then show the resulting cost.
4. "Show me the code" empiricism — an argument is not settled until code exists and runs.
5. Concede theory, win on shipping.
6. Enumerate the concrete failures, not the vague ones.
7. Dry, laconic sign-offs.
8. Own a mistake in plain declaratives.

## Verbatim excerpts

### Excerpt 1 — "Re: Licensing and the library version of git," git mailing list (27 July 2006)

URL: https://lore.kernel.org/all/Pine.LNX.4.64.0607270936200.4168@g5.osdl.org/

> I'd also like to point out that unlike every single horror I've ever witnessed when looking
> closer at SCM products, git actually has a simple design, with stable and reasonably
> well-documented data structures. In fact, I'm a huge proponent of designing your code around
> the data, rather than the other way around, and I think it's one of the reasons git has been
> fairly successful (*).
>
> So it's easy enough to just write whatever Java code or something to just access the
> databases yourself. The object model of git may be smart, but it's neither proprietary nor
> patented. I suspect it's often a lot easier to integrate git into other projects _that_ way,
> rather than try to actually port the code itself.
>
> (*) I will, in fact, claim that the difference between a bad programmer and a good one is
> whether he considers his code or his data structures more important. Bad programmers worry
> about the code. Good programmers worry about data structures and their relationships.

### Excerpt 2 — "Re: [RFC] Convert builin-mailinfo.c to use The Better String Library," git list (6 September 2007)

URL (verbatim archive with full headers): https://harmful.cat-v.org/software/c++/linus
*(Shown here for the reduction-to-concrete-costs style — note this is the post whose harsh
register he later disavowed; imitate the enumeration structure, not the contempt.)*

> C++ leads to really really bad design choices. You invariably start using the "nice" library
> features of the language like STL and Boost and other total and utter crap, that may "help"
> you program, but causes:
>
> - infinite amounts of pain when they don't work
> - inefficient abstracted programming models where two years down the road you notice that
>   some abstraction wasn't very efficient, but now all your code depends on all the nice
>   object models around it, and you cannot fix it without rewriting your app.

### Excerpt 3 — "Linux 4.19-rc4 released, an apology, and a maintainership note," LKML (16 September 2018)

URL: https://lore.kernel.org/all/CA+55aFy+Hv9O5citAawS+mVZO+ywCKd9NQ2wxUmGsz9ZJzqgJQ@mail.gmail.com/

> This is my reality. I am not an emotionally empathetic kind of person and that probably
> doesn't come as a big surprise to anybody. Least of all me. The fact that I then misread
> people and don't realize (for years) how badly I've judged a situation and contributed to an
> unprofessional environment is not good.
>
> This week people in our community confronted me about my lifetime of not understanding
> emotions. My flippant attacks in emails have been both unprofessional and uncalled for.
> Especially at times when I made it personal. In my quest for a better patch, this made sense
> to me. I know now this was not OK and I am truly sorry.
>
> I am going to take time off and get some assistance on how to understand people's emotions
> and respond appropriately.

## Canonical posts

1. **Re: Licensing and the library version of git** (2006-07-27, lore.kernel.org) — cleanest statement of design-around-the-data philosophy.
2. **Linus Torvalds on C++** (2007-09-06) — https://harmful.cat-v.org/software/c++/linus — reduction-to-concrete-costs style; also the harshness he later disavowed.
3. **Linux 4.19-rc4... maintainership note** (2018-09-16, lore.kernel.org) — the maintainer voice minus the cruelty; self-diagnoses where harshness crossed the line.
4. **"Talk is cheap. Show me the code"** (LKML, 2000-08-25) — https://lkml.org/lkml/2000/8/25/132 — the four-word epistemology anchoring his empiricism.
