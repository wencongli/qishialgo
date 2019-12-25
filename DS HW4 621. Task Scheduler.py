'''
method 1: DFS  # max time exceed, not accepted
'''

import sys
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # step 1: scan entire array to find the num of tasks
        task_kind=26
        task_num=[0]*task_kind
        for char in tasks:
            task_num[ord(char)-ord('A')]+=1
        
        # task_time record the start time of most recent task
        task_time=[-(n+1)]*task_kind
        
        # step 2: DFS/BFS to find the minimum intervals to finish all
        self.min_time=sys.maxsize
        
        # DFS: test every task, with >0 tasks remaining
        # memorization
        
        def DFS(time):
            # if all remaining task are done, convergence status
            if 0==sum(task_num):
                self.min_time=min(self.min_time, time)
            
            for task_ind in range(task_kind):
                if task_num[task_ind]>0:
                    # can explore this task_ind 1 level down
                    nxt_time=max(task_time[task_ind]+n+1, time)
                    # pruning
                    if nxt_time>self.min_time:
                        continue
                    task_num[task_ind]-=1
                    temp=task_time[task_ind]
                    task_time[task_ind]=nxt_time
                    DFS(nxt_time)
                    
                    # backtracking
                    task_num[task_ind]+=1
                    task_time[task_ind]=temp
        DFS(0)
        return self.min_time

'''
method 2: greedy (always choose the most frequent task first)

Runtime: 884 ms, faster than 8.00% of Python3 online submissions for Task Scheduler.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Task Scheduler.
'''

import sys
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # step 1: scan entire array to find the num of tasks
        task_kind=26
        task_num=[0]*task_kind
        for char in tasks:
            task_num[ord(char)-ord('A')]+=1
        
        # step 2: for each round, use greedy algo to pick the task with highest freq
        # set up the timer, when timer goes up n+1, pick the highest task again
        
        # note: the sequence of num of occurence doesn't matter
        # which means that task_num (1,2,3,4,5) is the same as (5,4,3,2,1)
        # so after each round, sort the remaining task number once again
        total_time=1
        task_remain=[x for x in task_num if x>0]
        while (sum(task_remain)>0):
            task_remain.sort(reverse=True)
            timer=0
            while(timer<=n):
                if(timer<len(task_remain) and task_remain[timer]>0):
                    # if the remaining num of corresponding task is >0
                    # take it at this time
                    task_remain[timer]-=1
                if(sum(task_remain)==0):
                    break
                total_time+=1
                timer+=1
                
            task_remain[:]=[x for x in task_remain if x>0]
        
        return total_time
