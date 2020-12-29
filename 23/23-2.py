input_str = "853192647"

import numpy as np

def get_final_result(nums):
  num1 = nums[int((np.where(nums==1)+1)[0])%len(nums)]  
  num2 = nums[int((np.where(nums==1)+2)[0])%len(nums)]  

  return num1*num2


def construct_full_start_state(string):
  input_nums = list(map(int, input_str))

  for i in range(10, 1000001):
    input_nums.append(i)
  
  return np.array(input_nums)

def get_removed_cups(nums, current_cup):
  start_ind = (current_cup + 1)%len(nums)
  end_ind = (current_cup + 4)%len(nums)

  if start_ind > end_ind:
    return np.concatenate(nums[start_ind:], nums[:end_ind])
  else:
    return nums[start_ind:end_ind]

def remove_cups(nums, current_cup):
  start_ind = (current_cup + 1)%len(nums)
  end_ind = (current_cup + 4)%len(nums)

  if start_ind > end_ind:
    return nums[end_ind:start_ind]
  else:
    return np.concatenate((nums[:start_ind], nums[end_ind:]))

def get_destination_cup(nums, current_cup):
  dest_cup = nums[current_cup] - 1
  if dest_cup == 0:
    dest_cup = 1000000

  while 1:
    if dest_cup in nums:
      return int(np.where(nums==dest_cup)[0])
    dest_cup -= 1
    if dest_cup == 0:
      dest_cup = 1000000

def add_removed_cups(nums, removed, destination_cup):
  return np.concatenate((nums[:destination_cup+1], removed, nums[destination_cup+1:]))


nums = construct_full_start_state(input_str)
current_cup = 0
current_cup_label = nums[current_cup]
for i in range(10000000):
  removed_cups = get_removed_cups(nums, current_cup)

  cups_after_removal = remove_cups(nums, current_cup)

  destination_cup = get_destination_cup(cups_after_removal, current_cup)

  nums = add_removed_cups(cups_after_removal, removed_cups, destination_cup)
  
  current_cup = (int(np.where(nums==current_cup_label)[0]) + 1)%len(nums)
  current_cup_label = nums[current_cup]


get_final_result(nums)