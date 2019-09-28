_in = input()
n = _in[0]
c = _in[1]

res = []

nums = []
nums_in = input()
for num_str in nums_in.split(" "):
    nums.append(int(num_str))

# räkna antalet per siffra, spara i dictionary
amounts = {}
for num in nums:
    if not num in amounts:
        amounts[num] = 0
    amounts[num] += 1

# sortera efter val, behåll i övrigt ordningen
## hitta unika "värde-värden"
unique_amounts = sorted(list(set(list(amounts.values()))))
unique_amounts.reverse()
# print(unique_amounts)
for unique_amount in unique_amounts:
    for key in amounts:
        val = amounts[key]
        if val == unique_amount:
            for i in range(val):
                res.append(str(key))
print(" ".join(res))
