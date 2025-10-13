# Randomized Algorithms

Suppose we are given $n$ nuts and $n$ bolts. Each nut matches one bolt and vice
versa.

The nuts and bolts are too close in size to distinguish by eye, but if you try a
nut and bolt pair together, the nut will be either too big, too small, or just
right. We have no way of comparing bolts to bolts, or nuts to nuts.

First problem: suppose we want to find the nut that matches a particular bolt.

Runtime? $n-1$

What about choosing randomly? Intuition: look at $n/2$ nuts on average.

How to formalize?

## Deterministic vs. Randomized Algorithms

Most algorithms we have seen so far are deterministic.

Their worst-case running time is the maximum over all problems of a certain
size:

$$
T_{worst}(n) = \max_{|X| = n} T(X)
$$

Average-case running time is defined by the expected value over all inputs:


$$
T_{avg}(n) = \E_{|X| = n} \[T(X)\] = \sum T(X) Pr(X)
$$

What is the hardest part of computing this sum?

Answer: we don't know the probabilities of the inputs.

Instead, in this course we will consider randomized algorithms, where the
algorithm itself makes randomized choices. Then, the running time of a
randomized algorithm is no longer fixed, but itself a random variable.

We can then consider the worst-case expected running time.

$$
T_{worst-expected}(n) = \max_{|X| = n} \E \[T(X)\]
$$

## Back to nuts and bolts

Let $T(n)$ denote the number of comparisons we use to find a match for a single
bolt and $n$ nuts.

Consider an algorithm where we choose a nut uniformly at random from the
untested nuts.

We have some base cases:  $T(1) = 0$ and $T(2) = 1$.

However, beyond this point, $T(n)$ is a random variable.

If the target nut is the $kth$ nut tested, our algorithm performs $\min{k, n-1}$
comparisons.

How would we write down the probability of exactly $k$ comparisons?

\begin{equation}
Pr[T(n) = k] = \cases{1/n \text{if k < n-1}}{2/n \text{if k=n-1}}
\end{equation}
