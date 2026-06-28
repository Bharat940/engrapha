"""
Computer Architecture (IT-404) -- Unit II Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes with vector diagrams.
Run: python ca_unit2_notes.py
Output: CA_Unit2_Notes.pdf
"""

from __future__ import annotations

import engrapha_notes as en
import engrapha_diagrams as ed
from reportlab.platypus import Paragraph, Table, TableStyle

# =============================================================================
#  THEME SETUP
# =============================================================================
en.set_story([])
en.set_theme(en.CATPPUCCIN_MOCHA)

diag_theme = ed.DiagramTheme.from_notes_theme(en.get_theme())


# =============================================================================
#  CUSTOM CPU DIAGRAM NODE DRAWERS
# =============================================================================
def draw_register(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    # Rounded rectangle representing a register, split into 4 fields
    diag._add(
        S.rounded_rect(
            cx - w / 2,
            cy - h / 2,
            w,
            h,
            rx=3,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    for i in range(1, 4):
        x = cx - w / 2 + i * (w / 4)
        diag._add(S.solid_line(x, cy - h / 2, x, cy + h / 2, color=stroke, width=0.8))


def draw_cu(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    # Control unit / sequencer block with internal partition lines
    diag._add(
        S.rounded_rect(
            cx - w / 2,
            cy - h / 2,
            w,
            h,
            rx=4,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    diag._add(
        S.solid_line(
            cx - w / 2, cy - h / 6, cx + w / 2, cy - h / 6, color=stroke, width=1.0
        )
    )
    for i in range(1, 6):
        x = cx - w / 2 + i * (w / 6)
        diag._add(S.solid_line(x, cy - h / 2, x, cy - h / 6, color=stroke, width=0.6))


def draw_flags(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    # Status flags register with Z, N, C, V cells
    diag._add(
        S.rounded_rect(
            cx - w / 2,
            cy - h / 2,
            w,
            h,
            rx=3,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    for i in range(1, 4):
        x = cx - w / 2 + i * (w / 4)
        diag._add(S.solid_line(x, cy - h / 2, x, cy + h / 2, color=stroke, width=0.8))
    t = diag.theme
    flag_chars = ["Z", "N", "C", "V"]
    for i, char in enumerate(flag_chars):
        fx = cx - w / 2 + (i + 0.5) * (w / 4)
        diag._add(
            S.label(
                fx,
                cy - 3.0,
                char,
                font=t.font_name_bold,
                size=7.0,
                color=stroke,
                anchor="middle",
            )
        )


# =============================================================================

# =============================================================================
#  COVER PAGE
# =============================================================================
en.bookmark("Cover Page")
en.suppress_footer(page_only=True)
en.sp(28)
t = Table(
    [
        [Paragraph("COMPUTER ARCHITECTURE", en.COVER_H1)],
        [Paragraph("Unit II -- Complete Exam Notes", en.COVER_H2)],
    ],
    colWidths=[en.CW],
)
t.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), en.get_theme().rl(en.get_theme().surface)),
            ("TOPPADDING", (0, 0), (-1, -1), 22),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 22),
            ("LEFTPADDING", (0, 0), (-1, -1), 20),
            ("RIGHTPADDING", (0, 0), (-1, -1), 20),
            ("BOX", (0, 0), (-1, -1), 2.5, en.get_theme().rl(en.get_theme().accent)),
        ]
    )
)
en.add(t)
en.sp(14)
en.add(
    Paragraph(
        "Prepared by: Bharat Dangi  |  Subject Code: IT-404  |  UIT-RGPV (Autonomous) Bhopal",
        en.COVER_SUB,
    )
)
en.add(Paragraph("Semester IV  |  Based on University Syllabus 2024-25", en.COVER_SUB))
en.sp(10)
en.rule(en.get_theme().rl(en.get_theme().accent), 1.5)
en.sp(8)

en.info_table(
    ["Topic", "Coverage"],
    [
        [
            "2.1 Fixed-Point Representation",
            "Integer representation, sign-magnitude, 1's complement, 2's complement, range",
        ],
        ["2.2 Integer Arithmetic -- Negation", "Negation in all three representations"],
        [
            "2.3 Integer Arithmetic -- Addition and Subtraction",
            "Signed addition, subtraction, overflow detection",
        ],
        [
            "2.4 Integer Arithmetic -- Multiplication",
            "Unsigned, signed (Booth's algorithm), hardware",
        ],
        [
            "2.5 Integer Arithmetic -- Division",
            "Restoring and non-restoring division algorithms",
        ],
        [
            "2.6 Floating-Point Representation",
            "IEEE 754 single and double precision, special values",
        ],
        [
            "2.7 Floating-Point Arithmetic",
            "Addition, subtraction, multiplication, division steps",
        ],
        ["2.8 Hardwired vs Microprogrammed CU", "Design comparison, trade-offs"],
        [
            "2.9 Control Memory and Microprogram Sequence",
            "Control memory, microinstruction formats, sequencer",
        ],
        ["2.10 Quick Revision Summary", "Key formulas, tables, and exam flashcards"],
    ],
)
en.br()
en.suppress_footer(page_only=True)
en.toc()

# =============================================================================
#  UNIT DIVIDER
# =============================================================================
en.footer(left="IT-404: Computer Architecture", right="Unit II Notes", show_page_num=True)
en.part_box("UNIT II -- ALU, NUMBER REPRESENTATIONS AND CONTROL UNIT")

# =============================================================================
#  2.1  FIXED-POINT REPRESENTATION
# =============================================================================
en.chap_box("2.1  Fixed-Point Representation")
en.section("Integer Representation")
en.definition(
    "<b>Fixed-Point Representation:</b> A method of encoding numbers in binary "
    "where the binary point (decimal point equivalent) is fixed at a specific "
    "position -- usually to the right of the least significant bit for integers. "
    "All digits are whole-number digits. The hardware can represent both "
    "<b>unsigned</b> (non-negative) and <b>signed</b> (positive and negative) integers."
)
en.body(
    "For an <b>n-bit word</b>, unsigned integers span 0 to 2<super>n</super> - 1. "
    "Signed integers require one bit (the MSB) to encode the sign. Three common "
    "signed representations are: Sign-Magnitude, 1's Complement, and 2's Complement."
)

en.section("Sign-Magnitude Representation")
en.definition(
    "<b>Sign-Magnitude:</b> The MSB is the sign bit (0 = positive, 1 = negative). "
    "The remaining n-1 bits represent the magnitude (absolute value). "
    "This is the most intuitive representation but has two zeros (+0 and -0) "
    "and requires special hardware for arithmetic."
)
en.code_block("""
 SIGN-MAGNITUDE (8-bit examples):
 ======================================================
 +7  =  0 000 0111    (sign bit 0, magnitude 7)
 -7  =  1 000 0111    (sign bit 1, magnitude 7)
 +0  =  0 000 0000
 -0  =  1 000 0000    (two representations of zero!)

 Range for n bits: -(2^(n-1) - 1)  to  +(2^(n-1) - 1)
 8-bit range: -127 to +127

 ADDITION RULE:
   Same sign: add magnitudes, keep sign.
   Different sign: subtract smaller magnitude from larger, keep sign of larger.
""")

en.section("1's Complement Representation")
en.definition(
    "<b>1's Complement:</b> Positive numbers are represented in standard binary. "
    "A negative number is formed by inverting ALL bits of the positive counterpart "
    "(bitwise NOT). Still has two zeros (+0 = 00...0 and -0 = 11...1). "
    "Addition requires an <b>end-around carry</b>: if there is a carry out of the "
    "MSB, it is added back to the LSB."
)
en.code_block("""
 1'S COMPLEMENT (8-bit examples):
 ======================================================
 +7  =  0000 0111
 -7  =  1111 1000    (invert all bits of +7)
 +0  =  0000 0000
 -0  =  1111 1111    (two zeros again!)

 Range for n bits: -(2^(n-1) - 1)  to  +(2^(n-1) - 1)
 8-bit range: -127 to +127

 ADDITION WITH END-AROUND CARRY:
 (+6) + (-4) = 0000 0110 + 1111 1011
                         = 1 0000 0001
                         ^-- carry out -> add to LSB
                           = 0000 0010 = +2  (correct!)
""")

en.section("2's Complement Representation")
en.definition(
    "<b>2's Complement:</b> The universally used representation for signed integers "
    "in modern computers. A negative number is formed by inverting all bits of the "
    "positive counterpart and then adding 1. There is only ONE zero. "
    "Addition and subtraction use the same hardware (no special cases). "
    "The MSB has weight -2<super>n-1</super> instead of +2<super>n-1</super>."
)
en.code_block("""
 2'S COMPLEMENT (8-bit examples):
 ======================================================
 +7  =  0000 0111
 -7  =  1111 1001    (invert all bits: 1111 1000, add 1: 1111 1001)
 +1  =  0000 0001
 -1  =  1111 1111
  0  =  0000 0000    (only one zero!)
 -128=  1000 0000    (most negative: no positive counterpart!)

 Range for n bits: -2^(n-1)  to  +(2^(n-1) - 1)
 8-bit range: -128 to +127   (one extra negative number)
 16-bit range: -32,768 to +32,767
 32-bit range: -2,147,483,648 to +2,147,483,647

 VALUE FORMULA:
   Value = -a_(n-1) * 2^(n-1) + sum(a_i * 2^i, i=0 to n-2)
   Example: 1011 = -1*8 + 0*4 + 1*2 + 1*1 = -8 + 3 = -5
""")

en.section("Representation Comparison")
en.info_table(
    ["Property", "Sign-Magnitude", "1's Complement", "2's Complement"],
    [
        [
            "Positive numbers",
            "Same as unsigned",
            "Same as unsigned",
            "Same as unsigned",
        ],
        [
            "Negation rule",
            "Flip MSB only",
            "Invert all bits",
            "Invert all bits + add 1",
        ],
        ["Number of zeros", "Two (+0 and -0)", "Two (+0 and -0)", "One (0000...0)"],
        [
            "n-bit range",
            "-(2^(n-1)-1) to +(2^(n-1)-1)",
            "-(2^(n-1)-1) to +(2^(n-1)-1)",
            "-2^(n-1) to +(2^(n-1)-1)",
        ],
        ["8-bit range", "-127 to +127", "-127 to +127", "-128 to +127"],
        [
            "Addition hardware",
            "Complex (sign check)",
            "Simple + end-around carry",
            "Simple (no special case)",
        ],
        ["Overflow detection", "Complex", "Moderate", "C_in XOR C_out of MSB"],
        [
            "Used in practice",
            "Floating-point sign",
            "Network checksums (TCP/IP)",
            "All modern computers (ALU)",
        ],
    ],
)

# Diagram: number line showing all three representations for 3-bit
en.subsection("Visual: 3-bit Signed Number Line")
en.code_block("""
 3-BIT NUMBER LINE COMPARISON:
 ======================================================
 Bit Pattern | Unsigned | Sign-Mag | 1's Comp | 2's Comp
 ------------|----------|----------|----------|----------
   000       |    0     |    +0    |    +0    |    0
   001       |    1     |    +1    |    +1    |   +1
   010       |    2     |    +2    |    +2    |   +2
   011       |    3     |    +3    |    +3    |   +3
   100       |    4     |    -0    |    -3    |   -4
   101       |    5     |    -1    |    -2    |   -3
   110       |    6     |    -2    |    -1    |   -2
   111       |    7     |    -3    |    -0    |   -1

 Note: 2's complement has no -0 and has an extra -4 (100).
""")

en.tip(
    "2's complement is THE standard for modern computers. "
    "Negation: invert all bits and add 1. Range: -2^(n-1) to +2^(n-1)-1. "
    "2's complement has one more negative number than positive. "
    "Overflow: carry into MSB != carry out of MSB."
)
en.br()

# =============================================================================
#  2.2  NEGATION
# =============================================================================
en.chap_box("2.2  Integer Arithmetic -- Negation")
en.section("Negation in Each Representation")
en.info_table(
    ["Representation", "Negation Rule", "Example: Negate +5 (0101)", "Special Case"],
    [
        [
            "Sign-Magnitude",
            "Flip the sign bit (MSB) only.",
            "+5 = 0101 -> -5 = 1101",
            "Negating -0 (1000) gives +0 (0000) -- both are zero.",
        ],
        [
            "1's Complement",
            "Invert ALL bits (bitwise NOT).",
            "+5 = 0101 -> NOT = 1010 = -5",
            "Negating -0 (1111) gives +0 (0000) -- OK.",
        ],
        [
            "2's Complement",
            "Invert all bits then add 1.",
            "+5 = 0101 -> NOT = 1010 -> +1 = 1011 = -5",
            "Negating -128 (1000 0000) overflows: result is still 1000 0000. "
            "This is the only overflow case in negation.",
        ],
    ],
)
en.code_block("""
 2'S COMPLEMENT NEGATION WORKED EXAMPLES (8-bit):
 ======================================================
 Negate +23 (0001 0111):
   Step 1 Invert: 1110 1000
   Step 2 Add 1:  1110 1001  = -23 (check: -128+64+32+8+1 = -23 yes!)

 Negate -50 (1100 1110):
   Step 1 Invert: 0011 0001
   Step 2 Add 1:  0011 0010  = +50 (check: 32+16+2 = 50 yes!)

 Negate -128 (1000 0000):
   Step 1 Invert: 0111 1111
   Step 2 Add 1:  1000 0000  = -128 AGAIN (overflow -- no +128 in 8-bit!)

 SHORTCUT: Scan from LSB, copy bits up to and including the first 1,
           then invert all remaining bits.
   Example: 0110 1100 -> scan right: copy 00, copy 1, invert rest:
            copy 00, copy 1 -> 1001 0100
""")
en.tip(
    "2's complement negation: invert + add 1. "
    "Shortcut: copy LSBs up to first 1 (inclusive), flip everything to the left. "
    "Only overflow: negating the most negative number (-2^(n-1))."
)
en.br()

# =============================================================================
#  2.3  ADDITION AND SUBTRACTION
# =============================================================================
en.chap_box("2.3  Integer Arithmetic -- Addition and Subtraction")
en.section("2's Complement Addition")
en.definition(
    "<b>2's Complement Addition:</b> Simply add the two n-bit numbers using "
    "standard binary addition. Ignore any carry out of the MSB (for n-bit result). "
    "This works for all combinations of positive and negative operands -- "
    "no sign checking is required."
)
en.code_block("""
 2'S COMPLEMENT ADDITION CASES (8-bit):
 ======================================================
 Case 1: Both positive (+30 + +20 = +50)
   0001 1110 (+30)
 + 0001 0100 (+20)
 -----------
   0011 0010 (+50)   Carry out = 0, V = 0  (no overflow)

 Case 2: Positive + Negative (+50 + -20 = +30)
   0011 0010 (+50)
 + 1110 1100 (-20)
 -----------
 1 0001 1110 (+30)   Carry out = 1, IGNORE (n-bit result correct)

 Case 3: Both negative (-30 + -20 = -50)
   1110 0010 (-30)
 + 1110 1100 (-20)
 -----------
 1 1100 1110 (-50)   Carry out = 1, IGNORE

 Case 4: OVERFLOW (+100 + +50 = +150 -- overflow in 8-bit!)
   0110 0100 (+100)
 + 0011 0010 (+50)
 -----------
   1001 0110 (-106)  Carry in to MSB = 0, Carry out of MSB = 0 but
                     result sign changed -> V = 1 (OVERFLOW!)
   Note: +150 > +127 (max 8-bit signed), so result wraps negative.
""")

en.section("Overflow Detection")
en.definition(
    "<b>Overflow:</b> Occurs when the result of a signed addition exceeds the "
    "representable range. For n-bit 2's complement, overflow can be detected by: "
    "V = C<sub>n-1</sub> XOR C<sub>n</sub>, where C<sub>n</sub> is the carry out "
    "of the MSB and C<sub>n-1</sub> is the carry into the MSB. "
    "Overflow ONLY happens when both operands have the same sign and the result "
    "has the opposite sign."
)
en.info_table(
    ["Operand A sign", "Operand B sign", "Result sign", "Overflow?"],
    [
        ["+", "+", "+", "No"],
        ["+", "+", "-", "YES -- positive + positive = negative (wrong!)"],
        ["+", "-", "either", "No (magnitude decreases)"],
        ["-", "+", "either", "No (magnitude decreases)"],
        ["-", "-", "-", "No"],
        ["-", "-", "+", "YES -- negative + negative = positive (wrong!)"],
    ],
)

en.section("2's Complement Subtraction")
en.definition(
    "<b>Subtraction via Addition:</b> A - B is computed as A + (-B) = A + (NOT B + 1). "
    "This means the hardware needs only an adder plus an inverter (XOR gate) -- "
    "no separate subtractor is required. This is the key advantage of 2's complement."
)
en.code_block("""
 SUBTRACTION HARDWARE (n-bit 2's complement):
 ======================================================
 A - B  =  A + (NOT B) + 1

 Hardware: Set the carry-in (Cin) = 1 and invert B (using XOR or MUX).
   When SUB control signal = 0: perform A + B  (normal addition, Cin=0)
   When SUB control signal = 1: perform A + NOT(B) + 1  (subtraction, Cin=1)

 EXAMPLE: 15 - 6 = 9  (8-bit)
   A = 0000 1111  (+15)
   B = 0000 0110  (+6)
   NOT B = 1111 1001
   A + NOT(B) + 1:
     0000 1111
   + 1111 1001
   +         1
   -----------
   1 0000 1001   carry out = 1 (ignore), result = 0000 1001 = +9 (correct!)
""")

# Adder/Subtractor flowchart
fc_addsub = ed.Flowchart(
    width=en.CW,
    height=240,
    theme=diag_theme,
    caption="Fig 1: 2's Complement Adder-Subtractor hardware operation",
)
fc_addsub.terminal("start", "Operation Request")
fc_addsub.decision("sub", "SUB control = 1?")
fc_addsub.process("prep_add", "Cin = 0, B unchanged (ADD)")
fc_addsub.process("prep_sub", "Cin = 1, B inverted via XOR (SUBTRACT)")
fc_addsub.process(
    "adder", "n-bit Ripple Carry / CLA Adder computes S = A + B_eff + Cin"
)
fc_addsub.process("flags", "Set flags: Z, N, C (carry out), V (C_n XOR C_(n-1))")
fc_addsub.terminal("done", "Result S available, flags latched")

fc_addsub.edge("start", "sub")
fc_addsub.edge("sub", "prep_add", branch="no")
fc_addsub.edge("sub", "prep_sub", branch="yes")
fc_addsub.edge("prep_add", "adder")
fc_addsub.edge("prep_sub", "adder")
fc_addsub.edge("adder", "flags")
fc_addsub.edge("flags", "done")
en.story.extend(fc_addsub.as_flowable())

en.tip(
    "A - B = A + NOT(B) + 1 in 2's complement. "
    "One adder serves both addition and subtraction (just invert B and set Cin=1). "
    "Overflow detection: V = carry_into_MSB XOR carry_out_of_MSB. "
    "Unsigned overflow = carry out. Signed overflow = V flag."
)
en.br()

# =============================================================================
#  2.4  MULTIPLICATION
# =============================================================================
en.chap_box("2.4  Integer Arithmetic -- Multiplication")
en.section("Unsigned Binary Multiplication")
en.definition(
    "<b>Binary Multiplication:</b> Similar to decimal long multiplication. "
    "For each bit of the multiplier (from LSB to MSB): if the bit is 1, add the "
    "multiplicand shifted left by the bit's position; if the bit is 0, add zero. "
    "The sum of all partial products is the result. An n-bit x n-bit multiplication "
    "produces a 2n-bit result."
)
en.code_block("""
 UNSIGNED MULTIPLICATION EXAMPLE (4-bit):
 ======================================================
 Multiplicand (M) = 1011  (11)
 Multiplier   (Q) = 1101  (13)
 Expected result  = 143 = 1000 1111

 Partial products:
   1011  x  1  (Q bit 0 = 1, shift 0)  ->  0000 1011
   1011  x  0  (Q bit 1 = 0, shift 1)  ->  0000 0000
   1011  x  1  (Q bit 2 = 1, shift 2)  ->  0010 1100
   1011  x  1  (Q bit 3 = 1, shift 3)  ->  0101 1000

   Sum: 0000 1011 + 0000 0000 + 0010 1100 + 0101 1000
      = 1000 1111  = 143  (correct!)

 HARDWARE (sequential approach):
   Accumulator A (n bits, init=0)
   Multiplier register Q (n bits, loaded with multiplier)
   Multiplicand register M (n bits)
   Counter (n bits, counts down)

   Each step: if Q[0]=1, A <- A + M; then shift right (A,Q) by 1.
   After n steps, (A,Q) holds the 2n-bit product.
""")

en.section("Booth's Algorithm (Signed Multiplication)")
en.definition(
    "<b>Booth's Algorithm:</b> An efficient algorithm for multiplying two signed "
    "2's complement integers. It handles both positive and negative multipliers "
    "uniformly. Instead of examining one multiplier bit at a time, Booth's algorithm "
    "examines pairs of bits (current bit Q[i] and previous bit Q[i-1]) to decide "
    "whether to add M, subtract M, or do nothing -- reducing the number of additions "
    "for multipliers with consecutive 1s."
)

en.subsection("Booth's Encoding Table")
en.info_table(
    ["Q[i] (current)", "Q[i-1] (previous)", "Operation", "Reason"],
    [
        ["0", "0", "No operation (shift only)", "Middle of a string of 0s"],
        ["0", "1", "A <- A + M (add multiplicand)", "End of a string of 1s"],
        ["1", "0", "A <- A - M (subtract multiplicand)", "Start of a string of 1s"],
        ["1", "1", "No operation (shift only)", "Middle of a string of 1s"],
    ],
)

en.code_block("""
 BOOTH'S ALGORITHM WORKED EXAMPLE (4-bit):
 ======================================================
 Multiplicand M = 0011  (+3)
 Multiplier   Q = 1101  (-3)  [Q_(-1) = 0 initially]
 Expected result = -9  =  1111 0111

 Registers: A (accumulator, 4 bits, init=0000), Q (multiplier), Q_(-1) (init=0)

 Step | Q[0] Q[-1] | Operation          | A        | Q    | Q[-1]
 -----|------------|--------------------|-----------|----- |------
  0   |            | Initial            | 0000     | 1101 |  0
  1   | 1    0     | A <- A - M (sub)   | 1101     | 1101 |  0
      |            | Arithmetic Shift R | 1110     | 1110 |  1
  2   | 0    1     | A <- A + M (add)   | 0001     | 1110 |  1
      |            | Arithmetic Shift R | 0000     | 1111 |  0
  3   | 1    0     | A <- A - M (sub)   | 1101     | 1111 |  0
      |            | Arithmetic Shift R | 1110     | 1111 |  1
  4   | 1    1     | No op (shift only) | 1110     | 1111 |  1
      |            | Arithmetic Shift R | 1111     | 0111 |  1

 Result: (A, Q) = 1111 0111 = -9  (correct! 3 x -3 = -9)

 KEY RULE: Arithmetic Right Shift preserves the sign bit.
           Shift right: MSB of A is replicated, not filled with 0.
""")

# Booth's algorithm flowchart
fc_booth = ed.Flowchart(
    width=en.CW,
    height=380,
    theme=diag_theme,
    caption="Fig 2: Booth's Algorithm flowchart for signed 2's complement multiplication",
)
fc_booth.terminal("start", "START: Load M, Q, Set A=0, Q[-1]=0, Count=n")
fc_booth.decision("q0q1", "Q[0], Q[-1] pair?")
fc_booth.process("add_m", "A <- A + M  (01: end of ones string)")
fc_booth.process("sub_m", "A <- A - M  (10: start of ones string)")
fc_booth.process("no_op", "No operation  (00 or 11)")
fc_booth.process("shift", "Arithmetic Right Shift (A, Q, Q[-1]) by 1")
fc_booth.process("decr", "Count <- Count - 1")
fc_booth.decision("done", "Count == 0?")
fc_booth.terminal("end", "END: Product in (A, Q) -- 2n bits")

fc_booth.edge("start", "q0q1")
fc_booth.edge("q0q1", "add_m", branch="01")
fc_booth.edge("q0q1", "sub_m", branch="10")
fc_booth.edge("q0q1", "no_op", branch="00/11")
fc_booth.edge("add_m", "shift")
fc_booth.edge("sub_m", "shift")
fc_booth.edge("no_op", "shift")
fc_booth.edge("shift", "decr")
fc_booth.edge("decr", "done")
fc_booth.edge("done", "end", branch="yes")
fc_booth.edge("done", "q0q1", branch="no", orthogonal=True)
en.story.extend(fc_booth.as_flowable())

en.tip(
    "Booth's: examine Q[0] and Q[-1]. 01=add, 10=subtract, 00/11=no-op. "
    "Always arithmetic right shift after each step. "
    "Works for any signed 2's complement operands. "
    "n steps for n-bit multiplication. Product in (A,Q) = 2n bits."
)
en.br()

# =============================================================================
#  2.5  DIVISION
# =============================================================================
en.chap_box("2.5  Integer Arithmetic -- Division")
en.section("Overview")
en.definition(
    "<b>Binary Division:</b> Computes quotient Q and remainder R such that "
    "Dividend = Divisor x Q + R. Hardware division is performed by a sequential "
    "algorithm that either restores or does not restore partial remainders. "
    "Two common algorithms: <b>Restoring Division</b> and <b>Non-Restoring Division</b>."
)

en.section("Restoring Division Algorithm (Unsigned)")
en.body(
    "In restoring division, the partial remainder is maintained non-negative at each step. "
    "If after subtracting the divisor the partial remainder goes negative, the divisor is "
    "restored (added back) and a quotient bit of 0 is recorded."
)
en.code_block("""
 RESTORING DIVISION ALGORITHM:
 ======================================================
 Registers: A (partial remainder, n bits, init=0)
            Q (dividend / quotient, n bits)
            M (divisor, n bits)
            Count = n (number of steps)

 Each step:
   1. Shift left (A, Q) by 1 bit
   2. A <- A - M  (trial subtraction)
   3. If A < 0 (MSB = 1): quotient bit Q[0] = 0, RESTORE: A <- A + M
      If A >= 0 (MSB = 0): quotient bit Q[0] = 1

 EXAMPLE: 7 / 2  (4-bit, expect Q=3, R=1)
 M = 0010, Dividend = 0111 loaded into Q, A = 0000

 Step | Shift (A,Q) | A-M        | Q[0] | Restore? | A after
 -----|-------------|------------|------|----------|--------
  1   | 0000 1110   | 0000-0010  | 1    | no (>=0) | 1110 -> A=0000, Q bit=1 wait
      | A=0000 Q=1110 -> A=A-M=1110 neg -> restore, Q[0]=0
      | A=0000 again
  2   | 0000 1100 -> A=A-M=1110 neg -> restore, Q[0]=0
  3   | 0000 1000 -> A=A-M=0110 pos, Q[0]=1
  4   | 0110 0011 -> A=A-M=0100 pos, Q[0]=1

 Result: Q = 0011 = 3 (quotient), A = 0001 = 1 (remainder)  Correct!
""")

en.section("Non-Restoring Division Algorithm")
en.definition(
    "<b>Non-Restoring Division:</b> Avoids the restoration step by alternating "
    "between addition and subtraction based on the sign of the partial remainder. "
    "If A is negative, shift left and ADD divisor. If A is non-negative, shift left "
    "and SUBTRACT divisor. This is faster than restoring division (fewer operations)."
)
en.code_block("""
 NON-RESTORING DIVISION RULES:
 ======================================================
 If A >= 0: Shift left (A,Q), then A <- A - M, Q[0] <- 1
 If A <  0: Shift left (A,Q), then A <- A + M, Q[0] <- 0

 After n steps: if A < 0, add one final correction: A <- A + M

 COMPARISON: Restoring vs Non-Restoring:
 -----------------------------------------
 | Property      | Restoring     | Non-Restoring   |
 |---------------|---------------|-----------------|
 | Steps         | n steps       | n steps         |
 | Operations/step| Sub + maybe Add| Sub or Add     |
 | Complexity    | Simpler logic | Slightly complex|
 | Speed         | Slower        | Faster          |
 | Correction    | Restore if neg| Final correction|
""")

fc_div = ed.Flowchart(
    width=en.CW,
    height=300,
    theme=diag_theme,
    caption="Fig 3: Restoring division flowchart",
)
fc_div.terminal("start", "Load: A=0, Q=Dividend, M=Divisor, Count=n")
fc_div.process("shift", "Shift Left (A, Q) by 1 bit")
fc_div.process("sub", "A <- A - M  (trial subtraction)")
fc_div.decision("neg", "A < 0 (MSB=1)?")
fc_div.process("restore", "Restore: A <- A + M; Q[0] <- 0")
fc_div.process("keep", "Keep:  Q[0] <- 1")
fc_div.process("decr", "Count <- Count - 1")
fc_div.decision("done", "Count == 0?")
fc_div.terminal("end", "Quotient in Q, Remainder in A")

fc_div.edge("start", "shift")
fc_div.edge("shift", "sub")
fc_div.edge("sub", "neg")
fc_div.edge("neg", "restore", branch="yes")
fc_div.edge("neg", "keep", branch="no")
fc_div.edge("restore", "decr")
fc_div.edge("keep", "decr")
fc_div.edge("decr", "done")
fc_div.edge("done", "end", branch="yes")
fc_div.edge("done", "shift", branch="no", orthogonal=True)
en.story.extend(fc_div.as_flowable())

en.tip(
    "Restoring: subtract, if negative restore (add back) and record 0, else record 1. "
    "Non-restoring: if A>=0 subtract and record 1; if A<0 add and record 0. "
    "Both take n steps for n-bit division. Product = Quotient * Divisor + Remainder."
)
en.br()

# =============================================================================
#  2.6  FLOATING-POINT REPRESENTATION
# =============================================================================
en.chap_box("2.6  Floating-Point Representation")
en.section("Why Floating-Point?")
en.definition(
    "<b>Floating-Point Representation:</b> A method for encoding real numbers "
    "(with fractional parts and very large or very small magnitudes) in binary. "
    "A floating-point number is represented as: <b>(-1)<super>S</super> x M x 2<super>E</super></b> "
    "where S is the sign, M is the mantissa (significand), and E is the exponent. "
    "The standard is <b>IEEE 754</b>, universally adopted in modern hardware."
)

en.section("IEEE 754 Single Precision (32-bit)")
en.packet_format(
    "IEEE 754 Single Precision (32 bits): Sign(1) | Exponent(8) | Mantissa(23)",
    [
        ("S", 1),
        ("Exponent (Biased, 8 bits)", 8),
        ("Mantissa / Fraction (23 bits)", 23),
    ],
    bit_ruler=True,
)
en.code_block("""
 IEEE 754 SINGLE PRECISION DETAILS:
 ======================================================
 Field        | Bits | Description
 -------------|------|--------------------------------------------
 Sign (S)     |  1   | 0 = positive, 1 = negative
 Exponent (E) |  8   | Stored as BIASED exponent: stored = actual + 127
              |      | Range of stored: 1 to 254 (00000001 to 11111110)
              |      | 00000000 (0) and 11111111 (255) are special
 Mantissa (M) | 23   | Fractional part of normalised significand
              |      | Implied leading 1: actual value = 1.MMMMM...

 VALUE FORMULA (normalised):
   Value = (-1)^S  x  1.Mantissa  x  2^(Stored_Exponent - 127)

 EXAMPLE: Represent -12.5 in IEEE 754 single precision.
   Step 1: Sign bit S = 1 (negative)
   Step 2: Convert 12.5 to binary: 1100.1 = 1.1001 x 2^3
   Step 3: Exponent = 3, stored exponent = 3 + 127 = 130 = 1000 0010
   Step 4: Mantissa = 1001 (the bits after the leading 1)
           Fill to 23 bits: 1001 0000 0000 0000 0000 000

   Result: 1 | 10000010 | 10010000000000000000000
           = C1 48 00 00  (hex)

 PRECISION: ~7 significant decimal digits.
 RANGE: approx 1.18 x 10^-38  to  3.4 x 10^38
""")

en.section("IEEE 754 Double Precision (64-bit)")
en.packet_format(
    "IEEE 754 Double Precision (64 bits): Sign(1) | Exponent(11) | Mantissa(52)",
    [
        ("S", 1),
        ("Exponent (Biased, 11 bits)", 11),
        ("Mantissa / Fraction (52 bits, shown as 20)", 20),
    ],
    bit_ruler=True,
)
en.code_block("""
 IEEE 754 DOUBLE PRECISION DETAILS:
 ======================================================
 Sign:     1 bit
 Exponent: 11 bits, bias = 1023  (stored = actual + 1023)
           Range of stored: 1 to 2046
 Mantissa: 52 bits (implied leading 1)

 VALUE FORMULA:
   Value = (-1)^S  x  1.Mantissa  x  2^(Stored_Exponent - 1023)

 PRECISION: ~15-16 significant decimal digits.
 RANGE: approx 2.2 x 10^-308  to  1.8 x 10^308
""")

en.section("Special IEEE 754 Values")
en.info_table(
    ["Exponent (stored)", "Mantissa", "Value", "Meaning"],
    [
        ["0 (all zeros)", "0 (all zeros)", "+0 or -0", "Positive/negative zero"],
        [
            "0 (all zeros)",
            "Non-zero",
            "(-1)^S x 0.Mantissa x 2^(-126)",
            "Denormalized (subnormal) number -- no leading 1",
        ],
        [
            "255 (all ones)",
            "0 (all zeros)",
            "+INF or -INF",
            "Positive/negative infinity (overflow)",
        ],
        ["255 (all ones)", "Non-zero", "NaN", "Not a Number (e.g., 0/0, sqrt(-1))"],
        ["1 to 254", "Any", "(-1)^S x 1.Mantissa x 2^(E-127)", "Normal number"],
    ],
)
en.info_table(
    ["Format", "Sign", "Exponent", "Mantissa", "Bias", "Range (approx)", "Precision"],
    [
        [
            "Single (float)",
            "1 bit",
            "8 bits",
            "23 bits",
            "127",
            "+-3.4 x 10^38",
            "~7 decimal digits",
        ],
        [
            "Double (double)",
            "1 bit",
            "11 bits",
            "52 bits",
            "1023",
            "+-1.8 x 10^308",
            "~15 decimal digits",
        ],
        [
            "Half (FP16)",
            "1 bit",
            "5 bits",
            "10 bits",
            "15",
            "+-65504",
            "~3 decimal digits",
        ],
    ],
)
en.tip(
    "IEEE 754 single: 1 sign + 8 exponent (bias 127) + 23 mantissa = 32 bits. "
    "Implied leading 1 (normalized). "
    "Special: E=0,M=0 -> zero; E=255,M=0 -> inf; E=255,M!=0 -> NaN. "
    "Value = (-1)^S x 1.M x 2^(E-127)."
)
en.br()

# =============================================================================
#  2.7  FLOATING-POINT ARITHMETIC
# =============================================================================
en.chap_box("2.7  Floating-Point Arithmetic")
en.section("Floating-Point Addition and Subtraction")
en.definition(
    "<b>FP Addition/Subtraction Algorithm:</b> Floating-point addition and subtraction "
    "require aligning the exponents before performing the mantissa operation. "
    "The steps are: (1) Check for zeros, (2) Align exponents, (3) Add/subtract "
    "mantissas, (4) Normalize the result, (5) Round and check for overflow/underflow."
)
en.code_block("""
 FLOATING-POINT ADDITION ALGORITHM:
 ======================================================
 Input: A = (-1)^Sa x Ma x 2^Ea,  B = (-1)^Sb x Mb x 2^Eb

 Step 1: Handle special cases (zero, infinity, NaN).

 Step 2: ALIGN EXPONENTS (denormalize the smaller number)
   If Ea > Eb: shift Mb right by (Ea - Eb) positions, set Eb = Ea
   If Eb > Ea: shift Ma right by (Eb - Ea) positions, set Ea = Eb
   (The number with the smaller exponent loses precision on alignment)

 Step 3: ADD OR SUBTRACT MANTISSAS
   If Sa == Sb: M_result = Ma + Mb (same sign, add)
   If Sa != Sb: M_result = Ma - Mb (different signs, subtract)
               Result sign = sign of the larger magnitude operand

 Step 4: NORMALIZE THE RESULT
   If result has form 1X.XXXX (overflow of mantissa): shift right 1 and Exp++
   If result has form 0.0XXXX (leading zeros): shift left until 1.XXXX and Exp--
   Repeat until form is 1.XXXX (normalized)

 Step 5: ROUND to fit in 23 (or 52) mantissa bits.
   Round to nearest even (IEEE default), round up, round down, or truncate.

 Step 6: CHECK FOR OVERFLOW/UNDERFLOW
   If Exp > 254 (single): result = +/- INF (overflow)
   If Exp < 1   (single): result = 0 or denormal (underflow)

 EXAMPLE: 0.5 + 0.4375  (in single precision concepts)
   A = 1.000 x 2^(-1)  (0.5)
   B = 1.110 x 2^(-2)  (0.4375 = 7/16)

   Align: shift B right by 1: B = 0.111 x 2^(-1)
   Add:   1.000 + 0.111 = 1.111
   Normalize: already normalized: 1.111 x 2^(-1)
   Result = 0.9375  (correct! 0.5 + 0.4375 = 0.9375)
""")

en.section("Floating-Point Multiplication")
en.definition(
    "<b>FP Multiplication:</b> Multiply the mantissas and add the exponents. "
    "The exponent sum must be corrected for the bias (subtract bias once). "
    "Normalize and round the result."
)
en.code_block("""
 FLOATING-POINT MULTIPLICATION:
 ======================================================
 A = (-1)^Sa x 1.Ma x 2^(Ea-bias)
 B = (-1)^Sb x 1.Mb x 2^(Eb-bias)

 A x B = (-1)^(Sa XOR Sb)  x  (1.Ma x 1.Mb)  x  2^((Ea+Eb)-2*bias)

 Steps:
   1. Result sign = Sa XOR Sb
   2. Result exponent (stored) = Ea + Eb - bias  (add stored exponents, subtract bias)
   3. Result mantissa = 1.Ma x 1.Mb  (multiply two 24-bit numbers -> 48-bit product)
   4. Normalize: if product has form 1X.XXXX, shift right 1 and Exp++
   5. Round to 23 bits, check overflow/underflow

 EXAMPLE (single precision):
   A = 0.5  = 1.000 x 2^(-1), stored Ea = 126
   B = 2.0  = 1.000 x 2^(+1), stored Eb = 128
   Sign = 0 (positive)
   Stored Exp = 126 + 128 - 127 = 127  -> actual exponent = 0
   Mantissa = 1.000 x 1.000 = 1.000
   Result = 1.000 x 2^0 = 1.0  (correct! 0.5 x 2.0 = 1.0)
""")

en.section("Floating-Point Division")
en.code_block("""
 FLOATING-POINT DIVISION:
 ======================================================
 A / B = (-1)^(Sa XOR Sb)  x  (1.Ma / 1.Mb)  x  2^((Ea-Eb)+bias)

 Steps:
   1. Result sign = Sa XOR Sb
   2. Result exponent (stored) = Ea - Eb + bias  (subtract stored exponents, add bias)
   3. Divide mantissas: 1.Ma / 1.Mb  (use binary long division)
   4. Normalize, round, check overflow/underflow.

 GUARD, ROUND, STICKY BITS (for rounding):
   To improve rounding accuracy, hardware keeps 3 extra bits beyond the 23 mantissa bits:
   Guard bit:  first bit shifted out
   Round bit:  second bit shifted out
   Sticky bit: OR of all remaining bits shifted out (1 if any 1 was lost)
   IEEE 754 round-to-nearest-even uses these to decide rounding direction.
""")

# FP arithmetic flowchart
fc_fp = ed.Flowchart(
    width=en.CW,
    height=300,
    theme=diag_theme,
    caption="Fig 4: IEEE 754 floating-point addition / subtraction algorithm",
)
fc_fp.terminal("start", "FP ADD / SUB: inputs A and B")
fc_fp.decision("special", "Special values? (0, INF, NaN)")
fc_fp.process("handle_sp", "Handle special case and return result")
fc_fp.process("align", "Align exponents: shift smaller mantissa right")
fc_fp.process("compute", "Add or subtract mantissas based on signs")
fc_fp.process("normalize", "Normalize: shift until form 1.XXXX, adjust exponent")
fc_fp.process("round_step", "Round to 23 bits (GRS bits)")
fc_fp.decision("ovflw", "Exponent overflow or underflow?")
fc_fp.process("set_inf", "Set +/-INF or 0 / denormal")
fc_fp.terminal("end", "Return IEEE 754 result")

fc_fp.edge("start", "special")
fc_fp.edge("special", "handle_sp", branch="yes")
fc_fp.edge("special", "align", branch="no")
fc_fp.edge("align", "compute")
fc_fp.edge("compute", "normalize")
fc_fp.edge("normalize", "round_step")
fc_fp.edge("round_step", "ovflw")
fc_fp.edge("ovflw", "set_inf", branch="yes")
fc_fp.edge("ovflw", "end", branch="no")
fc_fp.edge("set_inf", "end")
fc_fp.edge("handle_sp", "end")
en.story.extend(fc_fp.as_flowable())

# FP multiplication flowchart
fc_fpmul = ed.Flowchart(
    width=en.CW,
    height=620,
    theme=diag_theme,
    caption="Fig 5: IEEE 754 floating-point multiplication algorithm",
)
fc_fpmul.terminal("start", "FP MULTIPLY: Inputs A & B", x=240, y=590)
fc_fpmul.decision("special", "Special values?\n(0, INF, NaN)", x=240, y=520)
fc_fpmul.process("handle_sp", "Return special result\n(e.g., NaN/INF)", x=110, y=450)
fc_fpmul.process("signs", "Sign: Sr <- Sa XOR Sb", x=240, y=450)
fc_fpmul.process(
    "exponent", "Exponent: Er <- Ea + Eb - bias\n(stored exponents)", x=240, y=380
)
fc_fpmul.process("multiply", "Multiply mantissas:\nMr <- 1.Ma x 1.Mb", x=240, y=310)
fc_fpmul.decision("norm_chk", "Normalize needed?\nMr >= 2.0", x=240, y=240)
fc_fpmul.process("normalize", "Mr <- Mr / 2\nEr <- Er + 1", x=370, y=170)
fc_fpmul.process("round_step", "Round Mr to 23 bits", x=240, y=170)
fc_fpmul.decision("ovflw", "Exponent overflow\nor underflow?", x=240, y=100)
fc_fpmul.process("set_inf", "Set +/- INF or 0 /\ndenormalized", x=110, y=30)
fc_fpmul.terminal("end", "Return IEEE 754 result", x=240, y=30)

fc_fpmul.edge("start", "special")
fc_fpmul.edge("special", "handle_sp", branch="yes", orthogonal=True)
fc_fpmul.edge("special", "signs", branch="no")
fc_fpmul.edge("signs", "exponent")
fc_fpmul.edge("exponent", "multiply")
fc_fpmul.edge("multiply", "norm_chk")
fc_fpmul.edge("norm_chk", "normalize", branch="yes", orthogonal=True)
fc_fpmul.edge("norm_chk", "round_step", branch="no")
fc_fpmul.edge("normalize", "round_step")
fc_fpmul.edge("round_step", "ovflw")
fc_fpmul.edge("ovflw", "set_inf", branch="yes", orthogonal=True)
fc_fpmul.edge("ovflw", "end", branch="no")
fc_fpmul.edge("set_inf", "end")
fc_fpmul.edge("handle_sp", "end", path=[(50, 450), (50, 30)])
en.story.extend(fc_fpmul.as_flowable())

# FP division flowchart
fc_fpdiv = ed.Flowchart(
    width=en.CW,
    height=620,
    theme=diag_theme,
    caption="Fig 6: IEEE 754 floating-point division algorithm",
)
fc_fpdiv.terminal("start", "FP DIVIDE: Inputs A & B", x=240, y=590)
fc_fpdiv.decision("special", "Special values\nor divide by 0?", x=240, y=520)
fc_fpdiv.process(
    "handle_sp", "Return special result\n(e.g., NaN/INF/Div0)", x=110, y=450
)
fc_fpdiv.process("signs", "Sign: Sr <- Sa XOR Sb", x=240, y=450)
fc_fpdiv.process(
    "exponent", "Exponent: Er <- Ea - Eb + bias\n(stored exponents)", x=240, y=380
)
fc_fpdiv.process("divide", "Divide mantissas:\nMr <- 1.Ma / 1.Mb", x=240, y=310)
fc_fpdiv.decision("norm_chk", "Normalize needed?\nMr < 1.0", x=240, y=240)
fc_fpdiv.process("normalize", "Mr <- Mr x 2\nEr <- Er - 1", x=370, y=170)
fc_fpdiv.process("round_step", "Round Mr to 23 bits", x=240, y=170)
fc_fpdiv.decision("ovflw", "Exponent overflow\nor underflow?", x=240, y=100)
fc_fpdiv.process("set_inf", "Set +/- INF or 0 /\ndenormalized", x=110, y=30)
fc_fpdiv.terminal("end", "Return IEEE 754 result", x=240, y=30)

fc_fpdiv.edge("start", "special")
fc_fpdiv.edge("special", "handle_sp", branch="yes", orthogonal=True)
fc_fpdiv.edge("special", "signs", branch="no")
fc_fpdiv.edge("signs", "exponent")
fc_fpdiv.edge("exponent", "divide")
fc_fpdiv.edge("divide", "norm_chk")
fc_fpdiv.edge("norm_chk", "normalize", branch="yes", orthogonal=True)
fc_fpdiv.edge("norm_chk", "round_step", branch="no")
fc_fpdiv.edge("normalize", "round_step")
fc_fpdiv.edge("round_step", "ovflw")
fc_fpdiv.edge("ovflw", "set_inf", branch="yes", orthogonal=True)
fc_fpdiv.edge("ovflw", "end", branch="no")
fc_fpdiv.edge("set_inf", "end")
fc_fpdiv.edge("handle_sp", "end", path=[(50, 450), (50, 30)])
en.story.extend(fc_fpdiv.as_flowable())

en.tip(
    "FP add: align exponents (shift smaller), add mantissas, normalize, round. "
    "FP multiply: XOR signs, add stored exponents minus bias, multiply mantissas, normalize. "
    "FP divide: XOR signs, subtract stored exponents plus bias, divide mantissas, normalize. "
    "Guard/Round/Sticky bits improve rounding accuracy."
)
en.br()

# =============================================================================
#  2.8  HARDWIRED vs MICROPROGRAMMED CONTROL UNIT
# =============================================================================
en.chap_box("2.8  Hardwired vs Microprogrammed Control Unit")
en.section("Role of the Control Unit")
en.definition(
    "<b>Control Unit (CU):</b> The component of the CPU that generates the "
    "<b>control signals</b> required to execute each instruction. Based on the "
    "current instruction (from IR) and the processor state (flags, timing), "
    "the CU activates the appropriate datapath elements: ALU operation, register "
    "loads, memory read/write, I/O operations. Two implementation strategies exist: "
    "<b>Hardwired</b> and <b>Microprogrammed</b>."
)

en.section("Hardwired Control Unit")
en.definition(
    "<b>Hardwired Control Unit:</b> Control signals are generated by a fixed "
    "combinational/sequential logic circuit. The opcode bits are decoded by logic "
    "gates to produce control signals directly. There is no intermediate storage -- "
    "changing the instruction set requires redesigning the hardware."
)
en.bullet(
    [
        "<b>Structure:</b> Instruction decoder + timing generator (sequencer) + combinational logic gates.",
        "<b>Speed:</b> Very fast -- combinational logic, no memory access for control signals.",
        "<b>Flexibility:</b> Very inflexible -- modifying the ISA requires a new hardware design.",
        "<b>Cost:</b> Complex logic for complex ISAs. Simple for RISC (few instructions).",
        "<b>Used in:</b> RISC processors (ARM, MIPS, RISC-V) where ISA is simple and fixed.",
        "<b>Design:</b> Mealy/Moore finite state machine (FSM) whose outputs are control signals.",
    ]
)

en.section("Microprogrammed Control Unit")
en.definition(
    "<b>Microprogrammed Control Unit:</b> Each machine instruction is translated "
    "into a sequence of <b>microinstructions</b> stored in a <b>Control Memory (CM)</b> "
    "(also called the Control Store). The CU fetches microinstructions from CM and "
    "generates control signals. Changing the ISA only requires updating the microprogram."
)
en.bullet(
    [
        "<b>Structure:</b> Control Memory (ROM/RAM) + Microprogram Counter (MPC) + Microinstruction Register (MIR).",
        "<b>Speed:</b> Slower -- requires an additional memory fetch cycle per microinstruction.",
        "<b>Flexibility:</b> Very flexible -- new instructions added by writing new microprograms.",
        "<b>Cost:</b> Simpler hardware, but extra control memory required.",
        "<b>Used in:</b> CISC processors (Intel x86, IBM mainframes) with complex instruction sets.",
        "<b>Writable CU:</b> Some systems use writable control store (WCSL) -- microprogram in RAM, updatable at runtime.",
    ]
)

en.section("Comparison Table")
en.info_table(
    ["Property", "Hardwired CU", "Microprogrammed CU"],
    [
        [
            "Implementation",
            "Logic gates, FSM (combinational)",
            "Control memory (ROM/RAM) + MPC",
        ],
        [
            "Speed",
            "Very fast (1 clock cycle per control signal)",
            "Slower (fetch microinstruction from CM)",
        ],
        [
            "Flexibility",
            "Rigid -- hardware must be redesigned",
            "Flexible -- update microprogram in memory",
        ],
        [
            "Design complexity",
            "Complex for complex ISA",
            "Simpler hardware, complex microprogram",
        ],
        ["Debugging", "Difficult -- need new chip", "Easy -- reprogram control store"],
        ["Cost", "More expensive NRE for complex ISA", "Extra control memory cost"],
        ["Typical ISA", "RISC (ARM, MIPS, RISC-V)", "CISC (x86, IBM System/360)"],
        ["Modification", "Requires new fabrication", "Can be done at runtime (WCSL)"],
    ],
)

# CU comparison diagram
from engrapha_diagrams import ResponsiveDrawingFlowable

left_stack = ed.LayeredStack(
    width=en.CW * 0.44,
    height=220,
    theme=diag_theme,
    caption="Hardwired CU",
)
left_stack.layer("IR Opcode Input", sublabel="bits feed directly into gates")
left_stack.layer("Instruction Decoder", sublabel="combinational logic tree")
left_stack.layer("Timing Sequencer", sublabel="clock-driven state counter")
left_stack.layer("Control Signal Generator", sublabel="AND/OR gate network")
left_stack.layer("Control Signals Output", sublabel="to ALU, MUX, registers, buses")

right_stack = ed.LayeredStack(
    width=en.CW * 0.44,
    height=220,
    theme=diag_theme,
    caption="Microprogrammed CU",
)
right_stack.layer("IR Opcode Input", sublabel="maps to starting address in CM")
right_stack.layer(
    "Microprogram Counter (MPC)", sublabel="points to current microinstruction"
)
right_stack.layer("Control Memory (ROM)", sublabel="stores microinstructions (CM)")
right_stack.layer(
    "Microinstruction Register (MIR)", sublabel="holds current microinstruction"
)
right_stack.layer("Control Signals Output", sublabel="bits of MIR = control signals")

left_stack.as_flowable()
right_stack.as_flowable()

tbl_cu = Table(
    [
        [
            ResponsiveDrawingFlowable(left_stack.drawing),
            ResponsiveDrawingFlowable(right_stack.drawing),
        ]
    ],
    colWidths=[en.CW * 0.48, en.CW * 0.48],
)
tbl_cu.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]
    )
)
en.add(tbl_cu)
en.sp(6)
en.add(
    Paragraph(
        "Fig 7 (left): Hardwired CU -- pure logic gates.  |  Fig 7 (right): Microprogrammed CU -- ROM-based.",
        en.COVER_SUB,
    )
)

