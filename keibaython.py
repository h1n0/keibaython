import random
import PySimpleGUI as sg

sg.theme('DarkAmber') 

# 初期画面ウィンドウに配置するコンポーネント
layout = [  [sg.Text('出走頭数は？'), 
                sg.Combo(
                    values=[18,17,16,15,14,13,12,11,10,9,8,7,6,5],
                    default_value='選択してください',
                    size=(30,1),
                    readonly=True)
            ],
            [sg.Button('GO!!'),
            sg.Button('やめる')
            ] 

]

# 初期画面ウィンドウの生成
window = sg.Window('競馬ython', layout, size=(300, 150))


# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'やめる':
        break
    elif event == 'GO!!':
        if values[0] == '選択してください':
            sg.popup('値を入力してくれ；；')
        else:
            tierce = (sorted(random.sample(range(1,int(values[0])),k=3)))
            sg.popup('-'.join(map(str,tierce)))

window.close()

