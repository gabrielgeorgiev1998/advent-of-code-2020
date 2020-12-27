input_str = """1006401
17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,449,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,x,x,607,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29"""

lines = input_str.splitlines()

erl_tmstp  = int(lines[0])

bus_ids = []
for el in lines[1].split(","):
  try:
    bus_ids.append(int(el))
  except:
    pass

print(erl_tmstp)
print(bus_ids)

earliest_bus_id = 0
time_to_wait = 1000000000

for bus_id in bus_ids:
  multiple = 0
  while multiple <= erl_tmstp:
    multiple += bus_id
  
  curr_time_to_wait = multiple - erl_tmstp

  if(curr_time_to_wait < time_to_wait):
    time_to_wait = curr_time_to_wait
    earliest_bus_id = bus_id

print(time_to_wait * earliest_bus_id)