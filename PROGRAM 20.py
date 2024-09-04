from queue import Queue
graph={'A':['B','D','E','F'],
       'D':['A'],
       'B':['A','F','C'],
       'F':['B','A'],
       'C':['B'],
       'E':['A'],
       }
print("given graph is")
print(graph)
def BFS_TRAVERSAL(input_graph,source):
    Q=Queue()
    visited_vertices=list()
    Q.put(source)
    visited_vertices.append(source)
    while not Q.empty:
        vertex=Q.get
        print(vertex,end="->")
        for u in input_graph[vertex]:
            if u not in visited_vertices:
                Q.put(u)
                visited_vertices.append(u)
print("BFS_TRAVERSAL GRAPH IS:")
BFS_TRAVERSAL(graph,'A')
            

            
   