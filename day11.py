# part 1
with open('day11.txt') as prompt:
  octopus_garden = [[[int(energy), False] for energy in line] for line in prompt.read().splitlines()]
prompt.close()

# keeping track of flashes
flashes = 0

# run 100 times
for i in range(100):
  # increase everyone by one
  for line in octopus_garden:
    for octopus in line:
      octopus[0] += 1

  # assume a flash will occur
  flashed = True

  # while flashes are occuring
  while flashed == True:
    # reset validation
    flashed = False

    # for each octopus
    for row, line in enumerate(octopus_garden):
      for col, octopus in enumerate(line):
        # if the octopus is over 9, flash it.
        if octopus[0] > 9 and octopus[1] == False:
          octopus[1] = True
          flashed = True
          flashes += 1
          # collect neighbors
          neighbors = []
          if row > 0:
            neighbors.append(octopus_garden[row - 1][col])
            if col > 0:
              neighbors.append(octopus_garden[row - 1][col - 1])
            if col < 9:
              neighbors.append(octopus_garden[row - 1][col + 1])
          if row < 9:
            neighbors.append(octopus_garden[row + 1][col])
            if col > 0:
              neighbors.append(octopus_garden[row + 1][col - 1])
            if col < 9:
              neighbors.append(octopus_garden[row + 1][col + 1])
          if col > 0:
            neighbors.append(octopus_garden[row][col - 1])
          if col < 9:
            neighbors.append(octopus_garden[row][col + 1])
          
          # go to each neighbor, increase their energy level by 1
          for neighbor in neighbors:
            if neighbor[1] == False:
              neighbor[0] += 1

  # reset the flashes and energy levels
  for line in octopus_garden:
    for octopus in line:
      if octopus[1] == True:
        octopus[0] = 0
        octopus[1] = False

print("part 1:", flashes)

# part 2
# almost entirely the same, will note where different
with open('day11.txt') as prompt:
  octopus_garden = [[[int(energy), False] for energy in line] for line in prompt.read().splitlines()]
prompt.close()

# set a flag for whether we've synched and a count for what step we're on
synched = False
step = 0

while not synched:
  step += 1
  for line in octopus_garden:
    for octopus in line:
      octopus[0] += 1

  flashed = True

  while flashed == True:
    flashed = False

    for row, line in enumerate(octopus_garden):
      for col, octopus in enumerate(line):
        if octopus[0] > 9 and octopus[1] == False:
          octopus[1] = True
          flashed = True
          neighbors = []
          if row > 0:
            neighbors.append(octopus_garden[row - 1][col])
            if col > 0:
              neighbors.append(octopus_garden[row - 1][col - 1])
            if col < 9:
              neighbors.append(octopus_garden[row - 1][col + 1])
          if row < 9:
            neighbors.append(octopus_garden[row + 1][col])
            if col > 0:
              neighbors.append(octopus_garden[row + 1][col - 1])
            if col < 9:
              neighbors.append(octopus_garden[row + 1][col + 1])
          if col > 0:
            neighbors.append(octopus_garden[row][col - 1])
          if col < 9:
            neighbors.append(octopus_garden[row][col + 1])
          
          for neighbor in neighbors:
            if neighbor[1] == False:
              neighbor[0] += 1
  
  # a counter for how many flashed this step
  flashed_this_step = 0

  for line in octopus_garden:
    for octopus in line:
      if octopus[1] == True:
        octopus[0] = 0
        octopus[1] = False
        # increase counter
        flashed_this_step += 1

  # if we got 100 flashes, we know we're synched!
  if flashed_this_step == 100:
    synched = True

print("part 2:", step)
