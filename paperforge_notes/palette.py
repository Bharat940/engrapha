"""
paperforge_notes.palette -- Shared dark-theme color palette for ReportLab notes PDFs.

Import everything you need:
    from paperforge_notes.palette import BG, CYAN, GREEN, YELLOW, WHITE, TABLE_HDR, ...
Or simply use:
    import paperforge_notes as pn   # pn.BG, pn.CYAN, etc.
"""

from reportlab.lib import colors

# -- Page background & cards --------------------------------------------------
BG = colors.HexColor("#0d1117")
CARD_DARK = colors.HexColor("#161b22")
CARD_MID = colors.HexColor("#1c2333")

# -- Accent colors ------------------------------------------------------------
CYAN = colors.HexColor("#79c0ff")
GREEN = colors.HexColor("#3fb950")
GREEN_CARD = colors.HexColor("#0d2119")
YELLOW = colors.HexColor("#d29922")
YELLOW_CARD = colors.HexColor("#1f1a0a")
RED = colors.HexColor("#f85149")
RED_CARD = colors.HexColor("#1e0d0d")
PURPLE = colors.HexColor("#bc8cff")
PURPLE_CARD = colors.HexColor("#180d2b")

# -- Text ---------------------------------------------------------------------
WHITE = colors.HexColor("#f0f6fc")
WHITE_DIM = colors.HexColor("#9da7b3")
CODE_GREEN = colors.HexColor("#7ee787")

# -- Table --------------------------------------------------------------------
TABLE_HDR = colors.HexColor("#1f6feb")
TABLE_R1 = colors.HexColor("#161b22")
TABLE_R2 = colors.HexColor("#1b2230")
TABLE_BDR = colors.HexColor("#30363d")
CODE_BG = colors.HexColor("#161b22")

__all__ = [
    "BG",
    "CARD_DARK",
    "CARD_MID",
    "CYAN",
    "GREEN",
    "GREEN_CARD",
    "YELLOW",
    "YELLOW_CARD",
    "RED",
    "RED_CARD",
    "PURPLE",
    "PURPLE_CARD",
    "WHITE",
    "WHITE_DIM",
    "CODE_GREEN",
    "TABLE_HDR",
    "TABLE_R1",
    "TABLE_R2",
    "TABLE_BDR",
    "CODE_BG",
]
