# part 1, brute force, no explanation needed
with open('day6.txt') as prompt:
  lanterns = [int(lantern) for lantern in prompt.read().split(",")]
prompt.close()

for day in range(80):
  new_fish = []
  for idx in range(len(lanterns)):
    if lanterns[idx] == 0:
      new_fish.append(8)
      lanterns[idx] = 7
    lanterns[idx] -= 1
  lanterns += new_fish

print(len(lanterns))

# part 2, more efficiency needed
with open('day6.txt') as prompt:
  lanterns = [int(lantern) for lantern in prompt.read().split(",")]
prompt.close()

# instead of tracking each fish individually
# we're now going to track the total number of each fish at each of the current life stages

fish_per_life_stage = { 0:0, 1:0,2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0 }

# populate dictionary
for stage in lanterns:
  fish_per_life_stage[stage] += 1

# for each day
for day in range(256):
  # create the ledger for tomorrow
  new_fish_per_life_stage = { 0:0, 1:0,2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0 }
  
  # check each life stage.
  for stage, count in fish_per_life_stage.items():
    # for stage 0, we create an equal number of stage 8s and 6s
    if stage == 0:
      new_fish_per_life_stage[8] += count
      new_fish_per_life_stage[6] += count
    
    # otherwise, we just level age them up to the next stage
    else:
      new_fish_per_life_stage[stage - 1] += count
  
  # at the end of the day, replace our ledger
  fish_per_life_stage = new_fish_per_life_stage

print(sum(fish_per_life_stage.values()))