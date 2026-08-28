"""
Example "run me" script. Edit the WORDS / TITLE / SIZE below and run:

    python main.py

This is the file you'll actually run in VS Code (Run > Run Without
Debugging, or the ▷ button top-right of the editor).
"""

from generator import generate
from pdf_builder import build_pdf

TITLE = "Duan and Song Family Word Search"
SUBTITLE = "Ballet • Hockey • Photography — find every word below (words may run diagonally!)"
SIZE = 25

CATEGORIES = {
    "Family": ["LINA", "WILLIAM", "ALEXANDER", "KAILAI", "NORAH","KIKO"],
    "Ballet": ["BALLET", "TUTU", "POINTE", "PLIE", "ARABESQUE", "PIROUETTE",
               "BARRE", "LEOTARD", "DANCER", "JETE"],
    "Hockey": ["HOCKEY", "PUCK", "SKATES", "STICK", "GOALIE", "RINK",
               "SLAPSHOT", "PENALTY", "JERSEY", "HELMET"],
    "Photography": ["CAMERA", "LENS", "APERTURE", "SHUTTER", "FOCUS",
                     "PORTRAIT", "TRIPOD", "ZOOM", "FILTER", "FLASH"],
}
"""
    CATEGORIES = {
        "Family": ["LINA", "WILLIAM", "ALEXANDER", "KAILAI", "NORAH","KIKO"],
    }
"""

def main():
    words = []
    for cat, ws in CATEGORIES.items():
        for w in ws:
            words.append(w)

    

    grid, wordInfo, valid = generate(words, size=SIZE)

    if(valid):
        build_pdf(grid, wordInfo, CATEGORIES, TITLE, subtitle=SUBTITLE, output_path="word_search.pdf")
    else:
        print("need to change size")




if __name__ == "__main__":
    main()
