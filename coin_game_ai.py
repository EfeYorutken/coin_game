#todo
#add continious gameplay
import ai_stuff as ais
import random


def generate_random_game(length):
    res = []
    for i in range(length):
        res.append(random.randint(0,length))
    return res

def game():
    game_over = False
    level = 5
    while not game_over:
        game = generate_random_game(level)
        root = ais.node(game)
        ais.give_ai_game(game,root)
        
        max_socre = sum(game)
        user_score = 0
        print("================================")
        print(f"L E V E L\t{level}")
        print("================================")
        while True:
            print(game)
            move = input("which end do you wanto remove from? (right/left)")
            if move == "right" or move == "left":
                if move == "right":
                    root = root.right
                    user_score += game[len(game)-1]
                else:
                    root = root.left
                    user_score += game[0]
                if len(root.val) < 1:
                    break
                ai_response = ais.make_ai_move(root)
                if ai_response == "right":
                    root = root.right
                else:
                    root = root.left
                if len(root.val) < 1:
                    break
                game = root.val
            else:
                print("invalid option")
        if user_score > (max_socre - user_score):
            print(f"You won {user_score} to {max_socre - user_score}")
            level += 1
        elif user_score < (max_socre - user_score): 
            print(f"You lost {user_score} to {max_socre - user_score}")
            game_over = True
        else:
            print("it is a tie")

game()
