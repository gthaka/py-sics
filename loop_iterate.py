nums = [1, 2, 3, 4, 5]


def divider():
    print("--------------------------")


# loop & print all
for num in nums:
    print(num)

divider()

# break and continue keywords
for num in nums:
    if num == 3:
        print("Found!")
        break
    print(num)

divider()

# continue - ignore a value but not break out of the loop
for num in nums:
    if num == 3:
        print("Found!")
        continue
    print(num)

divider()

# nested loops
for num in nums:
    for letter in "abc":
        print(num, letter)

divider()

#
for i in range(1, 11):  # 1 to and not including 11 (1-10)
    print(i)

divider()

# while loops
x = 0

while x < 10:
    print(x)
    x += 1

divider()

y = 0
while True:  # infinite loop until condition is met
    if y == 5:  # the condition
        break
    print(y)
    y += 1
