import math

def fill_outer(w, h, reds):
    # print("#", w, h)
    # print(reds)
    reds -= 2 * w
    reds -= 2 * h
    reds -= 4
    # print(reds)
    if reds > 0:
        return fill_outer(w + 1, h + 1, browns)
    if reds == 0:
        return (w + 2, h + 2)
    if reds < 0:
        return None

_in = input().split(" ")
red = int(_in[0])
brown = int(_in[1])

# print(brown, red)

i = 1
while i < math.floor(math.sqrt(brown)) + 1:
    # print("##")
    # print(i)
    if brown % i == 0:
        # print(brown)
        brown_w = max(i, int(brown / i))
        brown_h = min(i, int(brown / i))
        # print(brown_w, brown_h)
        res = fill_outer(brown_w, brown_h, red)
        if res is not None:
            # print(res)
            print(res[0], res[1])
            break
    i += 1
