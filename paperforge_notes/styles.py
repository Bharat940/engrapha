from reportlab.lib.styles import ParagraphStyle as S

BODY_ST = S("Body")
SECT_ST = S("Section")
CODE_ST = S("Code")
COVER_H1 = S("Cover_H1", fontSize=24, alignment=1, spaceAfter=20)
COVER_H2 = S("Cover_H2", fontSize=18, alignment=1, spaceAfter=20)
COVER_SUB = S("Cover_Sub", fontSize=14, alignment=1, spaceAfter=10)
CHAP_H1 = S("Chap_H1", fontSize=20, alignment=0, spaceAfter=15)
H1 = S("Heading1", fontSize=16, spaceBefore=12, spaceAfter=6)
H2 = S("Heading2", fontSize=14, spaceBefore=10, spaceAfter=6)
H3 = S("Heading3", fontSize=12, spaceBefore=8, spaceAfter=4)
H4 = S("Heading4", fontSize=11, spaceBefore=6, spaceAfter=4)
H5 = S("Heading5", fontSize=10, spaceBefore=4, spaceAfter=2)
H6 = S("Heading6", fontSize=10, spaceBefore=4, spaceAfter=2)
TOC_H1 = S("TOC_Heading1", fontSize=14, spaceBefore=6)
TOC_H2 = S("TOC_Heading2", fontSize=12, leftIndent=20, spaceBefore=4)
TOC_H3 = S("TOC_Heading3", fontSize=11, leftIndent=40, spaceBefore=2)
BULLET_ST = S("Bullet", leftIndent=20, spaceBefore=2, spaceAfter=2)

# Backward-compatible style aliases used by the theme application layer.
PART_ST = H1
CHAP_ST = CHAP_H1
SUB_ST = H3
DEF_ST = BODY_ST
TIP_ST = BODY_ST
NOTE_ST = BODY_ST
CAP_ST = BODY_ST
