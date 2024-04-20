import random

class node:
    def __init__(self,val):
        self.val = val
        self.left : node = None
        self.right : node = None

def give_ai_game(game, root):
    if len(game) == 0 or root == None:
        return
    game_left = game[1:]
    game_right = game[:len(game)-1]
    root.left = node(game_left)
    root.right = node(game_right)

    give_ai_game(game_right,root.right)
    give_ai_game(game_left,root.left)

def print_tree(root, begin):
    if root == None:
        return
    print(f"{begin}{root.val}")
    print_tree(root.left, begin+"-")
    print_tree(root.right, begin+"-")

def evaluate(root,ai_turn)->int:
    if len(root.val) <= 2:
        if ai_turn:
            if len(root.val) == 0:
                return 0
            return max(root.val)
        else:
            if len(root.val) == 0:
                return 0
            return max(root.val) * -1
    left_res = evaluate(root.left,not ai_turn)
    right_res = evaluate(root.right,not ai_turn)

    return max(left_res,right_res)



def make_ai_move(root):
    left_eval = evaluate(root.left,True)
    right_eval = evaluate(root.right,True)
    if left_eval > right_eval:
        return "left"
    else:
        return "right"
