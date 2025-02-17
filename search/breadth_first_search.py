from collections import deque

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'F'],
  'C' : ['G'],
  'D' : [],
  'E' : [],
  'F' : ['H'],
  'G' : ['I'],
  'H' : [],
  'I' : []
}


def bfs(graph, node):
    visited = set()
    queue = deque()

    visited.add(node)
    queue.append(node)

    while queue:
        # popleft is O(1). For an array, pop(0) is O(n). Hence the change to deque from array.
        s = queue.popleft()
        visited.add(s)
        print(s, end = ' ')

        for n in graph[s]:
            # Because visited is a set, this lookup is O(1).
            if n not in visited:
                queue.append(n)


def main():
    bfs(graph, 'A')


main()
