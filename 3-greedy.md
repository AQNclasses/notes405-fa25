# Greedy Algorithms

## Class Scheduling Problem

## Knapsack problem

See worksheet.

## Storing Files on Tape

(4.1 in the textbook)

Consider storing $n$ files on magnetic tape.

Let $L[1..n]$ be an array listing the lengths of each file $i$.

The cost of accessing the $k$th file is:

$$
cost(k) = \sum_{i=1}^k L[i]
$$

Why? (We must scan past all other files on the tape).

The *expected* cost of reading a random file is

$$
E[cost] = \sum_{j=1}^n \frac{cost(j)}{n} = \frac{1}{n} \sum_{j=1}^n \sum_{i=1}^j L[i].
$$
