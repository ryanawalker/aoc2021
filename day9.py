with open('day9.txt') as prompt:
  heights = [[int(point) for point in depth] for depth in prompt.read().splitlines()]

height = len(heights)
width = len(heights[0])

# part 1
risk_total = 0

for x in range(height):
  for y in range(width):
    point = heights[x][y]
    adjacents = []
    if x > 0:
      adjacents.append(heights[x - 1][y])
    if y > 0:
      adjacents.append(heights[x][y - 1])
    if x < height - 1:
      adjacents.append(heights[x + 1][y])
    if y < width - 1:
      adjacents.append(heights[x][y + 1])
    
    if point < min(adjacents):
      risk_total += point + 1
    
print("part 1:", risk_total)

# part 2
deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)] # will be useful later
basins = []

def recursive_flood(x, y):
  # if this is flooded already, it is already counted or its a border
  if heights[x][y] == 9:
    return 0
  # otherwise, flood it and score it
  score = 1
  heights[x][y] = 9

  # then keep looking around at adjacents
  for delta in deltas:
    # find new coord to look at
    x_delta = x + delta[0]
    y_delta = y + delta[1]

    # make sure we're in-bounds and then keep flooding
    if x_delta >= 0 and x_delta < height and y_delta >= 0 and y_delta < width:
      score += recursive_flood(x_delta, y_delta)

  return score

for x in range(height):
  for y in range(width):
    basins.append(recursive_flood(x, y))

sorted_sizes = sorted(basins)

print("part 2", sorted_sizes[-1] * sorted_sizes[-2] * sorted_sizes[-3])
