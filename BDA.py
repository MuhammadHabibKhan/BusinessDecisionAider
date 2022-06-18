import tkinter as tk
from tkinter import ttk
from tkinter import *
import copy
from ElementaryRowOperations import *
import tkinter.messagebox
import re


window = tk.Tk()
window.geometry('400x600')
window.resizable(True, True)
window.title("Business Decision Aider - BDA")


frame1 = tk.Frame(master=window, width=400, height=540, borderwidth=10, relief='ridge', bg='grey')  # first page
frame2 = tk.Frame(master=window, width=500, height=600, borderwidth=10, relief='sunken', bg='grey')  # next
frame3 = tk.Frame(master=window, width=500, height=600, borderwidth=10, relief='groove', bg='grey')  # about
frame4 = tk.Frame(master=window, width=400, height=60, borderwidth=10, relief='ridge', bg='light grey')  # menu

msg_window = Toplevel(window, bg='yellow')
msg_window.title('Note')
msg_window.geometry('400x250')
tk.Label(msg_window, text="Ah! Some Bad News... \n \n Bugs & Error may occur when \ncomputing for models and \n variables larger than 2 \n ...\nWhile the user interface is \ndesigned to adapt to any \nvalue entered by the user \nsome expressions & code \nbits needs to be reworked",
         bg='yellow', font=("Helvetica Bold", 15), anchor='e').place(x=130, y=10)
msg_window.attributes('-topmost', True)
#photo_image4 = tk.PhotoImage(file='/Users/mhk/Desktop/Screenshot 2022-01-21 at 8.57.23 PM.png')
photo_image4 = tk.PhotoImage(file='Screenshot 2022-01-19 at 12.36.30 AM.png')
ttk.Label(master=msg_window, background='orange', width=50, image=photo_image4).place(x=10, y=10)


def msg_ok():
    msg_window.destroy()


bt11 = ttk.Button(msg_window, text="OK", style='TButton', command=msg_ok)
bt11.place(x=180, y=213)


#photo_image = tk.PhotoImage(file='/Users/mhk/Desktop/Screenshot 2022-01-19 at 12.36.30 AM.png')
photo_image = tk.PhotoImage(file='Screenshot 2022-01-19 at 12.36.30 AM.png')
ttk.Label(master=frame1, background='grey', image=photo_image).place(x=10, y=280)

#photo_image2 = tk.PhotoImage(file='/Users/mhk/Desktop/Screenshot 2022-01-19 at 7.33.37 AM.png')
photo_image2 = tk.PhotoImage(file='Screenshot 2022-01-19 at 7.33.37 AM.png')
ttk.Label(master=frame1, background='grey', image=photo_image2).place(x=140, y=280)


# Create A Main Frame
main_frame = Frame(window)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
frame5 = tk.Frame(master=my_canvas, width=500, height=5000, borderwidth=10, relief='sunken', bg='grey')  # next_next

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0, 0), window=frame5, anchor="nw")

tk.Label(master=frame1, text="Select Maximize / Minimize", bg='grey').place(x=10, y=10)

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
tk.Label(frame1, text="Enter Number of Models ", bg='grey').place(x=10, y=65)
# 1st Entry
ent_model_var = tk.IntVar()
ent_model = tk.Entry(frame1, width=33, bg='light blue', state='normal', textvariable=ent_model_var)
ent_model.place(x=10, y=90)
ent_model.focus()

# 2nd Label
tk.Label(frame1, text="Enter Number of Variables", bg='grey').place(x=10, y=125)
# 2nd Entry
ent_var_var = tk.IntVar()
ent_var = tk.Entry(frame1, width=33, bg='light blue', state='normal', textvariable=ent_var_var)
ent_var.place(x=10, y=150)

y_cord = 30
n_rows = 0
n_col = 0
var_names = []
model_names = []


