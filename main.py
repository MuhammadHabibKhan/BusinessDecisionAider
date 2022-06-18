# main window
import tkinter as tk
from tkinter import ttk
import math

window = tk.Tk()
window.geometry('700x600')
window.resizable(True, True)
window.title('Business Decision Aider - BDA')

# frames
frame1 = tk.Frame(master=window, width=700, height=600, borderwidth=15, relief='sunken', bg='white')
frame2 = tk.Frame(master=window, width=500, height=600, borderwidth=5, relief='groove', bg='white')
tk.Label(master=frame1, text="Select Maximize / Minimize", bg='white').place(x=10, y=10)

# Combobox
style = ttk.Style()
style.theme_use('alt')
c_var = tk.StringVar()
style.configure("TCombobox", fieldbackground="light green", background="teal")
combo = ttk.Combobox(frame1, style='TCombobox', width=32, textvariable=c_var)
combo['values'] = ('Select', 'Maximize Profit', 'Minimize Cost')
combo['state'] = 'normal'
combo.current(0)
combo.place(x=10, y=35)

# 1st Label
tk.Label(frame1, text="Enter Number of Models ", bg='white').place(x=10, y=70)
# 1st Entry
ent_data_var = tk.IntVar()
ent_data = tk.Entry(frame1, width=33, bg='light blue', state='normal', textvariable=ent_data_var)
ent_data.place(x=10, y=90)
ent_data.focus()

# 2nd Label
tk.Label(frame1, text="Enter Number of Variables", bg='white').place(x=10, y=120)
# 2nd Entry
ent_LCB_var = tk.IntVar()
ent_LCB = tk.Entry(frame1, width=33, bg='light blue', state='normal', textvariable=ent_LCB_var)
ent_LCB.place(x=10, y=140)
''''
# 3rd Label
tk.Label(frame1, text="Enter Upper Class Boundaries", bg='white').place(x=10, y=170)
# 3rd Entry
ent_UCB_var = tk.IntVar()
ent_UCB = tk.Entry(frame1, width=33, bg='light blue', state='normal', textvariable=ent_UCB_var)
ent_UCB.place(x=10, y=190)

# 4th Label
tk.Label(frame1, text="Enter Frequency", bg='white').place(x=10, y=220)
# 4th Entry
ent_Freq_var = tk.IntVar()
ent_Freq = tk.Entry(frame1, width=33, bg='light blue', state='normal', textvariable=ent_Freq_var)
ent_Freq.place(x=10, y=240)
'''


def clicked():
    print()


# reset button
def clicked1():
    ent_data.delete("0", tk.END)
    ent_LCB.delete("0", tk.END)
    # ent_UCB.delete("0", tk.END)
    # ent_Freq.delete("0", tk.END)
    combo.current(0)


# buttons
style = ttk.Style()
style.configure("TButton", foreground="black", background="pink", borderwidth=5, relief='relieved')
bt = ttk.Button(frame1, text="Next", style='TButton', command=clicked)
bt.place(x=160, y=290)
bt1 = ttk.Button(frame1, text="Reset", style='TButton', command=clicked1)
bt1.place(x=20, y=290)


frame1.pack(side='left')

window.mainloop()
