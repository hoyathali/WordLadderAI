import tkinter as tk
from tkinter import ttk
from collections import deque
from bfs_impl_search import bfs_impl_search
from dfs_impl_search import dfs_impl_search

class WordLadderGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Ladder Game")

        # Set window size to half the screen
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Styling
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12))
        style.configure("TLabel", font=("Helvetica", 12))

        # UI Components
        self.word_label = ttk.Label(master, text="Enter start word:")
        self.word_label.pack()

        self.word_entry = ttk.Entry(master)
        self.word_entry.pack()

        self.target_label = ttk.Label(master, text="Enter target word:")
        self.target_label.pack()

        self.target_entry = ttk.Entry(master)
        self.target_entry.pack()

        self.bfs_button = ttk.Button(master, text="BFS", command=self.bfs)
        self.bfs_button.pack(side=tk.LEFT, padx=10)

        self.dfs_button = ttk.Button(master, text="DFS", command=self.dfs)
        self.dfs_button.pack(side=tk.LEFT, padx=10)

        self.bfs_impl_button = ttk.Button(master, text="BFS Impl", command=self.bfs_impl)
        self.bfs_impl_button.pack(side=tk.RIGHT, padx=10)

        self.dfs_impl_button = ttk.Button(master, text="DFS Impl", command=self.dfs_impl)
        self.dfs_impl_button.pack(side=tk.RIGHT, padx=10)

        self.result_label = ttk.Label(master, text="")
        self.result_label.pack()

        self.expanded_label = ttk.Label(master, text="Nodes Expanded: 0")
        self.expanded_label.pack()

    def bfs(self):
        self.reset_display()
        self.start_word = self.word_entry.get().lower()
        self.target_word = self.target_entry.get().lower()

        word_list = self.load_word_list()
        result, nodes_expanded = self.find_word_ladder(self.bfs_search, word_list)
        self.display_result(result)
        self.update_expanded_label(nodes_expanded)

    def dfs(self):
        self.reset_display()
        self.start_word = self.word_entry.get().lower()
        self.target_word = self.target_entry.get().lower()

        word_list = self.load_word_list()
        result, nodes_expanded = self.find_word_ladder(self.dfs_search, word_list)
        self.display_result(result)
        self.update_expanded_label(nodes_expanded)

    def bfs_impl(self):
        self.reset_display()
        word_list = self.load_word_list()
        result, nodes_expanded = self.find_word_ladder(self.bfs_impl_search, word_list)
        self.display_result(result)
        self.update_expanded_label(nodes_expanded)

    def dfs_impl(self):
        self.reset_display()
        word_list = self.load_word_list()
        result, nodes_expanded = self.find_word_ladder(self.dfs_impl_search, word_list)
        self.display_result(result)
        self.update_expanded_label(nodes_expanded)

    def reset_display(self):
        self.result_label.config(text="")
        self.expanded_label.config(text="Nodes Expanded: 0")

    def find_word_ladder(self, search_algorithm, word_list):
        if self.start_word not in word_list or self.target_word not in word_list:
            return "Start and target words must be in the word list.", 0

        result, nodes_expanded = search_algorithm(word_list)
        return result, nodes_expanded

    def bfs_search(self, word_list):
        visited = set()
        visited.add(self.start_word)

        if self.start_word == self.target_word:
            return [self.start_word], 0

        queue = deque([(self.start_word, [self.start_word])])
        nodes_expanded = 0
        while queue:
            current_word, path = queue.popleft()
            nodes_expanded += 1

            for neighbor in self.get_neighbors(current_word, word_list):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))
                    visited.add(neighbor)

                    if neighbor == self.target_word:
                        return new_path, nodes_expanded

        return None, nodes_expanded


    def dfs_search(self, word_list):
        visited = set()
        visited.add(self.start_word)

        if self.start_word == self.target_word:
            return [self.start_word], 0

        stack = [(self.start_word, [self.start_word])]
        nodes_expanded = 0
        while stack:
            current_word, path = stack.pop()
            nodes_expanded += 1

            for neighbor in self.get_neighbors(current_word, word_list):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path))
                    visited.add(neighbor)

                    if neighbor == self.target_word:
                        return new_path, nodes_expanded

        return None, nodes_expanded


    def bfs_impl_search(self, word_list):
        return bfs_impl_search(word_list)

    def dfs_impl_search(self, word_list):
        return dfs_impl_search(word_list)

    def update_expanded_label(self, nodes_expanded):
        self.expanded_label.config(text=f"Nodes Expanded: {nodes_expanded}")

    def get_neighbors(self, word, word_list):
        neighbors = []
        for i in range(len(word)):
            for j in range(97, 123):  # ASCII values for lowercase letters
                new_word = word[:i] + chr(j) + word[i + 1:]
                if new_word in word_list and new_word != word:
                    neighbors.append(new_word)
        return neighbors

    def display_result(self, result):
        if isinstance(result, list):
            self.result_label.config(text=f"Word Ladder: {' -> '.join(result)}")
        else:
            self.result_label.config(text=result)

    def load_word_list(self, filename="5letterwords.txt"):
        try:
            with open(filename, "r") as file:
                word_list = set(word.strip().lower() for word in file)
            return word_list
        except FileNotFoundError:
            return set()
