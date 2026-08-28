# Word Search Generator

A small Python tool that builds a custom word search puzzle and outputs two
print-ready PDFs: a solvable puzzle and a matching answer key.

## What it does

Give it a list of words (organized into categories) and a grid size, and it
will:

1. Place every word into a letter grid, running horizontally, vertically, or
   diagonally.
2. Fill in all the empty squares with random letters so the words blend in.
3. Save two PDF files:
   - **`word_search.pdf`** — the puzzle itself: the letter grid, the title,
     and a page listing all the words to find, grouped by category.
   - **`answers.pdf`** — the same grid, but with every hidden word
     highlighted in gray, for checking your work.

## How to run it

1. Make sure you have the `reportlab` library installed:

   ```
   pip install reportlab
   ```

2. Open `main.py` and run it:

   ```
   python main.py
   ```

3. Look for `word_search.pdf` and `answers.pdf` in the same folder — they'll
   be created (or overwritten) each time you run the script.

## How to make your own puzzle

Everything you need to customize is at the top of `main.py`:

```python
TITLE = "Duan and Song Family Word Search"
SUBTITLE = "Ballet • Hockey • Photography — find every word below (words may run diagonally!)"
SIZE = 10

CATEGORIES = {
    "Family": ["LINA", "WILLIAM", "ALEXANDER", "KAILAI", "NORAH", "KIKO"],
    "Ballet": ["BALLET", "TUTU", "POINTE", "PLIE", "ARABESQUE", "PIROUETTE",
               "BARRE", "LEOTARD", "DANCER", "JETE"],
    "Hockey": ["HOCKEY", "PUCK", "SKATES", "STICK", "GOALIE", "RINK",
               "SLAPSHOT", "PENALTY", "JERSEY", "HELMET"],
    "Photography": ["CAMERA", "LENS", "APERTURE", "SHUTTER", "FOCUS",
                     "PORTRAIT", "TRIPOD", "ZOOM", "FILTER", "FLASH"],
}
```

**To make your own version:**

- **Change `TITLE` and `SUBTITLE`** to whatever you'd like printed at the top
  of the puzzle page.
- **Change `SIZE`** to make the grid bigger or smaller (this is the number of
  rows/columns — `10` means a 10x10 grid). A bigger grid gives the generator
  more room to place long words and hide them well; a smaller grid makes for
  an easier, faster puzzle.
- **Change `CATEGORIES`** to swap in your own words. Each entry is a category
  name paired with a list of words, in ALL CAPS:

  ```python
  CATEGORIES = {
      "Category Name": ["WORD1", "WORD2", "WORD3"],
      "Another Category": ["WORDA", "WORDB"],
  }
  ```

  You can add as many categories and words as you like, and the word list
  page will automatically lay them out side-by-side by category. Keep in
  mind that longer words and larger word lists need a bigger `SIZE` to fit
  comfortably — if the generator seems to be struggling or taking a while,
  try increasing `SIZE`.

Once you've made your edits, just run `python main.py` again to generate a
fresh `word_search.pdf` and `answers.pdf` with your new puzzle.

## Files in this project

- `main.py` — the file you edit and run; holds your title, size, and word
  categories.
- `generator.py` — builds the letter grid and figures out where each word
  goes.
- `pdf_builder.py` — turns the grid into the two formatted PDF files.
