from collections import defaultdict

game_nums = [6,4,12,1,20,0,16]

played_nums = defaultdict(lambda: [])

for ind, num in enumerate(game_nums):
  played_nums[num].append(ind)

last_num = 16
for i in range(7, 30000000):
  new_num = 0
  if len(played_nums[last_num]) > 1:
    new_num = played_nums[last_num][-1] - played_nums[last_num][-2]

  last_num = new_num
  played_nums[new_num].append(i)


print(new_num)

