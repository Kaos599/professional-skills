---
source:    LinkedIn
author:    provided by user
authored:  true
format:    linkedin post
added:     2026-08-08
notes:     |
  Technical decision-procedure post. Highest-value traits to copy:
  - Opens with "tl;dr" then two one-line ">" claims that each stand alone
  - Mechanism before advice: explains prefill vs decode before recommending anything
  - Names the wrong method explicitly (the a/b/c/d list) before giving the right one
  - Ends on a rule, not a summary: "the choice of engine just follows"
  - Zero em dashes across the whole piece
  - Lowercase sentence starts throughout, including "i"
  - Numbers used as texture, not decoration: 180 tok/s, 1K in / 128 out, 80K context, 24gb
  - Condition-to-tool mapping as the payload (weird+offline -> GGUF, mac -> MLX, etc.)
  - Deliberate comma splices and run-ons; at least one ungrammatical line kept as-is
  - Second person throughout: "your workload shape", "you live and die by"
---

tl;dr
> VRAM tells you what fits. and not how fast model runs.
> decode is limited by how fast memory feeds the chip, not by raw compute. a smaller, better-fed GPU can beat a bigger one.

inference is not one operation. it's two.

"prefill" reads your whole prompt and builds the KV cache. it's heavy on compute.
"decode" produces one token at a time, re-reading the weights and cache every step. it's bottlenecked on memory bandwidth.

so your workload shape changes everything: short prompt, long answer, you live and die by memory bandwidth. long prompt, short answer, attention kernels and the prefill path matter most. many users at once, the scheduler is the whole game.

when picking stack, i've seen people doing this -
a) count the VRAM.
b) find a benchmark screenshot with a big tokens per second number.
c) pick the engine with the biggest number.
d) buy the card with the most memory.

but it's not the appropriate.

let's say benchmark said 180 tok/s figure, it might have come from one user, one prompt shape, probably a 1K in, 128 out toy run. but the coding agent, you are gonna be using local-llm for will drag 80K of context for example

you must not start from the engine.
you must start from: what hardware is actually in the rack. whether the model sits in fast memory or spills into slow shared memory.
whether your problem is prefill or decode.
how long context runs and how many users hit it at once. whether prompts share prefixes you can cache.

answer those and the engine picks itself:
weird, offline, cpu-heavy, edge, GGUF, llama.cpp.
mac with big unified memory, MLX. models fit that never would on a 24gb card, but memory is slower, so you trade speed for capacity. one 4090 or 5090 on low-bit weights, ExLlamaV2.
a few consumer nvidia cards or local MoE, ExLlamaV3.
serving open models in production, vLLM, the safe default.
long context, MoE, routing, disaggregation, SGLang.
all nvidia, squeezing the last drop, TensorRT-LLM. a whole fleet, put Dynamo on top.

and remember - without a fast interconnect like NVLink, spraying tensor parallelism across multiple GPUs can be slower than plain pipeline parallelism. the moment a model crosses a GPU boundary you start paying a communication tax, and cheap PCIe links make you pay a lot of it.

so before anyone argues about which engine wins, answer the fundamental questions first. the hardware and the workload decide. the choice of engine just follows.
