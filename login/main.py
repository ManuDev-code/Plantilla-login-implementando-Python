import tkinter as tk
import login_ui

def main():
    root = tk.Tk()
    app = login_ui.LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()