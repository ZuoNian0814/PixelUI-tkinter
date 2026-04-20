import PixelUI as ui


"""
用法和 tkinter 基本相同，其他例子均在 PixelUI.py 的注释中

The usage is basically the same as tkinter. Other examples are in the comments of PixelUI. py
"""

def new():
    print('new')

def open_f():
    print('open')

def command():
    print('command')

def command_with_args(args):
    print(f'command {args}')

win = ui.Win(
    title='Main win',
    # 顶端菜单
    menu_config={
        "File": {"new": new},
        "Open": {"open": open_f}
    },
    w=500, h=500
)

# 文本
label = ui.Label(win.screen_frame, text='Text')
label.place(x=5, y=5)

# 按钮
button = ui.Button(win.screen_frame, text='Button', command=command, stroke=True)
button.place(x=5, y=30)

# 带参数的按钮
button_with_args = ui.Button(win.screen_frame, text='Button_with_args', command=command_with_args, command_args='text', stroke=True)
button_with_args.place(x=5, y=65)

# 多函数按钮
button = ui.Button(win.screen_frame, text='Multi function Button', command=(new, command), stroke=True)
button.place(x=5, y=100)

# 切换按钮
switch_button = ui.Button(win.screen_frame, text='Switch Button', command=(new, command), stroke=True, switch=True)
switch_button.place(x=5, y=135)

entry = ui.Entry(win.screen_frame)
entry.place(x=5, y=170)

win.mainloop()