def click_next():
    model_names.clear()
    var_names.clear()
    frame5.pack_forget()
    global y_cord_next
    y_cord_next = 0
    # y_cord_next = -50
    global y_cord
    frame1.pack_forget()
    frame4.pack_forget()
    if c_var.get() == 'Maximize Profit':
        try:
            x = list(map(int, ent_model.get().split(' ')))
            y = list(map(int, ent_var.get().split(' ')))
            if x[0] < 2 or y[0] < 2:
                frame4.pack()
                frame1.pack()
                raise StopIteration

            global n_rows
            n_rows = x[0] + 2
            global n_col
            n_col = y[0] + 1

            for i in range(x[0]):
                # 1st Entry on next page (name of models)
                m_name = tk.Label(frame2, text="Model #" + str(i + 1) + ' Name', bg='grey')
                ent_model_name_var = tk.StringVar()
                ent_model_name = tk.Entry(frame2, width=30, bg='light blue', state='normal',
                                          textvariable=ent_model_name_var)
                if i == 0:
                    ent_model_name.place(x=10, y=y_cord)
                    model_names.append(ent_model_name)
                    m_name.place(x=10, y=y_cord - 25)
                else:
                    y_cord += 32
                    m_name.place(x=10, y=y_cord)
                    y_cord += 28
                    ent_model_name.place(x=10, y=y_cord)
                    model_names.append(ent_model_name)
            for j in range(y[0]):
                # 2nd Entry on next page (name of variables)
                v_name = tk.Label(frame2, text="Variable #" + str(j + 1) + ' Name', bg='grey')
                ent_var_name_var = tk.StringVar()
                ent_var_name = tk.Entry(frame2, width=30, bg='light blue', state='normal',
                                        textvariable=ent_var_name_var)
                y_cord += 32
                v_name.place(x=10, y=y_cord)
                y_cord += 28
                ent_var_name.place(x=10, y=y_cord)
                var_names.append(ent_var_name)

            y_cord += 60
            bt5.place(x=20, y=y_cord)
            bt7.place(x=165, y=y_cord)
        except ValueError or TypeError:
            tk.messagebox.showwarning(title='Invalid Input', message='Please enter Integer Values')
            frame4.pack()
            frame1.pack()
        except StopIteration:
            tk.messagebox.showwarning(title='Invalid Input', message='Please Enter Values > 1')
        else:
            frame2.pack()
        # finally:
            # frame4.pack()
            # frame1.pack()
    else:
        import tkinter.messagebox
        tk.messagebox.showwarning(title='Wrong Selection', message='Please Select a Valid Function')
        frame4.pack()
        frame1.pack()

    # y_cord += 60
    # bt5.place(x=20, y=y_cord)
    # bt7.place(x=165, y=y_cord)
    # frame2.pack()


y_cord_next = -50
t_matrix = []