en.tip(
    "Hardwired CU: fast, inflexible, best for RISC. "
    "Microprogrammed CU: flexible, slower, best for CISC. "
    "Key insight: RISC uses hardwired, CISC uses microprogrammed. "
    "Microprogram = firmware (software stored in control ROM)."
)
en.br()

# =============================================================================
#  2.9  CONTROL MEMORY AND MICROPROGRAM SEQUENCE
# =============================================================================
en.chap_box("2.9  Control Memory and Microprogram Sequencing")
en.section("Control Memory (Control Store)")
en.definition(
    "<b>Control Memory (CM):</b> A fast read-only memory (ROM, or writable RAM in some "
    "designs) that stores the <b>microprogram</b> -- the set of all microinstructions "
    "for every machine instruction in the ISA. Each word in CM is one "
    "<b>microinstruction</b> whose bits directly control the datapath."
)
en.bullet(
    [
        "<b>Width:</b> One microinstruction word, typically 32-100 bits wide. Each bit (or field) controls one datapath signal.",
        "<b>Depth:</b> One entry per microinstruction step. A complex ISA may need thousands of microinstructions.",
        "<b>Access:</b> Addressed by the Microprogram Counter (MPC), similar to how PC addresses instruction memory.",
        "<b>ROM CM:</b> Fixed at chip design time. Fast access. Cannot be updated (mask ROM).",
        "<b>EPROM/RAM CM:</b> Can be programmed or rewritten. Enables microcode updates (CPU firmware patches).",
    ]
)

