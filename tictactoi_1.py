# ここでは学んだ知識を活かしてミニゲームなどを作っていく.

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
turn = 1

while turn <= 9:
    if turn % 2 == 1:
        print("あなたの番です")
        print("どこに石を置きますか？ ( , )で入力してください")
        x,y = map(int, input().split(","))
        if bannmenn[x,y] != 0:
            print("既に石が置かれています")
        else:
            bannmenn[x,y] = 1
            print(f"{(x,y)}に石を置きました")
    else:
        print("相手の番です")
        akimasu_x, akimasu_y = np.where(bannmenn == 0)
        # print(akimasu_x, akimasu_y)
        cpu_choice = random.randint(0,len(akimasu_x)-1)
        cpu_x = akimasu_x[cpu_choice]
        cpu_y = akimasu_y[cpu_choice]
        bannmenn[cpu_x,cpu_y] = 2
        print(f"CPUは({cpu_x},{cpu_y})に石を置きました")
    print(bannmenn)
    if win_judge(bannmenn) == 1:
        print("あなたの勝ちです")
        break
    elif win_judge(bannmenn) == 2:
        print("あなたの負けです")
        break
    elif win_judge(bannmenn) == 0:
        turn += 1
if turn == 10:
    print("引き分けです")