class Solution(object):
    def properties(self,board,word):
        row,col=4,4
        path=set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=row or c>=col or (r,c) in path or word[i]!=board[r][c]:
                return False
            path.add((r,c))
            result=(dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1)or dfs(r,c-1,i+1))
            path.remove((r,c))
            return result
        for  r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False

board=[['a','c','d','e'],['f','h','j','i'],['l','m','o','n'],['p','q','r','s','t']]

x=Solution()
x.properties(board,"anish")