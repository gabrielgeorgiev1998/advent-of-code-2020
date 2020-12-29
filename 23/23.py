input_str = "853192647"

def get_removed_cups(string, current_cup):
  start_ind = (current_cup+1)%len(string)
  end_ind = (current_cup+4)%len(string)

  if start_ind > end_ind:
    return string[start_ind:] + string[:end_ind]
  else:
    return string[start_ind:end_ind]

def remove_cups(string, current_cup):
  start_ind = (current_cup+1)%len(string)
  end_ind = (current_cup+4)%len(string)

  if start_ind > end_ind:
    return string[end_ind:start_ind]
  else:
    return string[:start_ind] + string[end_ind:] 

def get_destination_cup(string, current_cup):
  int_dest = int(current_cup) - 1
  if int_dest == 0:
    int_dest = 9

  while 1:
    if str(int_dest) in string:
      return str(int_dest)
    int_dest = int_dest - 1
    if int_dest == 0:
      int_dest = 9

def add_removed_cups(string, removed, destination_cup):
  dest_index = string.index(destination_cup)

  return string[:dest_index+1] + removed + string[dest_index+1:]

current_cup = input_str[0]


for i in range(100):
  print(current_cup)
  removed_cups = get_removed_cups(input_str, input_str.index(current_cup))
  print(removed_cups)

  str_without_removed = remove_cups(input_str, input_str.index(current_cup))
  print(str_without_removed)
  
  destination_cup = get_destination_cup(str_without_removed, current_cup)
  print(destination_cup)

  input_str = add_removed_cups(str_without_removed, removed_cups, destination_cup)
  print(input_str)

  current_cup = input_str[(input_str.index(current_cup)+1)%len(input_str)]

