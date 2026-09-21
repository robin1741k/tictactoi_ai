# minimax追加.

import numpy as np
import random

def win_judge(x):
    # 縦横のチェック
    for i in range(0,3):
        row = x[i,:]
        column = x[:,i]
        if np.all(row == row[0]) and row[0] != 0:
            return row[0]
        elif np.all(column == column[0]) and column[0] != 0:
            return column[0]
    # 斜めのチェック        
    diag1 = np.diagonal(x)
    diag2 = np.diagonal(np.fliplr(x))
    if np.all(diag1 == diag1[0]) and diag1[0] != 0:
        return diag1[0]
    elif np.all(diag2 == diag2[0]) and diag2[0] != 0:
        return diag2[0]
    return 0

def minimax(bannmenn,is_max):
    result = win_judge(bannmenn)
    if result == 2:
        return 1
    elif result == 1:
        return -1
    elif 0 not in bannmenn:
        return 0
    if is_max:
        best = -float("inf")
        akimasu_x, akimasu_y = np.where(bannmenn == 0)
        for i,j in zip(akimasu_x,akimasu_y):
            bannmenn[i,j] = 2
            score = minimax(bannmenn, False)
            bannmenn[i,j] = 0
            best = max(score,best)
        return best
    else:
        best = float("inf")
        akimasu_x, akimasu_y = np.where(bannmenn == 0)
        for i,j in zip(akimasu_x,akimasu_y):
            bannmenn[i,j] = 1
            score = minimax(bannmenn, True)
            bannmenn[i,j] = 0
            best = min(score,best)
        return best

bannmenn = np.zeros((3,3), dtype=int)
print(bannmenn)
found_win = False
found_block = False
is_turn = False
which = random.randint(0,1)

if which == 1:
    print("あなたは後手です")
    best = -float("inf")
    best_move = []
    akimasu_x, akimasu_y = np.where(bannmenn == 0)
    for i,j in zip(akimasu_x, akimasu_y):
        bannmenn[i,j] = 2 # 仮置きでシミュレーション.
        score = minimax(bannmenn,False) # 評価
        bannmenn[i,j] = 0 # 戻す
        if score > best:
            best = score
            best_move = [(i,j)]
        elif score == best:
            best_move.append((i,j))
    cpu_x, cpu_y = random.choice(best_move)
    bannmenn[cpu_x,cpu_y] = 2
    print(f"CPUは({cpu_x},{cpu_y})に石を置きました")
    print(bannmenn)
    is_turn = True
else:
    print("あなたが先手です ")
    is_turn = True

while True:
    if is_turn:
        print("あなたの番です")
        print("どこに石を置きますか？ ( , )で入力してください")
        x,y = map(int, input().split(","))
        if bannmenn[x,y] != 0:
            print("既に石が置かれています")
            continue
        else:
            bannmenn[x,y] = 1
            print(f"{(x,y)}に石を置きました")
        is_turn = False
    else:
        print("相手の番です")
        best = -float("inf")
        best_move = []
        akimasu_x, akimasu_y = np.where(bannmenn == 0)
        for i,j in zip(akimasu_x, akimasu_y):
            bannmenn[i,j] = 2 # 仮置きでシミュレーション.
            score = minimax(bannmenn,False) # 評価
            bannmenn[i,j] = 0 # 戻す
            if score > best:
                best = score
                best_move = [(i,j)]
            elif score == best:
                best_move.append((i,j))
        cpu_x, cpu_y = random.choice(best_move)
        bannmenn[cpu_x,cpu_y] = 2
        print(f"CPUは({cpu_x},{cpu_y})に石を置きました")
        is_turn = True
    print(bannmenn)
    if win_judge(bannmenn) == 1:
        print("あなたの勝ちです")
        break
    elif win_judge(bannmenn) == 2:
        print("あなたの負けです")
        break
    if 0 not in bannmenn:
        print("引き分けです")
        break