en.section("Microinstruction Format")
en.definition(
    "<b>Microinstruction:</b> A single entry in the control memory that specifies "
    "one or more micro-operations to be performed simultaneously, plus the address "
    "of the next microinstruction (or a condition field to select the next address)."
)

en.subsection("Horizontal Microinstruction")
en.body(
    "Each bit directly controls one datapath signal. Very wide (many bits) but allows "
    "maximum parallelism -- any combination of micro-operations can be performed "
    "simultaneously. Decoding overhead is minimal."
)
en.frame_format(
    "Horizontal Microinstruction Format",
    [
        ("ALU_OP (4)", "4 bits"),
        ("SRC_A (3)", "3 bits"),
        ("SRC_B (3)", "3 bits"),
        ("DEST (3)", "3 bits"),
        ("MEM_RD", "1 bit"),
        ("MEM_WR", "1 bit"),
        ("COND (2)", "2 bits"),
        ("NEXT_ADDR (10)", "10 bits"),
    ],
)

en.subsection("Vertical Microinstruction")
en.body(
    "Control signals are encoded into fields (like a mini instruction set). "
    "Narrower word width but requires a decoder at each stage. Less parallelism "
    "since only one encoded operation can be specified per field."
)
en.frame_format(
    "Vertical Microinstruction Format (encoded fields)",
    [
        ("F (4 bits)", "Encoded function"),
        ("DR (2 bits)", "Destination reg"),
        ("SA (2 bits)", "Source A"),
        ("SB (2 bits)", "Source B"),
        ("MB", "Memory/Bus"),
        ("SEQ (4 bits)", "Sequencer/Next addr"),
    ],
)

