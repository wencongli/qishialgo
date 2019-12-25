'''
Method1:
using list to represent path
Runtime: 136 ms, faster than 24.00% of Python3 online submissions for Course Schedule.
Memory Usage: 16.5 MB, less than 10.20% of Python3 online submissions for Course Schedule.
'''

import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort <==> DAG
        # detect if there is cycle, using DFS
        
        # first, build up the graph
        graph=collections.defaultdict(set)
        # traverse each edge
        for edge in prerequisites:
            nxt, prv = edge
            # course nxt needs course prv as prerequisite
            graph[nxt].add(prv)
        
        def DFS(course):
            visited.add(course)
            # if course doesn't have any prerequisite, label it and return true
            if course not in graph:
                return True
            else:
                path.append(course)
                for nxt_course in graph[course]:
                    # if there is a cycle, return false
                    if nxt_course in path:
                        return False
                    if nxt_course not in visited:
                        if(DFS(nxt_course) is False):
                            return False
                path.pop()
        
        # then DFS
        visited=set()
        path=[]
        for course in range(numCourses):
            if course not in visited:
                if(DFS(course) is False):
                    return False         
                
        return True


'''
Method2:
using set, instead of list, to represent path
“if element in path”: O(1) if path is set, O(n) if path is list
all of the courses are distinct, so set can be used to represent path

Runtime: 96 ms, faster than 94.63% of Python3 online submissions for Course Schedule.
Memory Usage: 16.5 MB, less than 12.25% of Python3 online submissions for Course Schedule.
'''


import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort <==> DAG
        # detect if there is cycle, using DFS
        
        # first, build up the graph
        graph=collections.defaultdict(set)
        # traverse each edge
        for edge in prerequisites:
            nxt, prv = edge
            # course nxt needs course prv as prerequisite
            graph[nxt].add(prv)
        
        def DFS(course):
            visited.add(course)
            # if course doesn't have any prerequisite, label it and return true
            if course not in graph:
                return True
            else:
                path.add(course)
                for nxt_course in graph[course]:
                    # if there is a cycle, return false
                    if nxt_course in path:
                        return False
                    if nxt_course not in visited:
                        if(DFS(nxt_course) is False):
                            return False
                path.remove(course)
        
        # then DFS
        visited=set()
        path=set()
        for course in range(numCourses):
            if course not in visited:
                if(DFS(course) is False):
                    return False         
                
        return True
