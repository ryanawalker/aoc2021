with open('day8.txt') as prompt:
  panels = [panel for panel in prompt.read().splitlines()]
prompt.close()

part_1_total = 0
total = 0

# just some cleanup to make iterating easier
displays = []
for panel in panels:
  split_panel = panel.split(" | ")
  displays.append([split_panel[0], split_panel[1]])

# take each line
for display in displays:
  digits = display[0].split(" ")
  output_values = display[1].split(" ")
  numbers = {}

  # now we look at all the digits in the line.
  # i'm sure there's a way to do this linearly, but it's not much slower
  # to just do it twice, lmao

  for digit in digits:
    # all the easy ones
    if len(digit) == 2:
      # this is a 1
      numbers[1] = "".join(sorted(digit))
    elif len(digit) == 3:
      # this is a 7
      numbers[7] = "".join(sorted(digit))
    elif len(digit) == 4:
      numbers[4] = "".join(sorted(digit))
    elif len(digit) == 7:
      numbers[8] = "".join(sorted(digit))
    
  for digit in digits:
    # deducing the harder ones via set differences
    if len(digit) == 6:
      if len(set(digit).difference(set(numbers[7]))) == 4:
        numbers[6] = "".join(sorted(digit))
      elif len(set(digit).difference(set(numbers[4]))) == 2:
        numbers[9] = "".join(sorted(digit))
      else:
        numbers[0] = "".join(sorted(digit))
    elif len(digit) == 5:
      if len(set(digit).difference(set(numbers[1]))) == 3:
        numbers[3] = "".join(sorted(digit))
      elif len(set(digit).difference(set(numbers[4]))) == 2:
        numbers[5] = "".join(sorted(digit))
      else:
        numbers[2] = "".join(sorted(digit))

  # invert the dictionary, just to make lookup easier
  numbers = {v: k for k, v in numbers.items()}

  # this is a stupid way to do this
  output_str = ""
  for value in output_values:
    # basically all that's left of part 1, lol
    if len(value) in [2, 3, 4, 7]:
      part_1_total += 1

    output_str += str(numbers["".join(sorted(value))])
  
  total += int(output_str)

print("part 1:", part_1_total)
print("part 2:", total)