import tkinter as tk


win = tk.Tk()
win.resizable(True, True)
win.title("Body Mass Index Calculator")


frame = tk.Frame(win)
frame.pack(fill=tk.BOTH)

lbl_name = tk.Label(frame, text="Ad-Soyad: ")
lbl_name.grid(column=0, row=0, padx=5, pady=5)

ent_name = tk.Entry(frame, bd=3, width=20)
ent_name.grid(column=1, row=0, padx=5, pady=5)

lbl_height = tk.Label(frame, text="Boy(m): ")
lbl_height.grid(column=0, row=1, padx=5, pady=5)

ent_height = tk.Entry(frame, bd=3, width=20)
ent_height.grid(column=1, row=1, padx=5, pady=5)

lbl_weight = tk.Label(frame, text="Kilo(kg): ")
lbl_weight.grid(column=0, row=2, padx=5, pady=5)

ent_weight = tk.Entry(frame, bd=3, width=20)
ent_weight.grid(column=1, row=2, padx=5, pady=5)

var = tk.StringVar()
var.set("Vücut Kitle Değeriniz:")
lbl_BMI_result = tk.Label(frame, textvariable=var)
lbl_BMI_result.grid(column=2, row=1, padx=5, pady=5)


def CalculateBMI():
    height = float(ent_height.get())
    weight = float(ent_weight.get())

    height_square = height*height

    mass_index = (weight/height_square)

    print(mass_index)
    return mass_index


def UpdateResultLabel():
    var.set("")
    name = ent_name.get()
    mass_index = CalculateBMI()
    var.set(f"Sayın, {name}. Vücut Kitle Değeriniz: {mass_index}")


btn_calculate = tk.Button(frame, text="Hesapla", command=UpdateResultLabel)
btn_calculate.grid(column=1, row=3, padx=5, pady=5)


win.mainloop()
