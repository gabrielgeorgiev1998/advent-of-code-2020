input_str = """12578151
5051300"""

num1, num2 = list(map(int, input_str.splitlines()))

def get_loopsize(num):
  loopsize = 0
  value = 1
  while 1:
    loopsize += 1
    value *= 7
    value %= 20201227
    if value == num:
      return loopsize

def apply(num, loopsize):
  value = 1
  for i in range(loopsize):
    value *= num
    value %= 20201227

  return value

print(apply(num1, get_loopsize(num2)))

