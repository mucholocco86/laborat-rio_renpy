"""Standalone Wells SDK window."""

import tkinter as tk

from wells_sdk.ui import build_panel


def main():
    root = tk.Tk()
    root.title("Wells SDK")
    root.geometry("800x470")
    root.minsize(720, 430)
    root.configure(bg="#222222")
    build_panel(root)
    root.mainloop()


if __name__ == "__main__":
    main()

