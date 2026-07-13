class Solution:
    def printNos(self, n):
        # Base case
        if n==0:
            return
        
        #main logic
        print(n, end=" ")
        self.printNos(n-1)
        
        