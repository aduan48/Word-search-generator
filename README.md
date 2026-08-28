# Word Search Generator

A small Python project that generates a word-search puzzle grid, checks its
own work, and renders a print-ready PDF (puzzle page + answer key).

## Files

- `generator.py` — the actual word-placement logic (pure functions, no I/O).
- `pdf_builder.py` — turns a generated grid into a PDF using `reportlab`.
- `main.py` — the script you run. Edit the word list / title here.
- `test_generator.py` — automated tests (`pytest`) that sanity-check the generator.
- `requirements.txt` — the two packages you need.

## Setup in VS Code

1. Install [VS Code](https://code.visualstudio.com/) and the **Python** extension
   (Extensions icon in the sidebar → search "Python" → the Microsoft one → Install).
2. Install Python 3.10+ if you don't have it (`python3 --version` in a terminal to check).
3. Open this folder in VS Code: `File → Open Folder…`
4. Open a terminal inside VS Code: `` Ctrl+` `` (backtick), or `Terminal → New Terminal`.
5. Create and activate a virtual environment (keeps this project's packages separate
   from everything else on your machine):

   ```bash
   python3 -m venv venv
   # Mac/Linux:
   source venv/bin/activate
   # Windows (PowerShell):
   venv\Scripts\Activate.ps1
   ```

   VS Code should pop up a prompt asking "Select venv as the workspace interpreter?" —
   say yes. If it doesn't, press `Ctrl+Shift+P` → "Python: Select Interpreter" → pick
   the one inside `venv`.

6. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running it

Open `main.py` and click the ▷ **Run** button in the top-right corner (or
`Ctrl+F5`, or type `python main.py` in the terminal). It will:

1. Generate the grid.
2. Print a warning if any word didn't fit.
3. Run a self-check (`verify()`) confirming every placed word is actually
   spelled out correctly in the grid.
4. Write `wordsearch.pdf` into the project folder.

Change `CATEGORIES`, `TITLE`, `SIZE`, or `SEED` at the top of `main.py` and
re-run any time — that's the whole "make your own" workflow.

## Testing ("back-testing" the generator)

There's no historical price data to backtest here — but the equivalent idea
for a generator like this is: *run it many times, with different inputs, and
confirm it never produces a broken puzzle.* That's what `test_generator.py`
does. Run it with:

```bash
pytest
```

or, in VS Code: click the **Testing** icon in the left sidebar (looks like a
flask) → "Configure Python Tests" → choose `pytest` → point it at this
folder. Tests will show up individually with green/red checkmarks, and you
can click any one to debug it with breakpoints.

The tests cover things like: every word actually gets placed, every placed
word is genuinely readable in the final grid (not just "recorded" as
placed), the same seed always produces the same puzzle, a too-small grid
fails gracefully instead of crashing, and it works across easy/medium/hard
direction sets.

If you add features (e.g. a "no two words overlap" mode, or a French/Spanish
letter set), add a new `test_*` function alongside the existing ones — that's
how you keep the generator from silently breaking as you change it.

## Debugging in VS Code

Set a breakpoint by clicking in the left gutter next to any line (e.g. inside
`can_place()` in `generator.py`), then press `F5` (or the Run/Debug icon) to
run `main.py` under the debugger. Execution will pause at the breakpoint and
you can inspect variables in the sidebar, step line-by-line (`F10`), or step
into a function call (`F11`).
