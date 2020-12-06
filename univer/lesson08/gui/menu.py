from tkinter import Tk, Menu, filedialog, Listbox, END, BOTH

from ua.python18_10_2020.univer.lesson08.vehicle.vehicles import *




class MainWindow:

    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.root = Tk()
        self.root.title("GUI на Python")
        self.root.geometry("300x250")

        self.file_menu = Menu()
        self.file_menu.add_command(label="New", command=self.new_win)
        self.file_menu.add_command(label="Save", command=self.show_list)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit")

        self.main_menu = Menu()
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.main_menu.add_cascade(label="Edit")
        self.main_menu.add_cascade(label="View")

        self.languages_listbox = Listbox()
        self.languages_listbox.pack(expand=True, fill=BOTH)

        self.root.config(menu=self.main_menu)
        self.root.mainloop()

    def get_list_text_from_file(self,filename):
        arr_text = []
        with open(filename, "r") as file_data:
            for line in file_data:
                arr_text.append(line)
        return arr_text

    def open_file(self):
        filename = filedialog.askopenfilename()
        values = self.get_list_text_from_file(filename)
        for value in values:
            self.languages_listbox.insert(END, value)

    def new_win(self):
        n_win = MainWindow(vehicles)


    def show_list(self):
        self.languages_listbox.delete(0,self.languages_listbox.size())
        for value in vehicles:
            self.languages_listbox.insert(END, value)

if __name__ == '__main__':
    vehicles = [Amphibia(16, 6, 85), Ship(25, 7, 70, 55), BatMobile()]
    main_window = MainWindow(vehicles)