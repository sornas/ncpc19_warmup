blimps = []
blimps.append(input())
blimps.append(input())
blimps.append(input())
blimps.append(input())
blimps.append(input())

nums = []

for i in range(5):
    if "FBI" in blimps[i]:
        nums.append(str(i + 1))
if len(nums) > 0:
    print(" ".join(nums))
else:
    print("HE GOT AWAY!")

