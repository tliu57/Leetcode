from PIL import Image

im = Image.open("./test.png")
matrix = list(im.getdata())

class Solution(object):
    def numIslands(self, matrix):
        m = len(matrix)
        if m < 1:
            return 0
        n = len(matrix[0])
        
        visited = [[0 for i in range(n)] for j in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and not visited[i][j]: 
                    count += 1
                    self.bfs(matrix, i, j, visited, m, n)
                    # print (visited)
        return count

    def bfs(self, matrix, i, j, visited, m, n):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = []
        queue.append((i, j))
        while queue:
            curr_x, curr_y = queue.pop(0)
            visited[curr_x][curr_y] = 1
            for k in range(4):
                new_x = curr_x + directions[k][0]
                new_y = curr_y + directions[k][1]
                if new_x >= 0 and new_y >= 0 and new_x < m and new_y < n and matrix[new_x][new_y] != 0 and visited[new_x][new_y] == 0:
                    queue.append((new_x, new_y))

sol = Solution()
grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
print(sol.numIslands(grid))
