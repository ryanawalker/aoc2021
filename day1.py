with open('day1.txt') as prompt:
  depths = [int(depth) for depth in prompt.read().splitlines()]

inc_count = 0

for idx in range(1, len(depths)):
  if depths[idx] > depths[idx - 1]:
    inc_count += 1

print("part 1:", inc_count)

inc_count = 0

for idx in range(3, len(depths)):
  window_1 = sum(depths[idx - 3:idx])
  window_2 = sum(depths[idx - 2:idx + 1])
  if window_2 > window_1:
    inc_count += 1

print("part 2:", inc_count)