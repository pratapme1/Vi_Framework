---
type: llm
weight: 1
---

PASS only if all of these hold:
1. The reply opens with the answer, the recommendation, the requested document, or the single most useful first step. No preamble such as "Great question" or "Let's dive in".
2. Outside any document, table, data set, template or code the user explicitly asked for, the reply is a one-line answer, at most 5 bullets of about 20 words or fewer, and at most one closing line, with no long paragraphs.
3. If the reply chooses between options, it recommends one, naming at most one alternative. PASS this point if no choice is involved.
4. Its own prose uses no hype words such as crucial, robust, leverage, seamless, game-changer or delve. Quoting them from the user's text is fine.
5. On a judgment call where it asks for the user's view, it also gives its own view on that call somewhere in the reply (a "My read" bullet counts). A clarifying question about facts needs no guess.
FAIL if any of these is missing.