def click_next_next():
    t_matrix.clear()
    frame2.pack_forget()
    # bt9["state"] = "enabled"
    global y_cord_next
    y_cord_next = 0
    y_cord_next = -50
    # frame5.pack_forget()
    if c_var.get() == 'Maximize Profit':
        x = list(map(int, ent_model.get()))
        y = list(map(int, ent_var.get()))
        global n_rows
        n_rows = x[0] + 2
        global n_col
        n_col = y[0] + 1

        name_list = ''
        u = 0
        for names in model_names:
            if u > 0:
                y_cord_next += 60 * n_col
            if u == len(model_names) - 1:
                name_list = name_list + str(names.get())
                mod = name_list[len(mod) + 1:]
                u += 1
            else:
                name_list = name_list + str(names.get()) + '\n'
                n_list = copy.deepcopy(name_list)
                mod = n_list.split('\n')[0]
                u += 1

            entry_list = ''
            h = 0
            for entries in var_names:
                if h == len(var_names) - 1:
                    entry_list = entry_list + str(entries.get())
                    res2 = entry_list[len(res) + 1:]
                    var_q = tk.Label(frame5, text="Amount of " + str(res2) + ' Required For ' + str(mod), bg='grey', anchor="w", width=40)
                    y_cord_next += 60
                    var_q.place(x=10, y=y_cord_next)
                    h += 1
                else:
                    entry_list = entry_list + str(entries.get()) + '\n'
                    e_list = copy.deepcopy(entry_list)
                    res = e_list.split('\n')[0]
                    var_q = tk.Label(frame5, text="Amount of " + str(res) + ' Required For ' + str(mod), bg='grey', anchor="w", width=40)
                    y_cord_next += 60
                    var_q.place(x=10, y=y_cord_next)
                    h += 1
        print(name_list)
        for i in range(x[0]):  # loop on number of models
            for j in range(y[0]):  # loop on number of variables
                ent_var_quantity_var = tk.IntVar()
                ent_var_quantity = tk.Entry(frame5, width=30, bg='light blue', state='normal',
                                            textvariable=ent_var_quantity_var)
                t_matrix.append(ent_var_quantity)
                if j == 0 and i == 0:
                    y_cord_next = 35
                    # y_cord_next += 60
                    ent_var_quantity.place(x=10, y=y_cord_next)
                else:
                    y_cord_next += 60
                    ent_var_quantity.place(x=10, y=y_cord_next)

            # constraints S1, S2, ... etc
            for k in range(x[0]):
                y_cord_next += 35
                tk.Label(frame5, text="Non-Negativity Constraints", bg='grey', anchor="w", width=40).place(x=10, y=y_cord_next)
                ent_neg_cons_var = tk.IntVar()
                ent_neg_cons = tk.Entry(frame5, width=30, bg='light grey', state='normal',
                                        textvariable=ent_neg_cons_var)
                t_matrix.append(ent_neg_cons)
                y_cord_next += 25
                ent_neg_cons.place(x=10, y=y_cord_next)
                if k == 0 and i == 0:
                    ent_neg_cons.delete('0', END)
                    ent_neg_cons.insert(END, '1')
                elif k == 1 and i == 0:
                    ent_neg_cons.delete('0', END)
                    ent_neg_cons.insert(END, '0')
                elif k == 0 and i == 1:
                    ent_neg_cons.delete('0', END)
                    ent_neg_cons.insert(END, '0')
                elif k == 1 and i == 1:
                    ent_neg_cons.delete('0', END)
                    ent_neg_cons.insert(END, '1')

            y_cord_next += 35
            mn = re.split("\n", name_list)
            tk.Label(frame5, text="Minimum Amount of " + str(mn[i]) + " required", bg='grey', anchor="w", width=40).place(x=10, y=y_cord_next)
            ent_rhv_var = tk.IntVar()
            ent_rhv = tk.Entry(frame5, width=30, bg='light yellow', state='normal', textvariable=ent_rhv_var)
            t_matrix.append(ent_rhv)
            y_cord_next += 25
            ent_rhv.place(x=10, y=y_cord_next)

        for L in range(y[0]):
            y_cord_next += 35
            vn = re.split('\n', entry_list)
            tk.Label(frame5, text="Cost of " + str(vn[L]), bg='grey', anchor="w", width=40).place(x=10, y=y_cord_next)
            ent_cost_var = tk.IntVar()
            ent_cost = tk.Entry(frame5, width=30, bg='light pink', state='normal', textvariable=ent_cost_var)
            t_matrix.append(ent_cost)
            y_cord_next += 25
            ent_cost.place(x=10, y=y_cord_next)

    y_cord_next += 60
    bt8.place(x=20, y=y_cord_next)
    bt9.place(x=165, y=y_cord_next)
    main_frame.pack(fill=BOTH, expand=1)

    return name_list


def how_to():
    how_to_window = Toplevel(window)
    how_to_window.geometry('400x600')
    how_to_window.resizable(True, True)
    how_to_window.title("BDA - GUIDE")


def click_home():
    frame2.pack_forget()
    frame3.pack_forget()
    frame1.pack()
    frame4.pack()


