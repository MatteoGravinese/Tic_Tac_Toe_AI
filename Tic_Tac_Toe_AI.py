import time

Player1=[]
Player2=[]
GameBoard=[]
Player1UpdateLog=[]
Player2UpdateLog=[]
TurnNumber=0
LookHereInAIBrain=0
PlayerGoesHere=0
UpdateLogPlace=0
PlayerGoesHereChanger=1
Player2Resetter=0
GameOverTracker=0
TotalGamesPlayed=0
gol=[]    


def onewins():
  global UpdateLogPlace, Player2Resetter, GameOverTracker, TurnNumber
  while Player2[Player2UpdateLog[UpdateLogPlace]]==8:
    Player2[Player2UpdateLog[UpdateLogPlace]]=0
    UpdateLogPlace=UpdateLogPlace+1
  if UpdateLogPlace==len(Player2UpdateLog):
    Player2Resetter=1
    UpdateLogPlace=0
    Player2[Player2UpdateLog[0]]=0
  Player2[Player2UpdateLog[UpdateLogPlace]]=Player2[Player2UpdateLog[UpdateLogPlace]]+1
  GameOverTracker=1
  TurnNumber=10


def twowins():
  global UpdateLogPlace, TurnNumber, GameOverTracker
  while Player1[Player1UpdateLog[UpdateLogPlace]]==8:
    Player1[Player1UpdateLog[UpdateLogPlace]]=0
    UpdateLogPlace=UpdateLogPlace+1
  Player1[Player1UpdateLog[UpdateLogPlace]]=Player1[Player1UpdateLog[UpdateLogPlace]]+1
  GameOverTracker=1        
  TurnNumber=10


for a in range(0, 3**10, 1):
    Player1.append(0)
for a in range(0, 3**10, 1):
    Player2.append(0)
