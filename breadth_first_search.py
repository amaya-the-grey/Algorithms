import numpy as numpy

'''
Breadth First Search aims to check each vertex of a graph while avoiding
cycles. Starting with a root vertex, each adjacent vertex is added to the
back of a queue, and the next vertex in the queue is visisted and removed
from the queue. This continues, avoiding repeats and cycles, until the
queue is empty and the graph has been traversed. 
'''

def breadth_first_search(graph, root):
    visited = []
    queue = []

    visited.append(root)
    for adjacent_vertex in graph[root]:
        queue.append(adjacent_vertex)

    while len(queue) != 0:
        for vertex in queue:
            if vertex not in visited:
                visited.append(vertex)
                for adjacent_vertex in graph[vertex]:
                    if adjacent_vertex in queue:
                        continue
                    else:
                        queue.append(adjacent_vertex)
            queue.pop(0)
            #print(visited, queue)





if __name__ == '__main__':
  graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
  breadth_first_search(graph, 0)
