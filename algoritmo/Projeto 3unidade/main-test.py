mat = [[37, 80, 92], [9, 17, 72], [90, 1, 28]]
mv = mat[0][0]
mi = mj = 0
for i in range(3):
  for j in range(3):
    if mat[i][j] < mv:
      mv = mat[i][j]
      mi = i
      mj = j
print('[', mi, mj, ']')