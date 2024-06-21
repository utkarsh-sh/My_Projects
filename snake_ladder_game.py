import random
def board(l):
    turn = 2
    for i in range(0, 100):
        l.insert(i,i+1)

    for j in range(99, -1, -10):
        if (turn % 2 == 0):
            print(f"{l[j]} | {l[j - 1]} | {l[j - 2]} | {l[j - 3]} | {l[j - 4]} "
                  f"| {l[j - 5]} | {l[j - 6]} | {l[j - 7]} | {l[j - 8]} | {l[j - 9]}")
            print("-------------------------------------------------------------------")
            turn -= 1
        else:
            print(f"{l[j - 9]} | {l[j - 8]} | {l[j - 7]} | {l[j - 6]} | {l[j - 5]} "
                  f"| {l[j - 4]} | {l[j - 3]} | {l[j - 2]} | {l[j - 1]} | {l[j]}")
            print("-------------------------------------------------------------------")
            turn += 1
def print_ladders_and_snakes():
    print("LADDER\n 3-24\n 14-42\n 30-86\n 37-57\n 50-96\n 66-74\n")
    print("SNAKES\n 95-18\n 77-45\n 60-28\n 34-10\n 20-2\n")
def move_player(player, move, moves_made):
    moves_made[player] += move
    if moves_made[player] in LADDERS:
        moves_made[player] = LADDERS[moves_made[player]]
    if moves_made[player] in SNAKES:
        moves_made[player] = SNAKES[moves_made[player]]
    return moves_made[player]

LADDERS = {3: 24, 14: 42, 30: 86, 37: 57, 50: 96, 66: 74}
SNAKES = {95: 18, 77: 45, 60: 28, 34: 10, 20: 2}
def play_game():
    whoo = input("Enter player 1 name :")
    wh = input("Enter player 2 name :")
    player = 1
    moves_made = {whoo: 1, wh: 1}
    dice=[1,2,3,4,5,6]
    while moves_made[whoo] <= 100 and moves_made[wh] <= 100:
        if player == 1:
            chance_1 = int(input(f"{whoo} Enter 1 ROLL the die! "))
            if chance_1 == 1:
                move = random.choice(dice)
                print(f"{whoo} rolled a {move}")
                moves_made[whoo] = move_player(whoo, move, moves_made)
                print(f"{whoo} is at position {moves_made[whoo]}")
                player = 2
        else:
            chance_2 = int(input(f"{wh} Enter 1 ROLL the die! "))
            if chance_2 == 1:
                move = random.choice(dice)
                print(f"{wh} rolled a {move}")
                moves_made[wh] = move_player(wh, move, moves_made)
                print(f"{wh} is at position {moves_made[wh]}")
                player = 1

    if moves_made[whoo] > moves_made[wh]:
        print(f"Congrats {whoo}!!")
    else:
        print(f"Congrats {wh}!!")

l=[]
board(l)
print_ladders_and_snakes()
play_game()