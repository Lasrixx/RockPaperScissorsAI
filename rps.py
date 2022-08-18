# Predicts next move based on combination of previous plays

combos = {}

def player(prev_play, opponent_history=[]):
  
  n = 3

  # Use a default guess for the first rounds of the game
  # Where there is not enough data to go on to generate a proper       # guess
  guess = "R"
  
  if prev_play != '':
    opponent_history.append(prev_play)

  if len(opponent_history) > n:

    # Need to update combos with the tally of how many times it has       been used by the opponent  
    # This way we can predict what they are likely to use again
    prev_combo = "".join(opponent_history[-(n+1):])
    if prev_combo in combos:
      combos[prev_combo]+=1
    else:
      combos[prev_combo]=1

    # Based on what combo they currently have built up, they can           either add an R, P, or S to it 
    curr_combo = "".join(opponent_history[-n:])
    potential_combos = [curr_combo+"R",curr_combo+"P",curr_combo+"S"]

    for combo in potential_combos:
      if not combo in combos:
        combos[combo] = 0

    # So we can use previous combos to predict out of which                potential combo they will use
    predict = max(potential_combos, key=lambda key: combos[key])[-1]

    # Use prediction of opponent's move to select our move
    if predict == "P":
      guess = "S"
    if predict == "R":
      guess = "P"
    if predict == "S":
      guess = "R"

  return guess
