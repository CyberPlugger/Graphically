import tkinter as tk
from tkinter import filedialog
import threading

root = tk.Tk()
root.configure(background='#000')
root.title('Graphically Project')

def get_endswith(text, prefix):
    return str(text).removeprefix(prefix).lstrip()

good_gr = ['amazing', 'good', 'gamer', '999', 'horrendous', 'cool']
bad_gr = ['bad', 'horrible', 'trash', '-999', 'terrible', 'shit']

def __graphics(graphics):
    global good_gr, bad_gr
    if graphics in good_gr:
        tk.Label(root, text='good graphics', fg='#fff', bg='#000').pack()
    elif graphics in bad_gr:
        tk.Label(root, text='bad graphics', fg='#fff', bg='#000').pack()
    else:
        raise type('GraphicallyException', (Exception,), {})('unknows graphics')

def __fps(fps):
    if int(fps) >= 60:
        tk.Label(root, text='good fps', fg='#fff', bg='#000').pack()
    else:
        tk.Label(root, text='bad fps', fg='#fff', bg='#000').pack()

def __players(players):
    tk.Label(root, text=f'players are {players}', bg='#000', fg="#fff").pack()

def __money(money):
    tk.Label(root, text=f'Money: {money}$', bg='#000', fg="#fff").pack()

intr_dict = {
    'fps =': __fps,
    'players =': __players,
    'graphics =': __graphics,
    'money =': __money,
}

def interpret(command):
    for i in intr_dict:
        if command.startswith(i):
            para = get_endswith(command, i)
            intr_dict[i](para)
            break

def main():
    x = filedialog.askopenfilename()
    n = open(file=x, mode='r', encoding='utf-8').read()
    for b in n.split('\n'):
        interpret(b)
    return

if __name__ == '__main__':
    print('Graphically interpreter. \nType "interpret from file" to interpret from file.')
    def mama():
        while True:
            x = input('> ')
            if x == 'interpret from file': main()
            else: interpret(x)
    threading.Thread(target=mama, daemon=True).start()

root.mainloop()