while TotalGamesPlayed<20000:
  GameBoard=[]
  for b in range(0, 9, 1):
    GameBoard.append(0)
  while TurnNumber<5:
    LookHereInAIBrain=0
    for d in range(0, 9, 1):
      LookHereInAIBrain=LookHereInAIBrain+(GameBoard[d]*(3**d))
    Player1UpdateLog.insert(0, LookHereInAIBrain)
    PlayerGoesHere=Player1[LookHereInAIBrain]
    if GameBoard[PlayerGoesHere]==0:
      GameBoard[PlayerGoesHere]=1
    else:
      while PlayerGoesHere+PlayerGoesHereChanger<9:
        if GameBoard[PlayerGoesHereChanger+PlayerGoesHere]==0:
          Player1[Player1UpdateLog[UpdateLogPlace]]=PlayerGoesHereChanger+PlayerGoesHere
          PlayerGoesHereChanger=9
        PlayerGoesHereChanger=PlayerGoesHereChanger+1
      if PlayerGoesHereChanger+PlayerGoesHere==9:
        Player1[Player1UpdateLog[UpdateLogPlace]]=0
        PlayerGoesHereChanger=1
        UpdateLogPlace=UpdateLogPlace+1
        while Player1[Player1UpdateLog[UpdateLogPlace]]==8:
          Player1[Player1UpdateLog[UpdateLogPlace]]=0
          UpdateLogPlace=UpdateLogPlace+1
        Player1[Player1UpdateLog[UpdateLogPlace]]=Player1[Player1UpdateLog[UpdateLogPlace]]+1
      UpdateLogPlace=0
      GameOverTracker=1
      TurnNumber=10
    if GameOverTracker==0:
      for g in range(0, 7, 3):
        if GameBoard[g]==GameBoard[g+1]==GameBoard[g+2]==1:
          onewins()
    if GameOverTracker==0:
      for h in range(0, 3, 1):
        if GameBoard[h]==GameBoard[h+3]==GameBoard[h+6]==1:
          onewins()
    if GameOverTracker==0:
      if GameBoard[0]==GameBoard[4]==GameBoard[8]==1:
        onewins()
    if GameOverTracker==0:
      if GameBoard[2]==GameBoard[4]==GameBoard[6]==1:
        onewins()
    UpdateLogPlace=0
    LookHereInAIBrain=0
    if GameOverTracker==0 and TurnNumber!=4:
      for d in range(0, 9, 1):
        LookHereInAIBrain=LookHereInAIBrain+(GameBoard[d]*(3**d))
      Player2UpdateLog.insert(0, LookHereInAIBrain)
      PlayerGoesHere=Player2[LookHereInAIBrain]
      if GameBoard[PlayerGoesHere]==0:
        GameBoard[PlayerGoesHere]=2
      else:
        while PlayerGoesHere+PlayerGoesHereChanger<9:
          if GameBoard[PlayerGoesHereChanger+PlayerGoesHere]==0:
            Player2[Player2UpdateLog[UpdateLogPlace]]=PlayerGoesHereChanger+PlayerGoesHere
            PlayerGoesHereChanger=9
          PlayerGoesHereChanger=PlayerGoesHereChanger+1
        if PlayerGoesHereChanger+PlayerGoesHere==9:
          Player2[Player2UpdateLog[UpdateLogPlace]]=0
          PlayerGoesHereChanger=1
          UpdateLogPlace=UpdateLogPlace+1
          while Player2[Player2UpdateLog[UpdateLogPlace]]==8:
            Player2[Player2UpdateLog[UpdateLogPlace]]=0
            UpdateLogPlace=UpdateLogPlace+1
            if UpdateLogPlace==len(Player2UpdateLog):
              Player2Resetter=1
              UpdateLogPlace=0
              Player2[Player2UpdateLog[0]]=0
          Player2[Player2UpdateLog[UpdateLogPlace]]=Player2[Player2UpdateLog[UpdateLogPlace]]+1
        PlayerGoesHereChanger=1
        GameOverTracker=1
        TurnNumber=10
      UpdateLogPlace=0
      if GameOverTracker==0:
        for g in range(0, 7, 3):
          if GameBoard[g]==GameBoard[g+1]==GameBoard[g+2]==2:
            twowins()
      if GameOverTracker==0:
        for h in range(0, 3, 1):
          if GameBoard[h]==GameBoard[h+3]==GameBoard[h+6]==2:
            twowins()
      if GameOverTracker==0:
        if GameBoard[0]==GameBoard[4]==GameBoard[8]==2:
          twowins()
      if GameOverTracker==0:
        if GameBoard[2]==GameBoard[4]==GameBoard[6]==2:
          twowins()
    if GameOverTracker==0 and TurnNumber==4:
      while Player2[Player2UpdateLog[UpdateLogPlace]]==8:
        Player2[Player2UpdateLog[UpdateLogPlace]]=0
        UpdateLogPlace=UpdateLogPlace+1
        if UpdateLogPlace==len(Player2UpdateLog):
          Player2Resetter=1
          UpdateLogPlace=0
          Player2[Player2UpdateLog[0]]=0
      Player2[Player2UpdateLog[UpdateLogPlace]]=Player2[Player2UpdateLog[UpdateLogPlace]]+1
    GameOverTracker=0
    TurnNumber=TurnNumber+1
  TurnNumber=0
  Player1UpdateLog=[]
  Player2UpdateLog=[]
  PlayerGoesHereChanger=1
  UpdateLogPlace=0
  if Player2Resetter==1:
    Player2=[]
    for a in range(0, 3**10, 1):
      Player2.append(0)
  Player2Resetter=0
  LookHereInAIBrain=0
  TotalGamesPlayed=TotalGamesPlayed+1
  if TotalGamesPlayed<8:
    time.sleep(0.7)
    for x in range(0, 3, 1):
      gol=[]
      for xx in range(0, 3, 1):
        gol.append(GameBoard[3*x+xx])
      print(gol)
    print("-------------")
  elif TotalGamesPlayed<25:
    time.sleep(0.2)
    for x in range(0, 3, 1):
      gol=[]
      for xx in range(0, 3, 1):
        gol.append(GameBoard[3*x+xx])
      print(gol)
    print("-------------")
  elif TotalGamesPlayed<100:
    time.sleep(0.01)
    for x in range(0, 3, 1):
      gol=[]
      for xx in range(0, 3, 1):
        gol.append(GameBoard[3*x+xx])
      print(gol)
    print("-------------")
  elif TotalGamesPlayed<250 and TotalGamesPlayed%10==0:
    time.sleep(0.1)
    print("Total games played:", TotalGamesPlayed)
  elif TotalGamesPlayed<20000 and TotalGamesPlayed%100==0:
    time.sleep(0.001)
    print("Total games played:", TotalGamesPlayed)
File=open("AIBrain.py", "a")
File.write("Player1=[")
for x in range(0, len(Player1)-1, 1):
  File.write(str(Player1[x])+", ")
File.write(str(Player1[len(Player1)-1]))
File.write("]")
File.close()
print("The AI brain has been saved as AIBrain.py")