def run_game(draws, boards):
  for draw in draws:
    for board in boards:
      for line in board:
        for num in line:
          if num[0] == draw:
            num[1] = 1
            if check_board(board):
              return(sum_board(board) * draw)

def check_board(board):

  for line in board:
    bingo = True
    for num in line:
      if num[1] == 0:
        bingo = False
    if bingo:
      return bingo

  for col_idx in range(len(board[0])):
    bingo = True
    for line in board:
      if line[col_idx][1] == 0:
        bingo = False
    if bingo:
      return bingo
  
  return bingo

def sum_board(board):
  score = 0
  for line in board:
    for num in line:
      if num[1] == 0:
        score += num[0]
  return score

def run_game_2(draws, boards):
  winning_boards = []
  for draw in draws:
    for board in boards:
      if board not in winning_boards:
        for line in board:
          for num in line:
            if num[0] == draw:
              num[1] = 1
              if check_board(board):
                if len(winning_boards) == len(boards) - 1:
                  return(sum_board(board) * draw)
                winning_boards.append(board)

with open('day4.txt') as prompt:
  instructions = list(prompt)

draws = list(map(int, instructions[0].rstrip().split(",")))
boards = []
board = []
for idx in range(2, len(instructions)):
  if instructions[idx] == "\n":
    boards.append(board)
    board = []
  else:
    board.append([[int(num), 0] for num in instructions[idx].lstrip().rstrip().split(" ") if num])

boards_2 = [[[[num for num in nums] for nums in line] for line in board] for board in boards]
print(run_game(draws, boards))
print(run_game_2(draws, boards_2))