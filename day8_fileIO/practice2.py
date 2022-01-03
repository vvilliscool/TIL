f1=open('list_num.txt', 'r')
f2=open('result_num.txt', 'w')

line = None    # 변수 line을 None으로 초기화

while True:
    line = f1.readline()
    if not line:
        break
    nums = line.strip('\n')
    nums = nums.split(' ')
    if '' in nums:
        continue
    f2.write(f'{nums[0]} + {nums[1]} = {float(nums[0])+float(nums[1])}\n')

f1.close()
f2.close()
