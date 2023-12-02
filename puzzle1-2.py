f = open('puzzle1input.txt', 'r')
lines = f.readlines()
calNums = []
spelledNums = {'one': '1', 'two': '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
for line in lines:
    line = line.strip()
    nums = []
    count = 0
    for i in line:
        if i.isnumeric():
            nums.append(i)
        else:
            for n in spelledNums:
                result = line.find(n, count)
                if result == count:
                    nums.append(spelledNums[n])
        count = count + 1
            
    cal = nums[0] + nums[len(nums)-1]
    calNums.append(cal)
sum = 0
for x in calNums:
    sum = sum + int(x)
print(sum)