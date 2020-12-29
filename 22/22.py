input_str = """Player 1:
38
1
28
32
43
21
42
29
18
13
39
41
49
31
19
26
27
40
35
14
3
36
12
16
45

Player 2:
34
15
47
20
23
2
11
9
8
7
25
50
48
24
46
44
10
6
22
5
33
30
4
17
37"""

def process(input_str):
  player_decks = list(map((lambda x: list(map(int, x.splitlines()[1:]))), input_str.split("\n\n")))

  return player_decks

def score(deck):
  score = 0
  for i, card in enumerate(reversed(deck)):
    score += (i+1) * card
  return score

def rec_combat(deck1, deck2, game_depth):
  game_history = []

  while len(deck1) != 0 and len(deck2) != 0:
    if (deck1 in game_history) and (deck2 in game_history):
      print("test", game_depth)
      return (score(deck1), 0)
    
    game_history.append(deck1.copy())
    game_history.append(deck2.copy())

    card1 = deck1.pop(0)
    card2 = deck2.pop(0)

    if (len(deck1) >= card1 and len(deck2) >= card2):
      subgame_scores = rec_combat(deck1[:card1], deck2[:card2], game_depth+1)
      if subgame_scores[0] == 0:
        deck2.append(card2)
        deck2.append(card1)
      else:
        deck1.append(card1)
        deck1.append(card2)
    else:
      if card1 > card2:
        deck1.append(card1)
        deck1.append(card2)
      else:
        deck2.append(card2)
        deck2.append(card1)
    
  return (score(deck1), score(deck2))

player1_deck, player2_deck = process(input_str)

'''
while len(player1_deck) != 0 and len(player2_deck) != 0:
  p1_card = player1_deck.pop(0)
  p2_card = player2_deck.pop(0)

  if p1_card > p2_card:
    player1_deck.append(p1_card)
    player1_deck.append(p2_card)
  else:
    player2_deck.append(p2_card)
    player2_deck.append(p1_card)


print(score(player1_deck))
print(score(player2_deck))
'''

print(rec_combat(player1_deck, player2_deck, 0))