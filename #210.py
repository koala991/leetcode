class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = Graph(list(range(numCourses)), [], prerequisites)

        course_queue, learned = [], [] 
        while len(graph) > 0:
            n_add = 0
            for course in graph.getNodes():
                if graph.getInDegree(course) == 0:
                    course_queue.append(course)
                    n_add += 1
            if n_add == 0 and len(graph) > 0:
                return []

            while len(course_queue) > 0:
                course = course_queue.pop(0)
                learned.append(course)
                graph.delete(course)
                
        return learned
        

class Graph(object):
    def __init__(self, nodes, pairs_1=[], pairs_2=[]):
        self.graph = {node: [[], []] for node in nodes} 
        for i, j in pairs_1:
            self.graph[i][0].append(j)
            self.graph[j][1].append(i)
        for j, i in pairs_2:
            self.graph[i][0].append(j)
            self.graph[j][1].append(i)

    def getOutDegree(self, node):
        return len(self.graph[node][0])

    def getInDegree(self, node):
        return len(self.graph[node][1])

    def delete(self, node):
        for n in self.graph[node][0]:
            self.graph[n][1].remove(node)
        for n in self.graph[node][1]:
            self.graph[n][0].remove(node)
        _ = self.graph.pop(node)
        return 
    
    def getNodes(self):
        return self.graph.keys()

    def __len__(self):
        return len(self.graph)    


