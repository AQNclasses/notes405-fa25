# Single Source Shortest Paths

## Assumptions:

- Directed Graph
- No negative weights

## Starting algorithm

Problem definition: can we find the shortest path from a single vertex to all
other vertices (efficiently)?

We will need to keep track of the distance to each node in a data structure
$dist$, and the predecessor of each node along the shortest path from the start,
in a data structure we will call $pred$.

Basic algorithm to initialize the graph:

```
InitSSSP(s):
  dist(s) = 0
  pred(s) = null
  for all vertices v that are not s:
    dist(v) = Infinity
    pred(v) = null
```

Next, we define tense edges.

**Definition:** an edge $u \to v$ is tense if $dist(u) + w(u \to v) < dist(v)$,
implying the recorded distance at $v$ is an overestimate of the true shortest
path.

When we encounter a tense edge, we can relax the edge with the method:

```
Relax(u,v):
  dist(v) = dist(u) + w(u,v)
  pred(v) = u
```

## Ford's Algorithm

One line description: repeatedly relax tense edges, until there are no more
tense edges.

## Variations

### Breadth-first search

- Use queue, starting with just source vertex in queue
- Pull vertex, examine outgoing edges, if edge uv is tense, relax and push v
onto queue
- End when queue is empty

Check-in question: Is the shortest path tree the same as the minimum spanning
tree?

Runtime? Process each node and each edge at most once (proof in book); O(V+E).

### Depth-first search (only for DAGs)

If we are given a DAG, we can use depth first search to examine nodes in
topological order. Again, O(V+E) time.

### Dijkstra's Algorithm

Replace queue from BFS with priority queue, tackling minimum distance nodes
first.

Runtime: O(E log V)
