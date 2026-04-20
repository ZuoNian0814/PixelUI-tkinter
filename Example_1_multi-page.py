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
    page_config=['page1', 'page2'],
    w=500, h=500
)

# 文本
label = ui.Label(win.screen_frames['page1'], text='Text1')
label.place(x=5, y=5)

label = ui.Label(win.screen_frames['page2'], text='Text2')
label.place(x=5, y=5)

win.mainloop()