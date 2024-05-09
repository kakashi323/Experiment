import heapq

def h(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, s, g):
    close, came, gscore, fscore, oheap = set(), {}, {s: 0}, {s: h(s, g)}, []

    heapq.heappush(oheap, (fscore[s], s))
    
    while oheap:
        c = heapq.heappop(oheap)[1]
        if c == g:
            d = []
            while c in came: d.append(c); c = came[c]
            return d[::-1]
        close.add(c)
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            n = c[0] + i, c[1] + j            
            t = gscore[c] + h(c, n)
            if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]) and grid[n[0]][n[1]] != 1:
                if n not in close or t < gscore.get(n, 0):
                    came[n] = c
                    gscore[n] = t
                    fscore[n] = t + h(n, g)
                    heapq.heappush(oheap, (fscore[n], n))
                
    return False

grid = [[0, 0, 0, 0, 1], [0, 1, 1, 0, 1], [0, 1, 'G', 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0]]
start, goal = (0, 0), (2, 2)
path = a_star(grid, start, goal)
print(f"Path from {start} to {goal}: {path}")