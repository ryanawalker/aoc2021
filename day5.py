def part_1(lines):
  vent_map = {}
  for line in lines:
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]

    if x1 == x2:
      # vertical
      for y in range(min(y1, y2), max(y1, y2) + 1):
        # find smallest y and plot points towards biggest y along x
        if (x1, y) in vent_map:
          vent_map[(x1, y)] += 1
        else:
          vent_map[(x1, y)] = 1
    elif y1 == y2:
      # horizontal
      for x in range(min(x1, x2), max(x1, x2) + 1):
        # find smallest x and plot points towards biggest x along y
        if (x, y1) in vent_map:
          vent_map[(x, y1)] += 1
        else:
          vent_map[(x, y1)] = 1
  
  total = 0

  for point in vent_map:
    if vent_map[point] >= 2:
      total += 1
  return total

def part_2(lines):
  vent_map = {}
  for line in lines:
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]

    if x1 == x2:
      # vertical
      for y in range(min(y1, y2), max(y1, y2) + 1):
        # find smallest y and plot points towards biggest y along x
        if (x1, y) in vent_map:
          vent_map[(x1, y)] += 1
        else:
          vent_map[(x1, y)] = 1
    elif y1 == y2:
      # horizontal
      for x in range(min(x1, x2), max(x1, x2) + 1):
        # find smallest x and plot points towards biggest x along y
        if (x, y1) in vent_map:
          vent_map[(x, y1)] += 1
        else:
          vent_map[(x, y1)] = 1
    else:
      # had to think really hard about this, but all diagonals boil down to essentially one case
      # we just need to figure out whether to count down or up for each axis
      # e.g. if we're doing 9,9 to 7,7 or 9,7 to 7,9, we still want to plot 9, 8, 7 for the x values, regardless of y value
      # vice versa if x1 is smaller
      # same holds true for y values
      # in 9,9 to 7,7 we want to plot 9, 8, 7 for y values
      # in 9,7 to 7,9 we want to do the opposite, 7, 8, 9

      # if x1 is bigger, we count down x
      if x1 > x2:
        x_inc = -1
      else:
        x_inc = 1
      # if y1 is bigger, we count down y
      if y1 > y2:
        y_inc = -1
      else:
        y_inc = 1
      
      # this is a little messy, but we're zipping together the two ranges of x1 to x2 and y1 to y2 (with appropriate incrementers) and plotting those points
      for x, y in zip(range(x1, x2 + x_inc, x_inc), range(y1, y2 + y_inc, y_inc)):
        if (x, y) in vent_map:
          vent_map[(x, y)] += 1
        else:
          vent_map[(x, y)] = 1
  
  total = 0

  for point in vent_map:
    if vent_map[point] >= 2:
      total += 1
  return total
 
with open('day5.txt') as prompt:
  lines = [line.split(" -> ") for line in prompt.read().splitlines()]

# clean this input. gotta be a better way for this but this works.
end_points = []
temp_point = []
for line in lines:
  temp_point = []
  for point in line:
    split_point = point.split(",")
    temp_point.append([int(split_point[0]), int(split_point[1])])
  end_points.append(temp_point) 

# run it!
print(part_1(end_points))
print(part_2(end_points))