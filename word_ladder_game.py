import tkinter as tk
from tkinter import ttk
from collections import deque
from bfs_impl_search import bfs_impl_search
from dfs_impl_search import dfs_impl_search

class WordLadderGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Ladder Game")

        # Set window size
        window_width = 800
        window_height = 600
        x_position = (master.winfo_screenwidth() - window_width) // 2
        y_position = (master.winfo_screenheight() - window_height) // 2
        master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Styling
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12))
        style.configure("TLabel", font=("Helvetica", 12))

        # UI Components
        self.canvas_frame = tk.Frame(master)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.word_label = ttk.Label(self.canvas_frame, text="Enter start word:")
        self.word_label.grid(row=0, column=0, padx=5, pady=5)

        self.word_var = tk.StringVar()
        self.word_entry = ttk.Entry(self.canvas_frame, textvariable=self.word_var)
        self.word_entry.grid(row=0, column=1, padx=5, pady=5)

        self.word_listbox_start = tk.Listbox(self.canvas_frame, selectmode=tk.SINGLE)
        self.word_listbox_start.grid(row=0, column=2, padx=5, pady=5)

        self.target_label = ttk.Label(self.canvas_frame, text="Enter target word:")
        self.target_label.grid(row=1, column=0, padx=5, pady=5)

        self.target_var = tk.StringVar()
        self.target_entry = ttk.Entry(self.canvas_frame, textvariable=self.target_var)
        self.target_entry.grid(row=1, column=1, padx=5, pady=5)

        self.word_listbox_end = tk.Listbox(self.canvas_frame, selectmode=tk.SINGLE)
        self.word_listbox_end.grid(row=1, column=2, padx=5, pady=5)

        self.bfs_button = ttk.Button(self.canvas_frame, text="BFS", command=self.bfs)
        self.bfs_button.grid(row=2, column=0, pady=10)

        self.dfs_button = ttk.Button(self.canvas_frame, text="DFS", command=self.dfs)
        self.dfs_button.grid(row=2, column=1, pady=10)

        self.bfs_impl_button = ttk.Button(self.canvas_frame, text="BFS Impl", command=self.bfs_impl)
        self.bfs_impl_button.grid(row=2, column=2, pady=10)

        self.dfs_impl_button = ttk.Button(self.canvas_frame, text="DFS Impl", command=self.dfs_impl)
        self.dfs_impl_button.grid(row=2, column=3, pady=10)

        self.result_label = ttk.Label(self.canvas_frame, text="")
        self.result_label.grid(row=3, column=0, columnspan=4, pady=5)

        self.expanded_label = ttk.Label(self.canvas_frame, text="Nodes Expanded: 0")
        self.expanded_label.grid(row=4, column=0, columnspan=4, pady=5)

        

        self.canvas_scrollbar = ttk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL)
        self.canvas = tk.Canvas(self.canvas_frame, yscrollcommand=self.canvas_scrollbar.set, bg="white")
        self.canvas.grid(row=5, column=0, columnspan=4, pady=10, sticky=tk.NSEW)
        self.canvas_scrollbar.config(command=self.canvas.yview)
        self.canvas_scrollbar.grid(row=5, column=4, sticky=tk.NS)

        # Load word list from file
        self.word_list = self.load_word_list()
        self.populate_word_listbox()

        # Autocomplete for word entry fields
        self.word_entry.bind("<KeyRelease>", self.autocomplete_start)
        self.target_entry.bind("<KeyRelease>", self.autocomplete_end)
        self.fit_to_screen()
    def fit_to_screen(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = int(screen_width * 0.3)
        window_height = int(screen_height * 0.8)

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


    def autocomplete_start(self, event):
        # Autocomplete words based on user input for start word
        current_entry = event.widget.get().lower()
        matching_words = [word for word in self.word_list if word.startswith(current_entry)]
        self.word_listbox_start.delete(0, tk.END)
        for word in matching_words:
            self.word_listbox_start.insert(tk.END, word)

    def autocomplete_end(self, event):
        # Autocomplete words based on user input for end word
        current_entry = event.widget.get().lower()
        matching_words = [word for word in self.word_list if word.startswith(current_entry)]
        self.word_listbox_end.delete(0, tk.END)
        for word in matching_words:
            self.word_listbox_end.insert(tk.END, word)

    def populate_word_listbox(self):
        # Display the word list in the listboxes
        for word in self.word_list:
            self.word_listbox_start.insert(tk.END, word)
            self.word_listbox_end.insert(tk.END, word)

    def bfs(self):
        self.reset_display()
        self.start_word = self.word_var.get().lower()
        self.target_word = self.target_var.get().lower()

        word_list = self.word_list
        result, nodes_expanded = self.find_word_ladder(self.bfs_search, word_list)
        self.display_result(result, nodes_expanded)
        self.draw_word_ladder(result)

    def dfs(self):
        self.reset_display()
        self.start_word = self.word_var.get().lower()
        self.target_word = self.target_var.get().lower()

        word_list = self.word_list
        result, nodes_expanded = self.find_word_ladder(self.dfs_search, word_list)
        self.display_result(result, nodes_expanded)
        self.draw_word_ladder(result)

    def bfs_impl(self):
        self.reset_display()
        word_list = self.word_list
        result, nodes_expanded = self.find_word_ladder(self.bfs_impl_search, word_list)
        self.display_result(result, nodes_expanded)
        self.draw_word_ladder(result)

    def dfs_impl(self):
        self.reset_display()
        word_list = self.word_list
        result, nodes_expanded = self.find_word_ladder(self.dfs_impl_search, word_list)
        self.display_result(result, nodes_expanded)
        self.draw_word_ladder(result)

    def reset_display(self):
        self.result_label.config(text="")
        self.expanded_label.config(text="Nodes Expanded: 0")
        self.canvas.delete("all")

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

    def display_result(self, result, nodes_expanded):
        if isinstance(result, list):
            # Update the expanded label
            self.update_expanded_label(nodes_expanded)
            # Draw the word ladder
            self.draw_word_ladder(result)
        else:
            # Display error message as a note
            self.result_label.config(text=f"Note: {result}")


    def create_word_ladder(self, result):
        word_ladder = ""
        for i in range(len(result) - 1):
            word_ladder += result[i] + " -> "
        word_ladder += result[-1]
        return word_ladder

    def load_word_list(self, filename="5letterwords.txt"):
        try:
            with open(filename, "r") as file:
                word_list = set(word.strip().lower() for word in file)
            return word_list
        except FileNotFoundError:
            return set()

    def draw_word_ladder(self, result):
        if not result:
            return

        word_count = len(result)
        cell_height = 40  # Fixed height for ladder cells
        canvas_width = self.canvas_frame.winfo_width() - 100  # Adjusted width
        canvas_height = cell_height * word_count
        line_spacing = canvas_height / word_count

        x_start = 20  # Adjusted starting position for error message and expanded label
        y_start = 0

        for i, word in enumerate(result):
            x = x_start
            y = y_start + i * (cell_height + line_spacing)

            if i == 0:
                color = "green"  # Color start word green
            elif i == word_count - 1:
                color = "red"  # Color end word red
            else:
                color = "black"

            # Draw the word
            text_id = self.canvas.create_text(x, y, text=word, fill=color, anchor="w")

            # Draw horizontal line
            if i < word_count - 1:
                line_y = y + cell_height
                self.canvas.create_line(x_start, line_y, canvas_width, line_y, fill="black", width=2)

        # Update canvas dimensions and scroll region
        self.canvas.update_idletasks()
        canvas_bbox = self.canvas.bbox("all")
        canvas_width = canvas_bbox[2] - canvas_bbox[0]
        canvas_height = canvas_bbox[3] - canvas_bbox[1]
        self.canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))



