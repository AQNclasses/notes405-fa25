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
T_{avg}(n) = E_{|X| = n} \[T(X)\] = \sum_{|X| = n} T(X) Pr(X)
$$

What is the hardest part of computing this sum?

Answer: we don't know the probabilities of the inputs.

Instead, in this course we will consider randomized algorithms, where the
algorithm itself makes randomized choices. Then, the running time of a
randomized algorithm is no longer fixed, but itself a random variable.

We can then consider the worst-case expected running time.

$$
T_{worst-expected}(n) = \max_{|X| = n} E \[T(X)\]
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

$$
Pr[T(n) = k] = \begin{cases}
1/n & \text{if k < n-1} \\
2/n & \text{if k=n-1}
\end{cases}
$$

Why two cases? If $k=n-1$, there are two nuts left to consider. The
second-to-last nut either fits our bolt, in which case we terminate our
algorithm, or it doesn't fit, in which case the only remaining nut must fit our
bolt. Either way, we terminate at $k=n-1$, doubling the chance of terminating
after $n-1$ comparisons.

You can think of the order of nuts to be drawn from the pile as a permutation,
since we do not replace the nuts once we've tested them. The odds of the single
nut we're trying to match being in any given position in the order is $1/n$.

Next, we plug our probability into our definition of expecation, separating the
last two terms from the sum at first, then simplifying:

$$
\begin{align*}
E\[T(n)\] & = \sum_{k=1}^{n-2} \frac{k}{n} + \frac{2(n-1)}{n} \\
& = \sum_{k=1}^n \frac{k}{n} - \frac{1}{n} \\
& = \frac{n+1}{2} - \frac{1}{n}
\end{align*}
$$

Alternative solution: We can think about the problem recursively. We always must
perform one test. With probability $1/n$, we find the matching nut and halt.
Otherwise, we recursively solve the problem with one fewer nut, giving the
recurrence

$$
E\[T(n)\] = 1 + \frac{n-1}{n} E\[T(n-1)\]
$$

with the base case $T(1) = 0$.

We can be clever and substitute a simpler function, using $t(n) = n E\[T(n)\]$:

$$
t(n) = n + t(n-1)
$$

and we see that this new recurrence is simply the sum of integers from 2 to $n$.

$$
\begin{align*}
t(n) & = \sum_{k=2}^n k = \frac{n(n+1)}{2} - 1 \\
\to E\[T(n)\] & = \frac{t(n)}{n} = \frac{n+1}{2} - \frac{1}{n}
\end{align*}
$$
