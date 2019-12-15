'''
evaluate “count“ afterwards
Runtime: 20 ms, faster than 98.92% of Python3 online submissions for Decode String.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Decode String.
'''

class Solution:
    def decodeString(self, s: str) -> str:
        if len(s)==0:
            return s
        s_lst=[]
        # count_lst=[]
        i=0
        while(i<len(s)):
            if s[i]!=']':
                s_lst.append(s[i])
            else:
                segment=''
                while(s_lst[-1]!='['):
                    segment=s_lst.pop()+segment
                # pop up the last '[' character
                s_lst.pop()
                base=1
                count=0
                # record the count of the repeating
                while(len(s_lst)>0 and '0'<=s_lst[-1] and s_lst[-1]<='9'):
                    count=count+(ord(s_lst[-1])-ord('0'))*base
                    s_lst.pop()
                    base*=10
                # repeat the segment by count times, and then push it 
                # back to the stack
                s_lst.append(segment*count)
            i+=1
        # dump out all of the elements in s_lst
        return ''.join(s_lst)
                
        
