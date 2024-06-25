import pyautogui
import time
import keyboard
#pip install pyautogui
#pip install keyboard
#
#
def move_mouse_to(position):
    """指定された位置にマウスカーソルを移動させる"""
    x, y = position
    pyautogui.moveTo(x, y)

def MoveAndPress(x,y,sl,t):
        time.sleep(t)
        pyautogui.moveTo(x, y)
        time.sleep(t)
        pyautogui.press(sl)
        time.sleep(t)
def MoveAndClick(x,y,t):
        pyautogui.moveTo(x, y)
        time.sleep(t)
        pyautogui.keyDown('shift')
        pyautogui.click()
        time.sleep(t)
        pyautogui.keyUp('shift')
        time.sleep(t)

#lx,ly,rx,ry,ax,ay=(0,0,0,0,0,0)
#この行でスロットの座標を指定すればtry~while間の座標取得を消しても動きます
#あとpauseを指定していますが不都合あれば変更してください
try:
   
    
    keyboard.wait('pause')  # ''キーが押されるまで待ちます
    lx,ly =pyautogui.position()     #Aスロット座標
    print(f"x:{lx}y:{ly}")
    
    keyboard.wait('pause')  # ''キーが押されるまで待ちます
    rx,ry =pyautogui.position()  #Bスロット座標
    print(f"x:{rx}y:{ry}")

    keyboard.wait('pause')  # ''キーが押されるまで待ちます
    ax,ay =pyautogui.position() #完成品スロット座標
    print(f"x:{ax}y:{ay}")

    #9スロット目に刀が来るようにしてください
    #あとrx,ryの値を使えば一応Bスロットのアイテムも自動で入れられます
    #pauseを押す度に動作するようになっている(はず)
    #for文消したら1スタックとか一気にできるよ
    #pyautoguiの機能で画面左上にマウスを無理やり移動させると強制停止できるようになってるよ
    while True:
    
        keyboard.wait('pause')  # ''キーが押されるまで待ちます
        for i in range(64):
    #MoveAndPress(rx,ry,str(j),0.1)
            MoveAndPress(lx,ly,"9",0.1)
            MoveAndClick(ax,ay,0.1)
except KeyboardInterrupt:
        print("Operation cancelled.")

