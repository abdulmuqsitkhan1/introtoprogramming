# === Global Variables ===
gravity = 0
reciever = False
Charge_Level = 0
xVelocity = 0
yVelocity = 0
inPlay = False
Player_1_Score = 0
Player_2_Score = 0
Max_Score = 10  # Default value

# === Broadcast Stub Functions ===
def broadcast(event_name):
    print(f"[Broadcast] {event_name}")

def say(message, duration):
    print(f"[Say] {message} ({duration}s)")

def set_position(x, y):
    print(f"[Set Position] x: {x}, y: {y}")

# === SNAP! Function Equivalents ===

def hitBall():
    global gravity, reciever, Charge_Level, xVelocity
    gravity = -0.1
    reciever = not reciever
    Charge_Level = 0
    xVelocity *= -1

def chargeBallPlayer1():
    global Charge_Level, xVelocity, yVelocity
    if Charge_Level == 0:
        xVelocity = 1
        yVelocity = 4
    elif Charge_Level == 1:
        xVelocity = 1.5
        yVelocity = 4
    elif Charge_Level == 2:
        xVelocity = 2
        yVelocity = 4
    elif Charge_Level == 3:
        xVelocity = 2.5
        yVelocity = 4
    elif Charge_Level == 4:
        xVelocity = 3
        yVelocity = 4
    elif Charge_Level == 5:
        xVelocity = 3.5
        yVelocity = 4
    elif Charge_Level == 6:
        xVelocity = 4
        yVelocity = 4
    elif Charge_Level == 7:
        xVelocity = 4.5
        yVelocity = 4
    elif Charge_Level == 8:
        xVelocity = 5
        yVelocity = 4
    elif Charge_Level == 9:
        xVelocity = 5.5
        yVelocity = 4.5
    elif Charge_Level == 10:
        xVelocity = 6
        yVelocity = 5

def chargeBallPlayer2():
    global Charge_Level, xVelocity, yVelocity
    if Charge_Level == 0:
        xVelocity = 1
        yVelocity = 4
    elif Charge_Level == 1:
        xVelocity = 1.5
        yVelocity = 4
    elif Charge_Level == 2:
        xVelocity = 2
        yVelocity = 4
    elif Charge_Level == 3:
        xVelocity = 2.5
        yVelocity = 4
    elif Charge_Level == 4:
        xVelocity = 3
        yVelocity = 4
    elif Charge_Level == 5:
        xVelocity = 3.5
        yVelocity = 4
    elif Charge_Level == 6:
        xVelocity = 4
        yVelocity = 4
    elif Charge_Level == 7:
        xVelocity = 4.5
        yVelocity = 4
    elif Charge_Level == 8:
        xVelocity = 5
        yVelocity = 4
    elif Charge_Level == 9:
        xVelocity = 5.5
        yVelocity = 4.5
    elif Charge_Level == 10:
        xVelocity = 6
        yVelocity = 5
    xVelocity *= -1

def stopPlay():
    global xVelocity, yVelocity, gravity, inPlay
    xVelocity = 0
    yVelocity = 0
    gravity = 0
    inPlay = False

def restartPlay():
    global inPlay, xVelocity, yVelocity, gravity, Charge_Level, reciever
    if not inPlay:
        set_position(-200, 20)
        reciever = False
        xVelocity = 5
        Charge_Level = 0
        broadcast("reset")
        gravity = -0.1
        yVelocity = 4
        inPlay = True

def stopGame():
    if Player_1_Score == Max_Score:
        broadcast("stopGame")
        say("Player 1 wins!", 4)
    else:
        broadcast("stopGame")
        say("Player 2 wins!", 4)

def scoringNet(r):
    global Player_1_Score, Player_2_Score
    if r:
        Player_1_Score += 1
        broadcast("Player1Scored")
    else:
        Player_2_Score += 1
        broadcast("Player2Scored")