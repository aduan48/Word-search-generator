"""
Renders a generate.py result into a print-ready PDF: puzzle page + answer key.
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black

LIGHT_GRAY = HexColor("#e3e3e3")
MID_GRAY = HexColor("#9a9a9a")


def build_pdf(result, categories, output_path, title, subtitle):
    """
    result: the dict returned by generator.generate()
    categories: dict of category_name -> [words], used only for the
        printed word list (order/grouping is cosmetic).
    output_path: where to write the .pdf
    """
    grid = result["grid"]
    size = result["size"]
    placements = result["placements"]

    page_w, page_h = letter
    margin = 34
    top_gap = 96
    bottom_gap = 210

    grid_area_w = page_w - 2 * margin
    grid_area_h = page_h - top_gap - bottom_gap
    cell = min(grid_area_w, grid_area_h) / size
    grid_w = cell * size
    grid_left = (page_w - grid_w) / 2
    grid_top_y = page_h - top_gap

    def cell_center(row, col):
        x = grid_left + col * cell + cell / 2
        y = grid_top_y - row * cell - cell / 2
        return x, y

    def draw_title_block(c, title_text, subtitle_text):
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(black)
        c.drawCentredString(page_w / 2, page_h - 40, title_text)
        c.setFont("Helvetica", 11)
        c.setFillColor(MID_GRAY)
        c.drawCentredString(page_w / 2, page_h - 58, subtitle_text)
        c.setFillColor(black)

    def draw_grid(c, highlight_words=None):
        highlight_cells = set()
        if highlight_words:
            for w in highlight_words:
                info = placements[w]
                r, cc, dr, dc = info["row"], info["col"], info["dr"], info["dc"]
                for i in range(info["len"]):
                    highlight_cells.add((r + dr * i, cc + dc * i))

        c.setLineWidth(1.4)
        c.setStrokeColor(black)
        c.rect(grid_left, grid_top_y - grid_w, grid_w, grid_w, stroke=1, fill=0)

        font_size = cell * 0.62
        c.setFont("Courier-Bold", font_size)

        for r in range(size):
            for col in range(size):
                x0 = grid_left + col * cell
                y0 = grid_top_y - (r + 1) * cell
                if (r, col) in highlight_cells:
                    c.setFillColor(LIGHT_GRAY)
                    c.rect(x0, y0, cell, cell, stroke=0, fill=1)
                c.setStrokeColor(MID_GRAY)
                c.setLineWidth(0.4)
                c.rect(x0, y0, cell, cell, stroke=1, fill=0)

                c.setFillColor(black)
                cx, cy = cell_center(r, col)
                c.drawCentredString(cx, cy - font_size * 0.36, grid[r][col])

    def draw_word_list(c, top_y):
        x = margin
        y = top_y
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x, y, "Find these words:")
        y -= 20

        col_width = (page_w - 2 * margin) / max(len(categories), 1)
        col_index = 0
        for category, words in categories.items():
            col_x = margin + col_index * col_width
            cy = y
            c.setFont("Helvetica-Bold", 10.5)
            c.setFillColor(black)
            c.drawString(col_x, cy, category)
            cy -= 14
            c.setFont("Helvetica", 10)
            for w in words:
                c.drawString(col_x, cy, w.title())
                cy -= 13
            col_index += 1

    c = canvas.Canvas(output_path, pagesize=letter)

    # Page 1: puzzle
    draw_title_block(c, title, subtitle)
    draw_grid(c)
    draw_word_list(c, page_h - top_gap - grid_w - 26)
    c.showPage()

    # Page 2: answer key
    draw_title_block(c, "Answer Key", f"Solutions for {title}")
    draw_grid(c, highlight_words=list(placements.keys()))
    draw_word_list(c, page_h - top_gap - grid_w - 26)
    c.showPage()

    c.save()
