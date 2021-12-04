with open('day2.txt') as prompt:
  instructions = [instruction.split(" ") for instruction in prompt.read().splitlines()]

x_pos, y_pos = 0, 0

for instruction in instructions:
  if instruction[0] == "forward":
    x_pos += int(instruction[1])
  elif instruction[0] == "up":
    y_pos -= int(instruction[1])
  else:
    y_pos += int(instruction[1])

print("part 1:", x_pos * y_pos)

x_pos, y_pos, aim = 0, 0, 0

for instruction in instructions:
  if instruction[0] == "down":
    aim += int(instruction[1])
  elif instruction[0] == "up":
    aim -= int(instruction[1])
  else:
    x_pos += int(instruction[1])
    y_pos += int(instruction[1]) * aim

print("part 2:", x_pos * y_pos)