en.info_table(
    ["Property", "Horizontal", "Vertical"],
    [
        ["Word width", "Very wide (50-100+ bits)", "Narrow (16-32 bits)"],
        [
            "Parallelism",
            "Maximum -- all operations simultaneously",
            "Limited -- encoded fields",
        ],
        ["Decoder needed", "No (direct control)", "Yes (field decoder required)"],
        ["Control memory size", "Fewer words but very wide", "More words but narrow"],
        ["Speed", "Faster (no decode delay)", "Slower (decode adds latency)"],
        ["Flexibility", "Very high", "Moderate"],
    ],
)

en.section("Microprogram Sequencer")
en.definition(
    "<b>Microprogram Sequencer:</b> The hardware that determines the address of "
    "the NEXT microinstruction to fetch from control memory. It selects the next "
    "address based on: the NEXT_ADDR field of the current microinstruction, "
    "condition flags (Z, N, C), or the opcode of the machine instruction being "
    "executed (for the fetch-to-execute transition)."
)

en.info_table(
    ["Next Address Source", "When Used", "Effect"],
    [
        [
            "NEXT_ADDR field of microinstruction",
            "Sequential execution",
            "Unconditional branch to specified CM address",
        ],
        [
            "NEXT_ADDR + 1 (increment MPC)",
            "Sequential microprogram steps",
            "Proceed to the next microinstruction",
        ],
        [
            "IR opcode -> mapping ROM -> CM address",
            "Start of each machine instruction",
            "Jump to the correct microprogram entry point",
        ],
        [
            "Conditional select based on flags",
            "Branch microinstructions",
            "Choose one of two addresses based on Z/N/C/V",
        ],
        [
            "Subroutine call/return",
            "Common microprogram sequences",
            "Push MPC to microprogram stack, jump, then return",
        ],
    ],
)

