
# Word Ladder Game

## Overview

The Word Ladder Game is a classic word puzzle where the challenge is to transform one word into another, changing only one letter at a time, with the constraint that every intermediate step is also a valid word. This implementation provides a graphical user interface (GUI) for users to play and visualize the game.

## Getting Started

To run the Word Ladder Game, you need to have Python and the Tkinter library installed. If not, you can install Tkinter using:

```bash
pip install tk
```

After installing Tkinter, you can run the game with:

```bash
python main.py
```

## How to Play

1. **Enter Start and Target Words:** Input the starting and target words in the provided text fields.

2. **Choose Search Algorithm:** Click the "BFS" button to use Breadth-First Search or the "DFS" button to use Depth-First Search. Additionally, there are "BFS Impl" and "DFS Impl" buttons that are intended for students to implement their custom search algorithms.

3. **View Results:** The game will display the word ladder from the start word to the target word. The "Nodes Expanded" label shows the number of nodes visited during the search.

4. ![image](https://github.com/hoyathali/WordTreeAI/assets/33727918/61ff2863-90e4-4e04-b121-a234b22db36b)


5. **Try Different Words:** You can enter new start and target words and choose a different search algorithm.

## Custom Search Algorithm Implementation

### Implementing `bfs_impl_search` and `dfs_impl_search`

For students working on the custom search algorithms, they need to implement the following functions:

- `bfs_impl_search(word_list)`: Perform Breadth-First Search on the given `word_list` to find the word ladder. Return the word ladder and the number of nodes expanded.
- Please check bfs_impl_search.py for more details

- `dfs_impl_search(word_list)`: Perform Depth-First Search on the given `word_list` to find the word ladder. Return the word ladder and the number of nodes expanded.
- Please check dfs_impl_search.py for more details
- 
### Tips for Implementation

- **Useful Structures:** Utilize Python data structures like queues and stacks for BFS and DFS, respectively.

- **Efficient Word Generation:** When generating neighbours of a word, ensure efficiency by considering only valid words in the dictionary.

- **Visited Nodes:** Keep track of visited nodes to avoid redundant exploration.

- **Termination Condition:** Implement a termination condition when the target word is found.

## Example

Here is an example structure for your `bfs_impl_search` and `dfs_impl_search`:

```python
def bfs_impl_search(self,word_list):
    # Implement BFS here
    pass

def dfs_impl_search(self,word_list):
    # Implement DFS here
    pass
```

Feel free to explore and experiment with different strategies to optimize the search process.

## Acknowledgments

This Word Ladder Game is inspired by classic word puzzles. Special thanks to the developers and contributors who made the project possible.

---

