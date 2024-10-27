from AIBrain import Player1 # type: ignore
GameBoard=[1, 2, 1, 
           2, 2, 1, 
           0, 1, 2]
AIBrainReader=0
for x in range(0, 9, 1):
    AIBrainReader=AIBrainReader+(GameBoard[x]*(3**x))
print(Player1[AIBrainReader]+1)