# DIGITS COUNT

nums = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
        '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

a = input()
b = input()

for i in range(int(a), int(b)+1):
    for digit in str(i):
        nums[digit] += 1

ans = ''

for num in nums.values():
    ans += str(num) + ' '

print(ans)
