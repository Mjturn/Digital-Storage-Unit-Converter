from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class DigitalStorageUnitConverter:
    def __init__(self):
        root = Tk()
        root.title("Digital Storage Unit Converter")
        root.iconbitmap("images\ssd_icon.ico")
        digital_storage_units = ["Bytes", "Kilobytes(KB)", "Megabytes(MB)", "Gigabytes(GB)", "Terabytes(TB)"]
        self.unit1_value = Entry(root, font=("comic sans", 15), borderwidth=0)
        self.unit1_value.grid(row=0, column=0, sticky="nsew")
        self.unit2_value = Entry(root, font=("comic sans", 15), borderwidth=0)
        self.unit2_value.config(state=DISABLED)
        self.unit2_value.grid(row=0, column=1, sticky="nsew")
        self.unit1 = ttk.Combobox(root, value=digital_storage_units, font=("comic sans", 15))
        self.unit1.current(0)
        self.unit1.grid(row=1, column=0)
        self.unit2 = ttk.Combobox(root, value=digital_storage_units, font=("comic sans", 15))
        self.unit2.current(0)
        self.unit2.grid(row=1, column=1)
        convert_button = Button(root, font=("comic sans", 11), text="Convert", bg="black", fg="white", borderwidth=0, command=self.convert)
        convert_button.grid(row=2, column=0, columnspan=2)
        root.mainloop()

    def convert(self):
        self.unit2_value.config(state=NORMAL)
        self.unit2_value.delete(0, END)
        self.validate()
        if self.unit1.get() == "Bytes" and self.unit2.get() == "Kilobytes(KB)":
            result = int(self.unit1_value.get()) / 1024
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Bytes" and self.unit2.get() == "Megabytes(MB)":
            result = int(self.unit1_value.get()) / pow(1024, 2)
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Bytes" and self.unit2.get() == "Gigabytes(GB)":
            result = int(self.unit1_value.get()) / pow(1024, 3)
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Bytes" and self.unit2.get() == "Terabytes(TB)":
            result = int(self.unit1_value.get()) / pow(1024, 4)
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Kilobytes(KB)" and self.unit2.get() == "Bytes":
            result = int(self.unit1_value.get()) * 1024
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Kilobytes(KB)" and self.unit2.get() == "Megabytes(MB)":
            result = int(self.unit1_value.get()) / 1024
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Kilobytes(KB)" and self.unit2.get() == "Gigabytes(GB)":
            result = int(self.unit1_value.get()) / pow(1024, 2)
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Kilobytes(KB)" and self.unit2.get() == "Terabytes(TB)":
            result = int(self.unit1_value.get()) / pow(1024, 3)
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Megabytes(MB)" and self.unit2.get() == "Bytes":
            result = int(self.unit1_value.get()) * pow(1024, 2)
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Megabytes(MB)" and self.unit2.get() == "Kilobytes(KB)":
            result = int(self.unit1_value.get()) * 1024
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Megabytes(MB)" and self.unit2.get() == "Gigabytes(GB)":
            result = int(self.unit1_value.get()) / 1024
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Megabytes(MB)" and self.unit2.get() == "Terabytes(TB)":
            result = int(self.unit1_value.get()) / pow(1024, 2)
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Gigabytes(GB)" and self.unit2.get() == "Bytes":
            result = int(self.unit1_value.get()) * pow(1024, 3)
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Gigabytes(GB)" and self.unit2.get() == "Kilobytes(KB)":
            result = int(self.unit1_value.get()) * pow(1024, 2)
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Gigabytes(GB)" and self.unit2.get() == "Megabytes(MB)":
            result = int(self.unit1_value.get()) * 1024
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Gigabytes(GB)" and self.unit2.get() == "Terabytes(TB)":
            result = int(self.unit1_value.get()) / 1024
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Terabytes(TB)" and self.unit2.get() == "Bytes":
            result = int(self.unit1_value.get()) * pow(1024, 4)
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Terabytes(TB)" and self.unit2.get() == "Kilobytes(KB)":
            result = int(self.unit1_value.get()) * pow(1024, 3)
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Terabytes(TB)" and self.unit2.get() == "Megabytes(MB)":
            result = int(self.unit1_value.get()) * pow(1024, 2)
            self.unit2_value.insert(0, result)
        elif self.unit1.get() == "Terabytes(TB)" and self.unit2.get() == "Gigabytes(GB)":
            result = int(self.unit1_value.get()) * 1024
            self.unit2_value.insert(0, result)
        self.unit2_value.config(state=DISABLED)

    def validate(self):
        if self.unit1.get() == self.unit2.get():
            messagebox.showerror("Same units", "The same units cannot be converted.")
        if len(self.unit1_value.get()) == 0:
            messagebox.showerror("Empty field", "The field is empty. You need to enter a number in order to convert.")
        try:
            float(self.unit1_value.get())
        except ValueError:
            messagebox.showerror("Not a number", "What you've entered was not a number. Please enter a number.")


window = DigitalStorageUnitConverter()