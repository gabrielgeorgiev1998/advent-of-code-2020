input_str = "853192647"

class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

value_to_node = {}

first_node = None
prev_node = None
for i in range(1, 1000001):
  if i < 10:
    value = int(input_str[i-1])
    node = Node(value)
    value_to_node[value] = node
    if prev_node != None:
      prev_node.next = node
    prev_node = node

    if first_node == None:
      first_node = node
  else:
    value = i
    node = Node(value)
    value_to_node[value] = node
    prev_node.next = node
    prev_node = node

node.next = first_node

curr_node = first_node

for i in range(10000000):
  curr_cup = curr_node.value

  removed = curr_node.next

  removed_values = [removed.value, removed.next.value, removed.next.next.value]

  curr_node.next = removed.next.next.next

  dest_cup = curr_cup - 1
  while 1:
    if dest_cup == 0:
      dest_cup = 1000000
    if dest_cup in removed_values:
      dest_cup -= 1
      continue
    break

  dest_node = value_to_node[dest_cup]

  dest_next = dest_node.next
  dest_node.next = removed
  removed.next.next.next = dest_next

  curr_node = curr_node.next

cup_1 = value_to_node[1]

print(cup_1.next.value * cup_1.next.next.value)