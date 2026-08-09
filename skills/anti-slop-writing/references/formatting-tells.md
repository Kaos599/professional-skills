# Formatting tells

Formatting should follow content. When it decorates instead, it reads as generated.

## Punctuation

**Em dashes.** Addressed by 84 of 100 harvested skills, the highest-consensus item in the
entire corpus. One skill citing a January 2026 comparison of 200 frontier-model samples against
6,000 human texts reports em dash at 16.9x the human rate, colon at 4.1x, semicolon at 3.1x.
(Reported by that skill; not independently verified here.)

The corpus splits on how hard to ban:
- Strict position: zero em dashes in short copy, social posts, email, and casual text.
- Moderate position: 1 to 2 in a long piece are fine when they clearly beat a comma, period,
  or parentheses.

**Resolution:** default to zero in anything under 500 words. In longer pieces allow at most one
per 500 words, never clustered, never as a rhythm crutch. **Never replace an em dash with a
hyphen.** Use a period, comma, or parentheses. Replace per occurrence, never with a blanket
find-and-replace, because the right substitute differs by clause. A blanket sweep will produce
sentences that are grammatical and wrong.

Note the counter-signal: some current models produce nearly dash-free output. Zero em dashes
proves nothing on its own.

**Colons and semicolons.** Watch density alongside dashes. Real people rarely use semicolons
in casual writing. Keep them for formal quotation, required syntax, or a genuinely complex list.

**Smart quotes.** Curly quotes and apostrophes outside code blocks usually mean the text was
pasted from a chat window or word processor. Use straight quotes.

**Ellipsis outside quotation.** A trailing-off tell.

## Markdown and layout

**Emoji in headings.** Flagged by 32 of 100 skills. Also: emoji as bullet markers, coloured
dots as status indicators, decorative Unicode glyphs used as icons.

**Bold sprinkled mid-sentence** for emphasis. Emphasise by word choice and position instead.

**The numbered-bold-colon list format.** A numbered list where every item is a bold phrase, a
colon, then a description. This specific shape is one of the most recognisable
generated-document signatures. Use plain prose or simple bullets.

**Bullets where prose reads better.** Lists carry parallel items; prose carries argument.
If the items are not genuinely parallel, write sentences. If the same shape repeats 3+ times
with the same fields, use a table instead.

**Headers over two-sentence sections.** Heading density should match content density. Keep
hierarchies flat, since one level deep is usually enough.

**Title Case headings.** Use sentence case unless house style says otherwise.

**Uniform section lengths and identical paragraph counts per section.**

**Every section ending with a takeaway or bottom line.**

## Mechanical paste-tells

Strip these on sight. No judgment call required.

- Unfilled placeholders: `[Your Name]`, `[INSERT SOURCE URL]`, `[insert X here]`, `2025-XX-XX`
- Chat-tool citation markup: `oaicite`, `contentReference`, `turn0search0`, `grok_card`
- AI-tool URL tracking parameters
- Chatbot artifacts left in the body: "Great question!", "I hope this helps!", "Certainly!",
  "You're absolutely right!", "Let me know if you'd like me to expand"
- Identity leaks: "As a large language model", "As an AI assistant"

## Verifiable references

If the draft contains any of the following, check each one. Generated text invents these
confidently:

- Backticked file paths: does the file exist?
- Quoted identifiers, function names, config keys, CLI flags: do they exist in the code?
- Recommended package installs: does the package resolve? Watch for names close to real ones.
- Cited URLs: does each return 200?
- Citations, journals, volume and page numbers, quotes attributed to named people
- Misattributed quotes. Einstein, Seneca, Confucius, and the Buddha are the usual victims.
