# Dynamic Programming


## Induction Review

Steps in inductive proof:

1. Prove base case
2. Assume that what you are trying to prove for all $n$ is true for (all or some) $k < n$.

Let $S(n)$ be a logical statement, indexed by an integer $n$.

If $S(0)$ holds, and $S(k) \to S(k+1)$, then $S(n)$ is true for all integers
$n$.

Example:

$$
\sum_{i=1}^n i = \frac{n(n+1)}{2}
$$

## Rod Cut


- Refer to Worksheet 1, "Rod Cut" problem

How to formulate a recursion for this problem?

Goal: find **optimal substructure**, such that the optimal solution to the
original problem incorporates optimal solutions to the subproblems.

At each stage of the algorithm, we are making one cut (or stopping and taking
revenue as-is).

To find revenue $r_n$, we search exhaustively over all possible options, finding the maximum over:

- $p_n$: the revenue from stopping here and making no more cuts.
- $r_1 + r_{n-1}$: max from a rod of size 1 and a rod of size $n-1$.
- $r_2 + r_{n-2}$: max from a rod of size 2 and a rod of size $n-2$.
- $\ldots$
- $r_{n-1} + r_1$

Written another way:

$$
r_n = \max \{ p_n, r_1 + r_{n-1}, \ldots, r_{n-1} + r_1 \}
$$

In functional notation:

$$
RodCut(n) = \max \{ p_n, RodCut(1) + RodCut(n-1), \ldots, RodCut(n-1) +
RodCut(1) \}
$$

Observations?

1. $p_n$ on its own is weird
2. Many repeated sub-problems

Reminder: *Recursion Trees* (draw on board, write down recurrence)

Another way to think of the problem: we cut off a rod at "the front", sell that
at price, and recurse on the remainder of the rod. Then, we are searching over
all lengths of rod to sell in the first step.

Can reformulate as:

$$
r_n = \max \{ p_i + r_{n-i} : 1 \leq i \leq n \}
$$

Still: many sub-problems, repeated. How to analyze performance?

We write down a **recurrence** that summarizes the performance of the
**recursive algorithm.**
