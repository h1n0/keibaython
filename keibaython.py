import random
import PySimpleGUI as sg

sg.theme('DarkAmber') 

def main():
    window = sg.Window('競馬ython', layout_default, size=(300, 150))

# イベントループ
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'やめる':
            break
        elif event == '三連単':
            window_tierce()


    window.close()

# 初期画面ウィンドウに配置するコンポーネント
layout_default = [  
            [sg.Button('三連単'),
            sg.Button('やめる')
            ] 

]



# 初期画面ウィンドウの生成


# 三連単
def window_tierce():
    layout_tierce = [  
    [
    # テキストメッセージ
    sg.Text('出走頭数は？'), 
    # ドロップダウンリスト
    sg.Combo(
        values=[18,17,16,15,14,13,12,11,10,9,8,7,6,5],
        default_value='選択してください',
        size=(30,1),
        readonly=True)
    ],
    [
    # ボタン
    sg.Button('GO!!'),
    sg.Button('やめる')
    ] 
    ]
    WindowTierce = sg.Window('三連単', layout_tierce, size=(300,150))
    while True:
        event, values = WindowTierce.read()
        if event == sg.WIN_CLOSED or event == 'やめる':
            break
        elif event == 'GO!!':
            if values[0] == '選択してください':
                sg.popup('値を入力してくれ；；')
            else:
                result = tip_tierce(values[0])
                sg.popup(result)
    WindowTierce.close()


def tip_tierce(NumOfRunners):
    
    # 処理
    tierce = (sorted(random.sample(range(1,int(NumOfRunners)),k=3)))
    return tierce

if __name__ == "__main__":
    main()

