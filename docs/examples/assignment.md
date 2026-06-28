# Example: Assignment

Assignment sheet with question numbers, code blocks, marking rubrics, and MCQs.

```python title="assignment.py"
import engrapha_notes as en
import engrapha_diagrams as ed

en.set_theme(en.LIGHT)
en.set_global_header(center="Data Structures — Assignment 3")

en.cover_card(
    "Assignment 3: Trees and Graphs",
    "Data Structures — Session 2026",
)

en.qbox("1. Draw a BST and its AVL rotation.")
en.answer(
    "Perform a single right rotation on the unbalanced node. "
    "The former left child becomes the new root. "
    "Height reduces by one."
)

en.chap_box("Programming Question")

en.qbox(
    "2. Implement a Trie supporting insert(), search(), and startsWith() "
    "in Python. Discuss time/space tradeoffs in a comment block."
)

en.code_block("""
class TrieNode:
    __slots__ = ("children", "is_end")
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
""", lang="python")

en.mcq(
    "3. Correct BST worst-case height (N nodes)?",
    ["N", "N/2", "log N", "N²"],
    correct_index=0,
)

en.build_doc("assignment.pdf")
```

![Screenshot placeholder](../assets/screenshots/notes_assignment.png)

