import sys

def rec(num, i):
    print(num, i)
    if len(str(num)) == num:
        return i + 1
    return rec(len(str(num)), i + 1)

res = []
while True:
    _in = input()
    if _in == "END":
        break
    res.append(rec(_in, 0))

for num in res:
    print(num)
