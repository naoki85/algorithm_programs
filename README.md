# algorithm_programs
These are algorithm programs I created myself.  
My Blog is [here](https://www.notion.so/naoki85/bcb265ad5edc493183984921c9a91270?v=0a92bc7ee9a544519f0b3615ebb1ea77)

## BellmanFord

```python
# [0 => 0, destination_vertex_number => start_vertex_number]
# For example
# 1 => 2  weight is 10
# 2 => 3  weight is 20
edges = [[None, None, None], [None, None, None, None], [None, 10, None, None], [None, None, 20, None]]
bf = BellmanFord(edges, 3)
bf.run(1)
bf.get_shortest_weight(2)
```

## Binary Search Tree

```python
b = Bst(8)
b.insert(4)
b.insert(10)
res = b.find_value_from_order(3)
```

## Dijkstra

```python
# [0 => 0, start_vertex_number => destination_vertex_number]
# For example
# 1 => 2  weight is 10
# 2 => 3  weight is 20
edges = [[None, None, None], [None, None, 10, None], [None, None, None, 20], [None, None, None, None]]
d = Dijkstra(edges, 3)
d.run(1)
d.get_shortest_weight(2)
```

## Eratosthenes 

```python
Eratosthenes.search(10)
```

## Karatsuba

```python
Karatsuba.multiplication(10, 20)
```

## Kosaraju

```python
edges = [[], [2], [1], [6], [], [8], [5], [3], [7]]
k = Kosaraju(edges, 8)
k.run()
k.get_summary()
```

## Lcs

Compute the two letter "Longest Common Subsequence".  
Referred to the content published in [Software Design](https://gihyo.jp/magazine/SD/archive/2021/202103).

```python
lcs = Lcs("SOFT", "OFF")
lcs.calc()
```

## MergeSort

```python
MergeSort.exec([1, 2, 3, 4, 5])
```

## MinIntHeap

```python
h = MinIntHeap()
h.add(10)
a = h.poll()
```

## QuickSort

```python
QuickSort.exec([1, 2, 3, 4, 5])
```

## Rotate 2D Array

```python
res = Rotate2dArray.turn_left90([[1, 2], [3, 4]])
```

## UnionFind

```python
uf = UnionFind(3)
uf.find(1)
uf.union(2, 3)
```
