

f = open('puzzle1input.txt', 'r')
lines = f.readlines()
calNums = []
for line in lines:
    line = line.strip()
    nums = []
    for i in line:
        if i.isnumeric():
            nums.append(i)
    cal = nums[0] + nums[len(nums)-1]
    calNums.append(cal)
sum = 0
for x in calNums:
    sum = sum + int(x)
print(sum)
    