

def maximumMinutes(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    fire_dic = {}
    # player_dic = {}

    def displayGrid():
        for i in range(m):
            print(grid[i])   

    def displayDictionary(dic):
        for i in range(m):
            line = ''
            for j in range(n):
                if (i,j) in dic:
                    line += str(dic[(i,j)]) + ' '
                else:
                    line += 'X '
            print(line)
    
    def calcFireSpreadMatrix(fire_pos, dic):
        visited = [fire_pos]
        dic[fire_pos] = 0
        start = 0
        while start < len(visited):
            current_pos = visited[start]
            new_positions = [(current_pos[0] - 1, current_pos[1]), (current_pos[0] + 1, current_pos[1]),
                             (current_pos[0], current_pos[1] + 1), (current_pos[0], current_pos[1] - 1)]
            for pos in new_positions:
                if pos[0] < m and pos[0] >= 0 and pos[1] < n and pos[1] >= 0 and grid[pos[0]][pos[1]] != 2:
                    if pos in dic:
                        if dic[pos] > dic[current_pos] + 1:
                            dic[pos] = dic[current_pos] + 1
                            visited.append(pos)
                    else:
                        dic[pos] = dic[current_pos] + 1
                        visited.append(pos)
            start += 1

    def canReach(f_dic, wait_time) -> bool:
        p_dic = {}
        visited = [(0,0)]
        p_dic[(0,0)] = wait_time
        start = 0
        while start < len(visited):
            current_pos = visited[start]
            new_positions = [(current_pos[0] - 1, current_pos[1]), (current_pos[0] + 1, current_pos[1]),
                             (current_pos[0], current_pos[1] + 1), (current_pos[0], current_pos[1] - 1)]
            for pos in new_positions:
                if pos[0] == (m-1) and pos[1] == (n-1):
                        return True
                if pos[0] < m and pos[0] >= 0 and pos[1] < n and pos[1] >= 0 and grid[pos[0]][pos[1]] == 0 and (pos not in f_dic or f_dic[pos] - p_dic[current_pos] >= 2):
                    
                    if pos in p_dic:
                        if p_dic[pos] > p_dic[current_pos] + 1:
                            p_dic[pos] = p_dic[current_pos] + 1
                            visited.append(pos)
                    else:
                        p_dic[pos] = p_dic[current_pos] + 1
                        visited.append(pos)
            start += 1
        return False
    
    def calcWaitTime(max):
        # 100 False
        # 50 True
        # 75 False
        # 63 True
        # 69 False
        top = max
        bottom = 0
        answer = -1
        while top - bottom > 1:
            val = int(bottom + (top-bottom)/2)
            if canReach(fire_dic, val):
                answer = val
                bottom = val
            else:
                top = val
        return answer
                


    def populateDic(dic, val):
        for i in range(m):
            for j in range(n):
                if grid[i][j] == val:
                    calcFireSpreadMatrix((i,j), dic)


    populateDic(fire_dic, 1)
    # displayGrid()
    # print()
    # displayDictionary(fire_dic)
    if not canReach(fire_dic, 0):
        return -1
    if canReach(fire_dic, 1000000000):
        return 1000000000
    return(calcWaitTime(n*m))

grid = [[0,2,0,0,1],[0,2,0,2,2],[0,2,0,0,0],[0,0,2,2,0],[0,0,0,0,0]]

# grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
# grid = [[0,0,0],[2,2,0],[1,2,0]]
# grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
print(maximumMinutes(grid))