def click_reset():
    # frame5.pack_()
    # frame3.pack_forget()
    frame2.pack_forget()
    # main_frame.pack_forget()
    ent_model.delete("0", tk.END)
    ent_var.delete("0", tk.END)
    combo.current(0)


def click_back_next():
    global y_cord_next
    y_cord_next = 0
    # y_cord_next = -50
    global y_cord
    y_cord = 30
    frame5.pack_forget()
    frame2.pack_forget()
    frame4.pack()
    frame1.pack()


def click_back_about():
    frame3.pack_forget()
    frame4.pack()
    frame1.pack()


def click_about():
    frame4.pack_forget()
    frame1.pack_forget()
    tk.Label(frame3, text="Software by ~ m h k ~ \n Based on Simplex Method \n Built for 2nd Semester Project "
                          "\n University Of Karachi - DCS (UBIT) ", bg='grey', ).place(x=60, y=165)
    frame3.pack()


def click_back_next_next():
    global y_cord_next
    y_cord_next = 0
    main_frame.pack_forget()
    # frame5.pack_forget()
    frame2.pack()


m = []
matrix = []


def click_result():
    global m, matrix, t_matrix
    m.clear()
    matrix.clear()
    try:
        for x in range(len(t_matrix)):
            e = list(map(int, t_matrix[x].get().split(' ')))
            m.append(e[0])
        a = list(map(int, ent_model.get().split(' ')))
        s = list(map(int, ent_var.get().split(' ')))
        for c in range(a[0] + 2):
            if c == s[0]:
                m.append(1)
            else:
                m.append(0)
        for v in range(a[0] + 2, len(t_matrix), a[0] + 4):  # only working for 2 two models, change the INDEX EXPRESSION
            m.insert(v, 0)

        nr = a[0] + 1
        nc = s[0] + s[0] + 1 + 1

        # global matrix

        #   r = 0
        #    while r < nr:
        #        r_matrix = []
        #        c = 0
        #        while c < nc:
        #            a = m[c]
        #            r_matrix.append(a)
        #            c = c + 1
        #        matrix.append(r_matrix)
        #        r = r + 1

        for w in range(nr):
            r_matrix = []
            for z in range(nc):
                if w == 0:
                    a = m[z]
                    r_matrix.append(a)
                else:
                    a = m[z+(nc*w)]  # expression not working with > 2
                    r_matrix.append(a)
            matrix.append(r_matrix)

        def pivot_column(mat):
            nc = len(mat[0])
            minimum = mat[nr - 1][0]
            m_index = 0
            for i in range(1, nc):
                if mat[nr - 1][i] < minimum:
                    minimum = mat[nr - 1][i]
                    m_index = i
            if minimum < 0:
                return m_index + 1

        def pivot_row(mat, m_index):
            try:
                nc = len(mat[0])
                nr = len(mat)
                lowest_ratio = mat[0][nc - 1] / mat[0][m_index - 1]
                row_index = 0
                for i in range(1, nr - 1):
                    if mat[i][nc - 1] / mat[i][m_index - 1] < lowest_ratio:
                        lowest_ratio = mat[i][nc - 1] / mat[i][m_index - 1]
                        row_index = i
            except ZeroDivisionError:
                tk.messagebox.showwarning(title='Invalid Input', message='Please Enter Valid Values')
            else:
                if lowest_ratio > 0:
                    return row_index + 1

        mat = copy.deepcopy(matrix)

        nc = len(mat[0])
        nr = len(mat)

        while True:
            a = pivot_column(mat)
            if a is None:
                break
            b = pivot_row(mat, a)
            print("Pivot Element's Coordinates are: ")
            print(b)
            print(a)
            print()
            c = reduce_to_one(mat, b - 1, a - 1)
            for h in range(nr - 1):  # -2 instead of -1 as we have labels now too
                main_mat = below_pivot_zero(c, b - 1 - h - 1, a - 1, b - 1)
                # print_matrix(d)
                # print()
            for k in range(nc - 1):
                if main_mat[nr - 1][k] >= 0:
                    break
        print(main_mat)
    except NameError or ValueError or TypeError or UnboundLocalError or ZeroDivisionError:
        tk.messagebox.showwarning(title='Invalid Input', message='Please Enter Valid Values')
        raise StopIteration
    else:
        return main_mat
    finally:
        m.clear()
        matrix.clear()


