with open('day3.txt') as prompt:
  binaries = [binary for binary in prompt.read().splitlines()]

counts = [[0, 0] for digit in binaries[0]]

for binary in binaries:
  for idx in range(len(binary)):
    if binary[idx] == "0":
      counts[idx][0] += 1
    else:
      counts[idx][1] += 1

gamma_rate_list = []
epsillon_rate_list = []

for count in counts:
  if count[0] > count[1]:
    gamma_rate_list.append("0")
    epsillon_rate_list.append("1")
  else:
    gamma_rate_list.append("1")
    epsillon_rate_list.append("0")

gamma = int("".join(gamma_rate_list), 2)
epsillon = int("".join(epsillon_rate_list), 2)
print(gamma * epsillon)

o2_list = list(binaries)
co2_list = list(binaries)

for idx in range(len(binaries[0])):
  count = [0, 0]
  temp_o2_list = []
  temp_co2_list = []
  if len(o2_list) != 1:
    for binary in o2_list:
      if binary[idx] == "0":
        count[0] += 1
      else:
        count[1] += 1
    if count[0] > count[1]:
      target = "0"
    else:
      target = "1"
    for binary in o2_list:
      if binary[idx] == target:
        temp_o2_list.append(binary)
    o2_list = list(temp_o2_list)

  count = [0, 0]
  if len(co2_list) != 1:
    for binary in co2_list:
      if binary[idx] == "0":
        count[0] += 1
      else:
        count[1] += 1
    if count[0] > count[1]:
      target = "1"
    else:
      target = "0"
    for binary in co2_list:
      if binary[idx] == target:
        temp_co2_list.append(binary)
    co2_list = list(temp_co2_list)
    
print(int(o2_list[0], 2) * int(co2_list[0], 2))
    