en.section("Microprogram Execution Sequence")
en.code_block("""
 MICROPROGRAM EXECUTION FLOW:
 ======================================================
 1. FETCH microinstruction:
    MIR <- CM[MPC]          (load current microinstruction into MIR)

 2. DECODE fields of MIR:
    - Extract ALU_OP, SRC_A, SRC_B, DEST, MEM_RD, MEM_WR, COND, NEXT_ADDR

 3. EXECUTE micro-operations simultaneously (one clock):
    - ALU performs ALU_OP on operands from SRC_A and SRC_B
    - Result stored in DEST register
    - Memory read or write if MEM_RD/MEM_WR set
    - All micro-ops in one microinstruction happen in parallel

 4. DETERMINE NEXT ADDRESS:
    - If COND == 00: MPC <- NEXT_ADDR  (unconditional jump)
    - If COND == 01: MPC <- NEXT_ADDR if Z=1 else MPC+1  (branch on zero)
    - If COND == 10: MPC <- NEXT_ADDR if C=1 else MPC+1  (branch on carry)
    - If COND == 11: MPC <- MAPPING[IR.opcode]  (fetch new machine instruction)

 5. REPEAT from step 1.

 MICROPROGRAMMED FETCH CYCLE (typical):
 ======================================================
 Micro-step 1: MAR <- PC; MPC+1
 Micro-step 2: MDR <- M[MAR]; PC <- PC+1; MPC+1
 Micro-step 3: IR <- MDR; MPC <- MAPPING[IR.opcode]  (dispatch to execute routine)
""")