def display_result():
    global m
    global matrix
    # m.clear()
    # matrix.clear()
    global y_cord_next
    y_cord_next = 10
    try:
        d = click_result()
    except NameError or ValueError or TypeError or UnboundLocalError or ZeroDivisionError or StopIteration:
        #global m
        #global matrix
        m = []
        matrix = []
        tk.messagebox.showwarning(title='Invalid Input', message='Please Enter Valid Values')
    else:
        result_window = Toplevel(window, bg='grey')
        result_window.geometry('400x600')
        result_window.resizable(True, True)
        result_window.title("RESULT")

        def close():
            result_window.destroy()

        bt10 = ttk.Button(result_window, text="CLOSE", style='TButton', command=close)
        bt10.place(x=200, y=425)

        tbox = tk.Text(result_window, borderwidth=5, relief='sunken', width=40, height=20, bg='light grey',
                       state='normal',
                       font=("Arial", 14))
        tbox.place(x=30, y=30)
        c = click_next_next()
        mn = re.split("\n", c)
        tbox.insert("1.0", 'Maximum Profit is ' + str(d[len(d)-1][len(d[0])-1]) + ' units')
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", 'Amount of ' + str(mn) + ' required is: ')
        a = list(map(int, ent_model.get().split(' ')))
        tbox.insert("3.0", "\n")
        for mod_val in range(1, a[0]+1):
            tbox.insert("3.0", " " + str(d[len(d)-1-mod_val][len(d[0])-1]) + " ")
        tbox.insert("4.0", "\n")
        tbox.insert("4.0", 'units respectively')
        # bt9["state"] = "disabled"
        d.clear()
    finally:
        m.clear()
        matrix.clear()


style = ttk.Style()
style.configure("TButton", foreground="black", background="white", borderwidth=5, relief='relieved')
bt = ttk.Button(frame1, text="Next", style='TButton', command=click_next)
bt.place(x=180, y=210)

bt1 = ttk.Button(frame1, text="Reset", style='TButton', command=click_reset)
bt1.place(x=40, y=210)

bt2 = ttk.Button(frame4, text="HOME", style='TButton', command=click_home)
bt2.place(x=5, y=2)

bt3 = ttk.Button(frame4, text="HOW-TO", style='TButton', command=how_to)
bt3.place(x=132, y=2)

bt4 = ttk.Button(frame4, text="ABOUT", style='TButton', command=click_about)
bt4.place(x=260, y=2)

bt5 = ttk.Button(frame2, text="BACK", style='TButton', command=click_back_next)
# bt5.place(x=55, y=430)

bt6 = ttk.Button(frame3, text="BACK", style='TButton', command=click_back_about)
bt6.place(x=200, y=290)

bt7 = ttk.Button(frame2, text="NEXT", style='TButton', command=click_next_next)
# bt7.place(x=200, y=430)

bt8 = ttk.Button(frame5, text="BACK", style='TButton', command=click_back_next_next)
# bt8.place(x=55, y=y_cord_next)

bt9 = ttk.Button(frame5, text="RESULT", style='TButton', command=display_result)
# bt9.place(x=200, y=y_cord_next)

#photo_image3 = tk.PhotoImage(file='/Users/mhk/Desktop/Screenshot 2022-01-19 at 12.15.04 AM.png')
photo_image3 = tk.PhotoImage(file='Screenshot 2022-01-19 at 7.33.37 AM.png')
grey_img = ttk.Label(master=frame5, background='grey', image=photo_image3)

frame1.pack(side='bottom')
frame4.pack(side='top')
window.mainloop()

print(m)
print(matrix)
