import tkinter as tk
from tkinter import ttk
from word_ladder_game import WordLadderGame

if __name__ == "__main__":
    root = tk.Tk()
  
    game = WordLadderGame(root)
    root.mainloop()
