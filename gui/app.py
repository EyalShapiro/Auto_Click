import tkinter as tk
from tkinter import ttk
from auto_clicker import AutoClicker


class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Clicker")

        self.time_click = tk.DoubleVar(value=0.1)
        self.loc = tk.StringVar(value="RIGHT")
        self.limit = tk.IntVar(value=10)

        self.create_widgets()

    def create_widgets(self):
        # Entry for time interval
        time_label = ttk.Label(self.root, text="Click interval time:")
        time_label.grid(row=0, column=0, sticky="w")
        time_entry = ttk.Entry(self.root, textvariable=self.time_click)
        time_entry.grid(row=0, column=1, padx=5, pady=5)

        # Combobox for click location
        loc_label = ttk.Label(self.root, text="Click location:")
        loc_label.grid(row=1, column=0, sticky="w")
        loc_combobox = ttk.Combobox(
            self.root, textvariable=self.loc, values=["LEFT", "MIDDLE", "RIGHT"]
        )
        loc_combobox.grid(row=1, column=1, padx=5, pady=5)

        # Entry for click limit
        limit_label = ttk.Label(self.root, text="Click limits:")
        limit_label.grid(row=2, column=0, sticky="w")
        limit_entry = ttk.Entry(self.root, textvariable=self.limit)
        limit_entry.grid(row=2, column=1, padx=5, pady=5)

        # Button to start clicking
        start_button = ttk.Button(
            self.root, text="Start Clicking", command=self.start_clicking
        )
        start_button.grid(row=3, columnspan=2, pady=10)

    def start_clicking(self):
        time_click = self.time_click.get()
        loc = self.loc.get()
        limit = self.limit.get()

        auto_clicker = AutoClicker(time_click, loc, limit)
        auto_clicker.start_clicking()

    def start(self):
        self.root.mainloop()


def main():
    root = tk.Tk()
    app = AutoClickerApp(root)
    app.start()


if __name__ == "__main__":
    main()