# Microprogram sequencer diagram
net_seq = ed.NetworkDiagram(
    width=en.CW,
    height=330,
    theme=diag_theme,
    caption="Fig 8: Microprogrammed Control Unit -- sequencer and control memory",
)
net_seq.node(
    "ir",
    "Instruction\nRegister (IR)",
    x=65,
    y=275,
    kind="custom",
    custom_draw=draw_register,
)
net_seq.node("map", "Mapping\nROM", x=65, y=165, kind="database")
net_seq.node(
    "mpc",
    "Microprogram\nCounter (MPC)",
    x=210,
    y=165,
    kind="custom",
    custom_draw=draw_register,
)
net_seq.node("cm", "Control\nMemory (CM)", x=355, y=165, kind="database")
net_seq.node(
    "mir",
    "Microinstruction\nRegister (MIR)",
    x=355,
    y=55,
    kind="custom",
    custom_draw=draw_register,
)
net_seq.node(
    "ctrl",
    "Control\nSignals Out",
    x=465,
    y=55,
    kind="custom",
    custom_draw=draw_register,
)
net_seq.node("cond", "Flags", x=210, y=55, kind="custom", custom_draw=draw_flags)
net_seq.node(
    "seq",
    "Sequencer\n(Next Addr Logic)",
    x=210,
    y=275,
    kind="custom",
    custom_draw=draw_cu,
)

