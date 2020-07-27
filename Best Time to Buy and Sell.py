class Solution:
    def maxProfit(A):
        if len(A)>0:        
            while True:
                max_=max(A)
                min_=min(A)
                if A.index(max(A))<A.index(min(A)):
                    if A.index(max_)>A.index(min_):
                        return max_-min_
                        break
                    elif A.index(max_)<A.index(min_):
                        A.remove(max_)
                else:
                    return  0
                    break

        else:
            return 0
print(Solution.maxProfit([2,4,1]))
