n = int(input())
p = list(map(int, input().split()))

parent = [0]*(n+1)

for i in range(2, n+1):
    parent[i] = p[i-2]

path = []
current = n


while current != 0:
    path.append(current)
    current = parent[current]
path.reverse()
print(*path)