net_seq.link("ir", "map", label="opcode")
net_seq.link("map", "mpc", label="start addr")
net_seq.link("mpc", "cm", label="CM address")
net_seq.link("cm", "mir", label="microinstruction")
net_seq.link("mir", "ctrl", label="control signals")
net_seq.link("mir", "seq", label="NEXT_ADDR, COND")
net_seq.link("cond", "seq", label="flags")
net_seq.link("seq", "mpc", label="next MPC")
en.story.extend(net_seq.as_flowable())

en.tip(
    "Control Memory: stores all microinstructions. MPC addresses it. "
    "MIR holds the current microinstruction. "
    "Sequencer determines next MPC from: NEXT_ADDR field, condition flags, or IR opcode mapping. "
    "Horizontal MI: wide, direct control. Vertical MI: narrow, encoded, needs decoder."
)
en.br()

# =============================================================================
#  2.10  QUICK REVISION SUMMARY
# =============================================================================
en.part_box("UNIT II -- QUICK REVISION SUMMARY")
en.chap_box("Key Concepts at a Glance")

en.info_table(
    ["Topic", "Key Point to Remember"],
    [
        [
            "Sign-Magnitude",
            "MSB = sign bit. Two zeros (+0 and -0). Range: -(2^(n-1)-1) to +(2^(n-1)-1). "
            "Complex arithmetic (sign check needed). Rarely used for computation.",
        ],
        [
            "1's Complement",
            "Negate = invert all bits. Two zeros. Range: -(2^(n-1)-1) to +(2^(n-1)-1). "
            "Addition needs end-around carry. Used in TCP/IP checksums.",
        ],
        [
            "2's Complement",
            "Negate = invert + add 1. ONE zero. Range: -2^(n-1) to +2^(n-1)-1. "
            "Simple addition hardware (no special cases). Universal standard.",
        ],
        [
            "2's Complement Range",
            "8-bit: -128 to +127. 16-bit: -32768 to +32767. 32-bit: -2^31 to +2^31-1. "
            "One extra negative number (no positive counterpart).",
        ],
        [
            "Overflow Detection",
            "V = carry_into_MSB XOR carry_out_of_MSB. "
            "Positive + Positive = Negative -> overflow. "
            "Negative + Negative = Positive -> overflow.",
        ],
        [
            "Subtraction",
            "A - B = A + NOT(B) + 1. Hardware: invert B, set Cin=1. "
            "One adder does both add and subtract.",
        ],
        [
            "Booth's Algorithm",
            "Signed multiplication. Examine (Q[0], Q[-1]): "
            "01=add M, 10=subtract M, 00/11=no op. Arithmetic right shift each step. "
            "n steps for n-bit multiplication.",
        ],
        [
            "Restoring Division",
            "Shift left (A,Q), subtract M. If A<0: restore (A+M), Q[0]=0. Else: Q[0]=1. "
            "n steps. Quotient in Q, remainder in A.",
        ],
        [
            "Non-Restoring Division",
            "If A>=0: shift, A-M, Q[0]=1. If A<0: shift, A+M, Q[0]=0. "
            "Faster than restoring (no restoration step).",
        ],
        [
            "IEEE 754 Single (32-bit)",
            "1 sign + 8 exponent (bias 127) + 23 mantissa. Implied leading 1. "
            "Value = (-1)^S x 1.M x 2^(E-127). Range ~+-3.4 x 10^38.",
        ],
        [
            "IEEE 754 Double (64-bit)",
            "1 sign + 11 exponent (bias 1023) + 52 mantissa. "
            "Value = (-1)^S x 1.M x 2^(E-1023). Range ~+-1.8 x 10^308.",
        ],
        [
            "IEEE 754 Special Values",
            "E=0,M=0 -> zero. E=0,M!=0 -> denormal. "
            "E=all ones,M=0 -> +/-INF. E=all ones,M!=0 -> NaN.",
        ],
        [
            "FP Addition Steps",
            "(1) Align exponents (shift smaller). (2) Add/subtract mantissas. "
            "(3) Normalize (1.XXXX). (4) Round. (5) Check overflow/underflow.",
        ],
        [
            "FP Multiplication",
            "Sign = XOR of signs. Exponent = Ea + Eb - bias. Mantissa = Ma x Mb. "
            "Normalize and round.",
        ],
        [
            "Hardwired CU",
            "Logic gates, FSM. Fast, inflexible. Best for RISC (ARM, MIPS). "
            "Modify ISA = new chip design.",
        ],
        [
            "Microprogrammed CU",
            "Control memory (ROM) stores microinstructions. Flexible, slower. "
            "Best for CISC (x86). Modify ISA = update microprogram.",
        ],
        [
            "Horizontal Microinstruction",
            "One bit per control signal. Wide word. Maximum parallelism. No decoder needed.",
        ],
        [
            "Vertical Microinstruction",
            "Encoded fields. Narrow word. Less parallelism. Decoder needed. Smaller CM size.",
        ],
        [
            "Microprogram Sequencer",
            "Determines next MPC from: NEXT_ADDR field, condition flags, IR opcode mapping. "
            "MPC -> CM -> MIR -> control signals -> datapath.",
        ],
    ],
)

