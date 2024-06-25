# SlashBrade_AutoRefine
抜刀剣を自動で修理したい！

pauseを指定していますが不都合あれば変更してください

# インポート

多分pythonはpython3ならどれでも動く(3.9以降なら確実に)

    pip install pyautogui
    pip install keyboard

# Tips:
9スロット目に刀が来るようにしてください

rx,ryの値を使えば一応Bスロットのアイテムも自動で入れられます

pauseを押す度に動作するようになっている(はず)

for文消したら1スタックとか一気にできるよ

pyautoguiの機能で画面左上にマウスを無理やり移動させると強制停止できるようになってるよ

MoveAndPress()関数は　「特定座標にマウスを移動」「ホットバーのスロット（1~9）のアイテムを移動」だよ
