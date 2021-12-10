import statistics

with open('day10.txt') as prompt:
  lines = prompt.read().splitlines()

# part 1
# create a dict to check closers against openers
valid_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
# create a score dict to make scoring easier and more efficient later
invalid_scores = {")": 3, "]": 57, "}": 1197, ">": 25137, "": 0}

score = 0

for line in lines:
  # a space to keep track of all our openers as we see them
  openers = []
  invalid_bracket = ""

  for bracket in line:
    # if a bracket is an opener, add it to the list
    if bracket in valid_map.keys():
      openers.append(bracket)
    # if it is a closer
    if bracket in valid_map.values():
      # valid closer for last opener: pop the last opener off the list
      if bracket == valid_map[openers[-1]]:
        openers.pop(-1)
      # otherwise, mark it as invalid and break out of the line
      else:
        invalid_bracket = bracket
        break
  # look up the score for the invalid bracket and add it up
  score += invalid_scores[invalid_bracket]

print("part 1:", score)

# part 2
# basically same as above, will mark where different
autocomplete_scores = {"(": 1, "[": 2, "{": 3, "<": 4}
scores = []

for line in lines:
  openers = []
  score = 0
  invalid_bracket = ""
  for bracket in line:
    if bracket in valid_map.keys():
      openers.append(bracket)
    if bracket in valid_map.values():
      if bracket == valid_map[openers[-1]]:
        openers.pop(-1)
      else:
        invalid_bracket = bracket
        break
  # if the invalid bracket is not set, it's either a valid or incomplete line
  # valid lines will score as zero, bc openers will be empty
  # invalid lines go through their openers list in reverse, and score them up
  if invalid_bracket == "":
    for opener in openers[::-1]:
      score *= 5
      score += autocomplete_scores[opener]
    scores.append(score)

# imported from statistics bc i didn't want to write my own median logic, haha.
# to do your own, simply sort the list and then take whatever is at the middle index
print("part 2:", statistics.median(scores))