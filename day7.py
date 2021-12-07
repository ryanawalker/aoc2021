with open('day7.txt') as prompt:
  crabs = [int(position) for position in prompt.read().split(",")]
prompt.close()

costs = {}

for i in range(min(crabs), max(crabs) + 1):
  cost = 0
  for crab in crabs:
    cost += abs(i - crab)
  costs[i] = cost

print(min(costs.values()))

costs = {}

for i in range(min(crabs), max(crabs) + 1):
  cost = 0
  for crab in crabs:
    steps = abs(i - crab)
    cost += sum(range(1, steps + 1))
  costs[i] = cost

print(min(costs.values()))
