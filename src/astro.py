import math
import sys

h = 0
m = 1

start_1 = input().split(":")
start_2 = input().split(":")
int_1 = input().split(":")
int_2 = input().split(":")

start_1[h] = int(start_1[h])
start_1[m] = int(start_1[m])
start_2[h] = int(start_2[h])
start_2[m] = int(start_2[m])
int_1[h] = int(int_1[h])
int_1[m] = int(int_1[m])
int_2[h] = int(int_2[h])
int_2[m] = int(int_2[m])

st1_hours = [start_1[h]]
st1_minutes = [start_1[m]]
while True:
    st1_hours.append(st1_hours[-1] + int_1[h])
    st1_minutes.append(st1_minutes[-1] + int_1[m])
    if st1_minutes[-1] >= 60 :
        st1_minutes[-1] -= 60
        st1_hours[-1] += 1
    if st1_hours[-1] % 24 == st1_hours[0] % 24 and \
            st1_minutes[-1] == st1_minutes[0] :
        break

st2_hours = [start_2[h]]
st2_minutes = [start_2[m]]

while True:
    st2_hours.append(st2_hours[-1] + int_2[h])
    st2_minutes.append(st2_minutes[-1] + int_2[m])
    if st2_minutes[-1] >= 60 :
        st2_minutes[-1] -= 60
        st2_hours[-1] += 1
    if st2_hours[-1] % 24 == st2_hours[0] % 24 and \
            st2_minutes[-1] == st2_minutes[0] :
        break

def lcd(a, b):
    return abs(a*b) // math.gcd(a, b)

longest = lcd(lcd(lcd(len(st1_hours), len(st2_hours)), len(st1_minutes)), len(st2_minutes))

new_list = st1_minutes.copy()
while len(st1_minutes) < longest:
    for val in new_list:
        st1_minutes.append(val)

new_list = st2_minutes.copy()
while len(st2_minutes) < longest:
    for val in new_list:
        st2_minutes.append(val)

repeats = 0
last_hour = st1_hours[-1]
new_list = st1_hours.copy()
while len(st1_hours) < longest:
    repeats += 1
    for val in new_list:
        # print(val, last_hour, repeats)
        st1_hours.append(val + (last_hour * repeats))

repeats = 0
last_hour = st2_hours[-1]
new_list = st2_hours.copy()
while len(st2_hours) < longest:
    repeats += 1
    for val in new_list:
        st2_hours.append(val + (last_hour * repeats))

days = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

for hour_1 in st1_hours:
    for hour_2 in st2_hours:
        if hour_2 % 168 > hour_1 % 168:
            break
        if hour_1 % 168 == hour_2 % 168:
            if st1_minutes[st1_hours.index(hour_1)] == st2_minutes[st2_hours.index(hour_2)]:
                print(days[(hour_1 // 24) % 7])
                print("{:02d}:{:02d}".format(hour_1 % 24, st1_minutes[st1_hours.index(hour_1)]))
                sys.exit()

print("Never")
