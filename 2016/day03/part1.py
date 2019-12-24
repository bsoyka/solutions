import re
with open("input.txt") as f:
    triangles = [list(map(int, re.findall(r"\d+", line.strip()))) for line in f]
valid = 0
for triangle in triangles:
    if not triangle[0] + triangle[1] > triangle[2]:
        continue
    if not triangle[1] + triangle[2] > triangle[0]:
        continue
    if not triangle[0] + triangle[2] > triangle[1]:
        continue
    valid += 1
print(valid)