en.highlight(
    "<b>UNIT II EXAM BLUEPRINT:</b>  "
    "2-mark: State IEEE 754 single precision format. "
    "Define 2's complement range. Differentiate hardwired vs microprogrammed CU. "
    "State Booth's algorithm encoding table.  "
    "5-mark: Convert a number to IEEE 754 single precision with all steps. "
    "Trace Booth's algorithm for a 4-bit example. "
    "Explain FP addition algorithm with steps. "
    "Explain restoring division with example.  "
    "10-mark: Explain IEEE 754 representation (single and double) with special values. "
    "Explain Booth's algorithm with hardware and flowchart. "
    "Compare hardwired and microprogrammed control unit with diagrams. "
    "Explain microinstruction formats (horizontal and vertical) with control memory.",
)

en.sp(10)
en.rule(en.get_theme().rl(en.get_theme().accent), 1.0)
en.sp(6)
en.add(
    Paragraph(
        "Computer Architecture IT-404 Unit II -- Bharat Dangi  |  UIT-RGPV (Autonomous) Bhopal | Semester IV",
        en.COVER_SUB,
    )
)

# =============================================================================
#  BUILD PDF
# =============================================================================
en.build_doc(
    "CA_Unit2_Notes.pdf",
    title="Computer Architecture - Unit II Notes",
    author="Bharat Dangi",
)
print("Generated: CA_Unit2_Notes.pdf")
