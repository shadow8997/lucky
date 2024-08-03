import tkinter as tk
from tkinter import simpledialog, messagebox

class NameApp:
    def __init__(self, root):
        self.names_list = []

        self.root = root
        self.root.title("Name List App")

        self.add_button = tk.Button(root, text="Add Name", command=self.add_name)
        self.add_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", wraplength=300, justify="left")
        self.result_label.pack(pady=10)

    def add_name(self):
        name = simpledialog.askstring("Input", "Enter a name:")
        if name:
            self.names_list.append(name.strip())
            self.update_names_display()

    def update_names_display(self):
        formatted_names = ', '.join(f'"{name}"' for name in self.names_list)
        self.result_label.config(text=formatted_names)

if __name__ == "__main__":
    root = tk.Tk()
    app = NameApp(root)
    root.mainloop()