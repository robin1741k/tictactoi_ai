# 簡単な条件分岐を追加.

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

bannmenn = np.zeros((3,3), dtype=int)
print(bannmenn)
found_win = False
found_block = False
is_turn = False
which = random.randint(0,1)

if which == 1:
    print("あなたは後手です")
    akimasu_x, akimasu_y = np.where(bannmenn == 0)
    cpu_choice = random.randint(0,len(akimasu_x)-1)
    cpu_x = akimasu_x[cpu_choice]
    cpu_y = akimasu_y[cpu_choice]
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
        # 毎ターンフラグをリセット.
        found_win = False
        found_block = False
        akimasu_x, akimasu_y = np.where(bannmenn == 0)
        for i,j in zip(akimasu_x, akimasu_y):
                bannmenn[i,j] = 2 # 仮置きでシミュレーション.
                if win_judge(bannmenn) == 2:
                    cpu_x, cpu_y = i, j
                    found_win = True
                    break
                else:
                    bannmenn[i,j] = 0
        if not found_win:
            for i,j in zip(akimasu_x, akimasu_y):
                bannmenn[i,j] = 1 # 仮置きでシミュレーション.
                if win_judge(bannmenn) == 1:
                    bannmenn[i,j] = 2
                    cpu_x, cpu_y = i, j
                    found_block = True
                    break
                else:
                    bannmenn[i,j] = 0
            if not found_block:
                cpu_choice = random.randint(0,len(akimasu_x)-1)
                cpu_x = akimasu_x[cpu_choice]
                cpu_y = akimasu_y[cpu_choice]
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