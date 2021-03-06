import random
import PySimpleGUI as sg

sg.theme('DarkAmber') 

def main():
    init_window = sg.Window('競馬ython', layout_default, size=(300, 150))

    while True:
        event, values = init_window.read()
        if event == sg.WIN_CLOSED or event == cancel:
            break
        elif event == '三連単':
            window_proc(0)
        elif event == '三連複':
            window_proc(1)
        elif event == '単勝':
            window_proc(2)
        elif event == '複勝':
            window_proc(3)
        elif event == '枠連':
            window_proc(4)

    init_window.close()

text = '出生頭数は？'
select = '選択してください'
go = 'GO!!'
cancel = 'やめる'
starters = sorted(list(range(5,19)), reverse=True)

# ボタン
col1 = [
    [sg.Button('三連単')], 
    [sg.Button('三連複')], 
    [sg.Button('単勝')], 
]
col2 = [
    [sg.Button('複勝')], 
    [sg.Button('枠連')], 
    [sg.Button(cancel)],
]


# 初期画面のレイアウト
layout_default = [  
            [sg.Column(col1),sg.Column(col2)] 
        ]


# 三連単のウインドウを呼ぶ関数
def window_proc(case):
        if case == 0:
            layout_tierce = [  
                [
                sg.Text(text), 
                sg.Combo(
                    values=starters,
                    default_value=select,
                    size=(30,1),
                    readonly=True)
                ],
                [
                sg.Button(go),
                sg.Button(cancel)
                ] 
                ]
            window = sg.Window('三連単', layout_tierce, size=(300,150))

            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == cancel:
                    break
                elif event == go:
                    if values[0] == select:
                        sg.popup('値を入力してくれ；；')
                    else:
                        result = tip_tierce(values[0])
                        sg.popup(result)

            window.close()

        elif case == 1:           
            layout_trio = [  
                [
                sg.Text(text), 
                sg.Combo(
                    values=starters,
                    default_value=select,
                    size=(30,1),
                    readonly=True)
                ],
                [
                sg.Button(go),
                sg.Button(cancel)
                ] 
                ]
            window = sg.Window('三連複', layout_trio, size=(300,150))

            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == cancel:
                    break
                elif event == go:
                    if values[0] == select:
                        sg.popup('値を入力してくれ；；')
                    else:
                        result = tip_tierce(values[0])
                        sg.popup(result)

            window.close()

        elif case == 2:
            layout_win = [  
                [
                sg.Text(text), 
                sg.Combo(
                    values=starters,
                    default_value=select,
                    size=(30,1),
                    readonly=True)
                ],
                [
                sg.Button(go),
                sg.Button(cancel)
                ] 
                ]
            window = sg.Window('単勝', layout_win, size=(300,150))

            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == cancel:
                    break
                elif event == go:
                    if values[0] == select:
                        sg.popup('値を入力してくれ；；')
                    else:
                        result = tip_win(values[0])
                        sg.popup(result)

            window.close()

        elif case == 3:
            layout_show = [  
                [
                sg.Text(text), 
                sg.Combo(
                    values=starters,
                    default_value=select,
                    size=(30,1),
                    readonly=True)
                ],
                [
                sg.Button(go),
                sg.Button(cancel)
                ] 
                ]
            window = sg.Window('複勝', layout_show, size=(300,150))

            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == cancel:
                    break
                elif event == go:
                    if values[0] == select:
                        sg.popup('値を入力してくれ；；')
                    else:
                        result = tip_win(values[0])
                        sg.popup(result)

            window.close()

        elif case == 4:
            layout_bracket = [  
                [
                sg.Text(text), 
                sg.Combo(
                    values=starters,
                    default_value=select,
                    size=(30,1),
                    readonly=True)
                ],
                [
                sg.Button(go),
                sg.Button(cancel)
                ] 
                ]
            window = sg.Window('複勝', layout_bracket, size=(300,150))

            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == cancel:
                    break
                elif event == go:
                    if values[0] == select:
                        sg.popup('値を入力してくれ；；')
                    else:
                        result = tip_bracket()
                        sg.popup(result)

            window.close()



# 三連単のデータ処理する関数
def tip_tierce(NumOfRunners):
    tierce = (sorted(random.sample(range(1,int(NumOfRunners)),k=3)))
    return ('-'.join(map(str, tierce)))
# 単勝
def tip_win(NumOfRunners):
    win = (random.sample(range(1,int(NumOfRunners)),k=1))
    return win
# 枠連
def tip_bracket():
    bracket = (random.sample(range(1,9),k=2))
    return ('-'.join(map(str, bracket)))

if __name__ == "__main__":
    main()

