import tkinter as tk
import tkinter.messagebox as mb
from kubik import Kubik


def main():
    root = tk.Tk()
    app = Kubik(root)

    root.mainloop()


if __name__ == "__main__":
    main()
