from tkinter import *

operator = ''

def click_button(character):
    global operator
    operator = operator + character
    calculator_display.delete(0, END)
    calculator_display.insert(END, operator)

def delete_all():
    global operator
    operator = ''
    calculator_display.delete(0, END)

def get_result():
    global operator
    result= str(eval(operator))
    calculator_display.delete(0, END)
    calculator_display.insert(0, result)
    operator = ''

def review_check():
    x = 0
    for b in food_box:
        if food_variables[x].get() == 1:
            food_box[x].config(state=NORMAL)


application = Tk()
application.geometry("1250x630")
application.title("Restaurant system")
application.config(bg="burlywood")

# Top panel
top_panel = Frame(application, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

title_tag = Label(top_panel, text="Invoicing System",
                  fg="azure4", font=("Dosis", 58), bg="burlywood")
title_tag.grid(row=0, column=0)

# Left panel
left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# Cost panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg="azure4", padx=50)
cost_panel.pack(side=BOTTOM)

# Food panel
food_panel = LabelFrame(left_panel, text="Food", font=("Dosis", 19, "bold"),
                        bd=1, relief=FLAT, fg="azure4")
food_panel.pack(side=LEFT)

# drink panel
drink_panel = LabelFrame(left_panel, text="Drink", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
drink_panel.pack(side=LEFT)

# dessert panel
dessert_panel = LabelFrame(left_panel, text="Dessert", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
dessert_panel.pack(side=LEFT)

# Left panel
right_panel = Frame(application, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# Calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
calculator_panel.pack()

# Invoice panel
invoice_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
invoice_panel.pack()

# buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
buttons_panel.pack()

# Product lists
food_list = ["Chicken", "Lamb", "Salmon", "Hake", "Kebab", "Pizza1", "Pizza2", "Pizza3"]
drink_list = ["Lemonade", "Soda", "Juice", "Cola", "White wine", "Red wine", "Rose wine", "Prosecco"]
dessert_list = ["Ice cream", "Fruit", "Brownies"]

drink_variables = []
drink_box = []
drink_text = []
counter = 0
for drink in drink_list:
    drink_variables.append('')
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drink_panel, text=drink.title(), font=("Dosis", 19, "bold"), onvalue=1,
                        offvalue=0, variable=drink_variables[counter],
                        command=review_check)
    drink.grid(row=counter, column=0, sticky=W)

    drink_box.append("")
    drink_box.append("")
    drink_box[counter] = Entry(drink_panel, font=("Dosis", 19, "bold"), bd=1, width=6,
                               state=DISABLED, textvariable=[counter])
    drink_box[counter].grid(row=counter, column=1)
    counter += 1

dessert_variables = []
dessert_box = []
dessert_text = []
counter = 0
for dessert in dessert_list:
    dessert_variables.append('')
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_panel, text=dessert.title(), font=("Dosis", 19, "bold"), onvalue=1, offvalue=0,
                          variable=dessert_variables[counter])
    dessert.grid(row=counter, column=0, sticky=W)

    dessert_box.append("")
    dessert_box.append("")
    dessert_box[counter] = Entry(dessert_panel, font=("Dosis", 19, "bold"), bd=1, width=6,
                                 state=DISABLED, textvariable=[counter],
                                 command=review_check)
    dessert_box[counter].grid(row=counter, column=1)
    counter += 1

food_variables = []
food_box = []
food_text = []
counter = 0

for food in food_list:
    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel, text=food.title(), font=("Dosis", 19, "bold"),
                       onvalue=1, offvalue=0, variable=food_variables[counter],
                       command=review_check)
    food.grid(row=counter, column=0, sticky=W)

    food_box.append("")
    food_box.append("")
    food_box[counter] = Entry(food_panel, font=("Dosis", 19, "bold"),
                              bd=1, width=6, state=DISABLED,
                              textvariable=[counter])
    food_box[counter].grid(row=counter, column=1)
    counter += 1

# Variables
food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_cost_var = StringVar()
taxes_cost_var = StringVar()
total_cost_var = StringVar()

# Cost label
food_cost_label = Label(cost_panel,
                        text="Food Cost",
                        font=("Dosis", 12, "bold"),
                        bg="azure4",
                        fg="white")
food_cost_label.grid(row=0, column=0)
food_cost_text = Entry(cost_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=food_cost_var)
food_cost_text.grid(row=0, column=1, padx= 41 )



drink_cost_label = Label(cost_panel,
                        text="Drink Cost",
                        font=("Dosis", 12, "bold"),
                        bg="azure4",
                        fg="white")
drink_cost_label.grid(row=1, column=0)
drink_cost_text = Entry(cost_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=drink_cost_var)
drink_cost_text.grid(row=1, column=1, padx=41)

dessert_cost_label = Label(cost_panel,
                        text="Dessert Cost",
                        font=("Dosis", 12, "bold"),
                        bg="azure4",
                        fg="white")
dessert_cost_label.grid(row=2, column=0, padx=41)
dessert_cost_text = Entry(cost_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=dessert_cost_var)
dessert_cost_text.grid(row=2, column=1, padx=41)

subtotal_cost_label = Label(cost_panel,
                        text="Subtotal",
                        font=("Dosis", 12, "bold"),
                        bg="azure4",
                        fg="white")
subtotal_cost_label.grid(row=0, column=2, padx=41)
subtotal_cost_text = Entry(cost_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=subtotal_cost_var)
subtotal_cost_text.grid(row=0, column=3, padx=41)

tax_cost_label = Label(cost_panel,
                        text="TAX",
                        font=("Dosis", 12, "bold"),
                        bg="azure4",
                        fg="white")
tax_cost_label.grid(row=1, column=2)
tax_cost_text = Entry(cost_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=taxes_cost_var)
tax_cost_text.grid(row=1, column=3, padx=41)

total_cost_label = Label(cost_panel,
                        text="Total",
                        font=("Dosis", 12, "bold"),
                        bg="azure4",
                        fg="white")
total_cost_label.grid(row=2, column=2, padx=41)
total_cost_text = Entry(cost_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=total_cost_var)
total_cost_text.grid(row=2, column=3, padx=41)

# Butons
buttons = ["total", "invoice", "save", "reset"]
column = 0
for button in buttons:
    button = Button(buttons_panel,
                    text=button.title(),
                    font=("Dosis", 14, "bold"),
                    fg="white",
                    bg="azure4",
                    bd=1,
                    width=9)
    button.grid(row=0,
                column=column)
    column += 1

# Invoice area
invoice_text = Text(invoice_panel,
                    font=("Dosis", 12, "bold"),
                    bd=1,
                    width=42,
                    height=10)
invoice_text.grid(row=0,
                  column=0)

# Calculator
calculator_display = Entry(calculator_panel,
                           font= ("Dosis", 16, "bold"),
                           width=32,
                           bd=1)
calculator_display.grid(row=0, column=0, columnspan=4)

calculator_buttons = ["7", "8", "9", "+",
                      "4", "5", "6", "-",
                      "1", "2", "3", "x",
                      "CE", "Delete", "0", "/"]

stored_buttons = []

my_row = 1
my_column = 0

for button in calculator_buttons:
    button = Button(calculator_panel,
                    text=button.title(),
                    font=("Dosis", 16, "bold"),
                    fg="white",
                    bg="azure4",
                    bd=1,
                    width=8)
    stored_buttons.append(button)

    button.grid(row=my_row,column=my_column)

    if my_column == 3:
        my_row += 1

    my_column += 1

    if my_column == 4:
        my_column = 0

stored_buttons[0].config(command=lambda: click_button("7"))
stored_buttons[1].config(command=lambda: click_button("8"))
stored_buttons[2].config(command=lambda: click_button("9"))
stored_buttons[3].config(command=lambda: click_button("+"))
stored_buttons[4].config(command=lambda: click_button("4"))
stored_buttons[5].config(command=lambda: click_button("5"))
stored_buttons[6].config(command=lambda: click_button("6"))
stored_buttons[7].config(command=lambda: click_button("-"))
stored_buttons[8].config(command=lambda: click_button("1"))
stored_buttons[9].config(command=lambda: click_button("2"))
stored_buttons[10].config(command=lambda: click_button("3"))
stored_buttons[11].config(command=lambda: click_button("*"))
stored_buttons[12].config(command=get_result )
stored_buttons[13].config(command=delete_all)
stored_buttons[14].config(command=lambda: click_button("0"))
stored_buttons[15].config(command=lambda: click_button("/"))




application.mainloop()