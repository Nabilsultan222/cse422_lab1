'''
https://colab.research.google.com/drive/1LC3vOjNghkZ7LAzRjI7V45Iksft9PMpo?usp=sharing
'''


#A-STAR SEARCH ALGORITHM
gr,hn ={},{}
file = open("Input file.txt","r")
l = file.readlines()
for i in l:
  x = i.split()
  hn[x[0]] = int(x[1])
  n = []
  for j in range(2, len(x), 2):
    n.append([x[j], int(x[j+1])])
  gr[x[0]] = n
file.close()

import heapq

def A_Star_Search(s, e, hn, gr):
    li = []
    heapq.heappush(li, (hn[s], 0, s))
    par = {s: None}
    vis = []
    while li != []:
      f, g, cn = heapq.heappop(li)
      if cn == e:
        path = []
        while cn is not None:
          path.append(cn)
          cn = par[cn]
        return path[::-1], g
      if cn in vis:
        continue
      vis.append(cn)

      for nc, tc in gr.get(cn, []):
        if nc not in vis:
          ng = g + tc
          nf = ng + hn.get(nc)
          heapq.heappush(li, (nf, ng, nc))
          par[nc] = cn
    return None


op = A_Star_Search(input("Start: "),input("Goal: "), hn, gr)

if op == None:
  print("NO PATH FOUND")
else:
    print(f"Path: {'-> '.join(op[0])}")
    print(f"Total distance: {op[1]} km")