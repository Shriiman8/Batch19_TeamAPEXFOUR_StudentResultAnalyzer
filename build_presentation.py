"""
Builds a professional, 7-slide widescreen PowerPoint presentation (presentation.pptx)
for the 'Student Result and Grade Analyzer' hackathon submission.
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette Definitions
    COLOR_BG_DARK = RGBColor(15, 23, 42)       # Slate 900 (Title / Accent)
    COLOR_BG_LIGHT = RGBColor(248, 250, 252)   # Slate 50
    COLOR_PRIMARY = RGBColor(30, 58, 138)      # Blue 900
    COLOR_ACCENT_BLUE = RGBColor(37, 99, 235)  # Blue 600
    COLOR_ACCENT_GREEN = RGBColor(16, 185, 129)# Emerald 500
    COLOR_ACCENT_RED = RGBColor(239, 68, 68)   # Red 500
    COLOR_CARD_BG = RGBColor(255, 255, 255)    # Pure White
    COLOR_CARD_BORDER = RGBColor(226, 232, 240)# Slate 200
    COLOR_TEXT_DARK = RGBColor(30, 41, 59)     # Slate 800
    COLOR_TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
    COLOR_TEXT_WHITE = RGBColor(255, 255, 255)

    blank_layout = prs.slide_layouts[6]

    # Helper: Add Slide Header
    def add_slide_header(slide, title_text, category_text="MINI HACKATHON PROJECT"):
        # Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG_LIGHT
        bg.line.fill.background()

        # Top Banner bar
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.15))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = COLOR_PRIMARY
        top_bar.line.fill.background()

        # Category / Tag
        tx_box_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.3))
        tf_cat = tx_box_cat.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = "Arial"
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = RGBColor(191, 219, 254) # Blue 200

        # Title
        tx_box_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.40), Inches(11.5), Inches(0.6))
        tf_t = tx_box_t.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.name = "Arial"
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_WHITE

        # Footer info
        foot_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.35))
        tf_f = foot_box.text_frame
        p_f = tf_f.paragraphs[0]
        p_f.text = "Batch: Batch - 19 | Team: APEX FOUR | Student Result & Grade Analyzer"
        p_f.font.name = "Arial"
        p_f.font.size = Pt(10)
        p_f.font.color.rgb = COLOR_TEXT_MUTED

    # Helper: Add Styled Card
    def add_card(slide, left, top, width, height, title, body_lines, accent_color=COLOR_ACCENT_BLUE):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_CARD_BORDER
        card.line.width = Pt(1.5)

        # Header Accent stripe
        stripe = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, Inches(0.1))
        stripe.fill.solid()
        stripe.fill.fore_color.rgb = accent_color
        stripe.line.fill.background()

        # Text inside card
        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p_head = tf.paragraphs[0]
        p_head.text = title
        p_head.font.name = "Arial"
        p_head.font.size = Pt(16)
        p_head.font.bold = True
        p_head.font.color.rgb = COLOR_TEXT_DARK
        p_head.space_after = Pt(10)

        for line in body_lines:
            p = tf.add_paragraph()
            p.text = line
            p.font.name = "Arial"
            p.font.size = Pt(12)
            p.font.color.rgb = COLOR_TEXT_DARK
            p.space_after = Pt(6)

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_BG_DARK
    bg1.line.fill.background()

    # Decorative banner box
    decor = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(1.2), Inches(11.333), Inches(0.08))
    decor.fill.solid()
    decor.fill.fore_color.rgb = COLOR_ACCENT_BLUE
    decor.line.fill.background()

    # Badge Pill
    pill = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.5), Inches(3.6), Inches(0.45))
    pill.fill.solid()
    pill.fill.fore_color.rgb = COLOR_ACCENT_BLUE
    pill.line.fill.background()
    p_pill = pill.text_frame.paragraphs[0]
    p_pill.text = "C PROGRAMMING MINI HACKATHON"
    p_pill.font.name = "Arial"
    p_pill.font.size = Pt(11)
    p_pill.font.bold = True
    p_pill.font.color.rgb = COLOR_TEXT_WHITE
    p_pill.alignment = PP_ALIGN.CENTER

    # Main Title
    tb_t1 = s1.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(11.333), Inches(1.8))
    tf_t1 = tb_t1.text_frame
    tf_t1.word_wrap = True
    p1 = tf_t1.paragraphs[0]
    p1.text = "Student Result & Grade Analyzer"
    p1.font.name = "Arial"
    p1.font.size = Pt(40)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_TEXT_WHITE

    p1_sub = tf_t1.add_paragraph()
    p1_sub.text = "A Menu-Driven Performance Evaluation, Subject Validation & Class Analytics System in C"
    p1_sub.font.name = "Arial"
    p1_sub.font.size = Pt(18)
    p1_sub.font.color.rgb = RGBColor(148, 163, 184)
    p1_sub.space_before = Pt(10)

    # Team Info Cards
    # Team & Batch Box
    team_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(4.3), Inches(5.3), Inches(2.2))
    team_card.fill.solid()
    team_card.fill.fore_color.rgb = RGBColor(30, 41, 59)
    team_card.line.color.rgb = RGBColor(51, 65, 85)
    tf_tc = team_card.text_frame
    tf_tc.word_wrap = True
    ptc1 = tf_tc.paragraphs[0]
    ptc1.text = "TEAM DETAILS"
    ptc1.font.name = "Arial"
    ptc1.font.size = Pt(13)
    ptc1.font.bold = True
    ptc1.font.color.rgb = COLOR_ACCENT_BLUE
    ptc1.space_after = Pt(8)

    ptc2 = tf_tc.add_paragraph()
    ptc2.text = "• Batch: Batch - 19"
    ptc2.font.name = "Arial"
    ptc2.font.size = Pt(15)
    ptc2.font.color.rgb = COLOR_TEXT_WHITE
    ptc2.space_after = Pt(4)

    ptc3 = tf_tc.add_paragraph()
    ptc3.text = "• Team Number: APEX FOUR"
    ptc3.font.name = "Arial"
    ptc3.font.size = Pt(15)
    ptc3.font.color.rgb = COLOR_TEXT_WHITE

    # Members Box
    mem_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.3), Inches(5.5), Inches(2.2))
    mem_card.fill.solid()
    mem_card.fill.fore_color.rgb = RGBColor(30, 41, 59)
    mem_card.line.color.rgb = RGBColor(51, 65, 85)
    tf_mc = mem_card.text_frame
    tf_mc.word_wrap = True
    pmc1 = tf_mc.paragraphs[0]
    pmc1.text = "CONTRIBUTING TEAM MEMBERS"
    pmc1.font.name = "Arial"
    pmc1.font.size = Pt(13)
    pmc1.font.bold = True
    pmc1.font.color.rgb = COLOR_ACCENT_GREEN
    pmc1.space_after = Pt(8)

    members = ["1. Daksh (Lead Developer)", "2. Shriman Nautiyal (Algorithm & Validation)", "3. Shivam Rawat (Testing & Documentation)"]
    for m in members:
        p = tf_mc.add_paragraph()
        p.text = f"• {m}"
        p.font.name = "Arial"
        p.font.size = Pt(13)
        p.font.color.rgb = COLOR_TEXT_WHITE
        p.space_after = Pt(4)

    # =========================================================================
    # SLIDE 2: PROBLEM STATEMENT & MOTIVATION
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_header(s2, "Problem Statement & Project Objectives", "CHALLENGE CONTEXT")

    add_card(s2, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2),
             "The Academic Grading Challenge", [
                 "• Manual calculation of student totals, percentages, and letter grades is prone to human error and significant delays.",
                 "• Misleading Averages: In typical percentage calculators, a student scoring 90% in 4 subjects and 10% in 1 subject passes overall despite failing a core competency.",
                 "• Vulnerability to Bad Input: Standard C console programs frequently enter infinite loops when users type non-numeric characters into scanf().",
                 "• Lack of Instant Analytics: Educators lack real-time class summaries showing pass rates, toppers, and grade distribution."
             ], accent_color=COLOR_ACCENT_RED)

    add_card(s2, Inches(6.9), Inches(1.5), Inches(5.6), Inches(5.2),
             "Project Scope & Key Objectives", [
                 "• Multi-Student Records: Dynamic processing of up to 100 students across 5 academic subjects using C struct arrays.",
                 "• Strict Subject-Wise Pass Enforcement: Enforces minimum passing mark of 35 in EACH individual subject. Any subject < 35 triggers immediate FAIL with grade 'F'.",
                 "• Dual Reporting Modules: Produces a cleanly aligned ASCII result summary table AND a statistical class performance report.",
                 "• Bulletproof Input Validation: Eliminates input buffer corruption via fgets() + sscanf(), rejects duplicate/negative roll numbers and invalid marks."
             ], accent_color=COLOR_ACCENT_BLUE)

    # =========================================================================
    # SLIDE 3: PROPOSED SOLUTION & KEY FEATURES
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_header(s3, "Proposed Solution & Core Architecture", "SYSTEM FEATURES")

    features = [
        ("Modular Menu-Driven Interface", [
            "Seamless switch-case console navigation with 5 intuitive options.",
            "Handles empty-database edge cases gracefully without crashes."
        ], Inches(0.8), Inches(1.5)),
        ("Rigorous Subject-Level Evaluation", [
            "Mandatory 35/100 passing threshold in each of the 5 subjects.",
            "Standard letter grading: A+ (>=90%), A (>=80%), B, C, D, E, F."
        ], Inches(6.9), Inches(1.5)),
        ("Structured Tabular Output", [
            "ASCII formatted grid with fixed column widths and clear headers.",
            "Displays roll number, name, 5 subject marks, total, percentage, grade, and status."
        ], Inches(0.8), Inches(4.2)),
        ("Class Analytics & Topper Intelligence", [
            "Computes class average, pass/fail counts and pass percentages.",
            "Identifies class topper (highest percentage among passed candidates)."
        ], Inches(6.9), Inches(4.2))
    ]

    for title, lines, left, top in features:
        add_card(s3, left, top, Inches(5.6), Inches(2.5), title, ["• " + l for l in lines], accent_color=COLOR_ACCENT_BLUE)

    # =========================================================================
    # SLIDE 4: PROGRAM LOGIC & FUNDAMENTAL C CONCEPTS
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_header(s4, "Program Logic Flow & C Concepts Applied", "TECHNICAL IMPLEMENTATION")

    add_card(s4, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2),
             "Key C Programming Concepts Used", [
                 "• Structs (typedef struct): Encapsulates student roll number, name, marks array, total, percentage, grade, and status.",
                 "• 1D Arrays: Used for storing 5 subject marks and the collection of Student structs (up to 100 students).",
                 "• Pointers: Passing struct pointers (Student *s, const Student *students) for zero-copy, efficient memory access.",
                 "• String Operations: string.h functions (strcpy, strcspn, strlen, strncpy) for safe string handling.",
                 "• Loops & Control Structures: while loops for menus/retry prompts, for loops for iterations, switch-case for routing.",
                 "• Modular Functions: 11 decoupled functions adhering to single-responsibility architecture."
             ], accent_color=COLOR_PRIMARY)

    add_card(s4, Inches(6.9), Inches(1.5), Inches(5.6), Inches(5.2),
             "Algorithm & Grading Logic", [
                 "1. Start -> Initialize student database and display main menu loop.",
                 "2. Input Student Details -> Read and validate Roll No (unique, >0), Name, and 5 marks in range [0, 100].",
                 "3. Result Calculation:",
                 "     totalMarks = Sum(marks[0..4])",
                 "     percentage = (totalMarks / 500.0) * 100.0",
                 "4. Condition Check: If ANY marks[i] < 35.0:",
                 "     isPassed = 0; Grade = 'F' (Fail)",
                 "   Else: isPassed = 1; Assign A+, A, B, C, D, E based on %.",
                 "5. Analytics: Aggregate class average, pass/fail count, identify passed topper with highest percentage."
             ], accent_color=COLOR_ACCENT_GREEN)

    # =========================================================================
    # SLIDE 5: IMPLEMENTATION HIGHLIGHTS & ROBUST INPUT VALIDATION
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_header(s5, "Input Validation & Resilient Engineering", "FAULT TOLERANCE")

    validation_items = [
        ("Buffer Overflow & Infinite Loop Shield", [
            "Replaced risky scanf() with robust fgets() line-buffered reading.",
            "sscanf(buffer, \"%d %c\", &val, &extra) ensures complete line validation and catches trailing alphabet junk without hanging."
        ], Inches(0.8), Inches(1.5)),
        ("Negative & Out-of-Bounds Protection", [
            "Marks strictly bounded within [0.0, 100.0]; negative or >100 entries immediately re-prompt the user with descriptive diagnostics.",
            "Roll numbers must be positive integers (>0)."
        ], Inches(6.9), Inches(1.5)),
        ("Duplicate Roll Number Prevention", [
            "isRollNumberUnique() traverses the student list to guarantee no two students share the same identifier.",
            "Prevents accidental record overwrite or ambiguous search queries."
        ], Inches(0.8), Inches(4.2)),
        ("Zero-Data Edge Case Handling", [
            "Attempting to view the summary table or class analytics report before adding students cleanly displays informative warnings.",
            "System remains responsive and returns directly to the main menu."
        ], Inches(6.9), Inches(4.2))
    ]

    for title, lines, left, top in validation_items:
        add_card(s5, left, top, Inches(5.6), Inches(2.5), title, ["• " + l for l in lines], accent_color=COLOR_ACCENT_BLUE)

    # =========================================================================
    # SLIDE 6: TEST CASES & EMPIRICAL VERIFICATION
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_slide_header(s6, "Test Suite & Empirical Verification Results", "TESTING & QUALITY ASSURANCE")

    # Add Test Case Table
    rows, cols = 6, 6
    left, top, width, height = Inches(0.8), Inches(1.6), Inches(11.733), Inches(4.8)
    table_shape = s6.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table

    col_widths = [Inches(1.8), Inches(2.3), Inches(2.3), Inches(1.5), Inches(1.8), Inches(2.0)]
    for idx, w in enumerate(col_widths):
        table.columns[idx].width = w

    headers = ["Test Category", "Input Test Data", "Observed Behavior", "Total / %", "Grade & Status", "Result"]
    for c_idx, h in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Arial"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER

    test_data = [
        ("Normal Pass & Boundary 100", "Marks: 95, 98, 100, 92, 90\nRoll: 101 (Daksh)", "All subjects >= 35, highest total recorded", "475 / 95.0%", "Grade A+\nPASS", "PASSED (Class Topper)"),
        ("Subject Fail (High % Total)", "Marks: 88, 92, 28, 85, 90\nRoll: 102 (Shriman)", "Chemistry=28 (<35). Triggers individual fail rule", "383 / 76.6%", "Grade F\nFAIL", "PASSED (Rule Verified)"),
        ("Threshold Boundary Pass", "Marks: 35, 40, 35, 50, 45\nRoll: 103 (Shivam)", "Exact 35.0 pass mark boundary tested on 2 subjects", "205 / 41.0%", "Grade E\nPASS", "PASSED (Pass Verified)"),
        ("Minimum Boundary (0 marks)", "Marks: 75, 80, 0, 70, 65\nRoll: 104 (Aarav)", "Chemistry=0.0 absolute minimum score", "290 / 58.0%", "Grade F\nFAIL", "PASSED (Rule Verified)"),
        ("Invalid & Non-Numeric Input", "Marks: -5, 105, 'xyz'\nRoll: -10, 'abc', duplicate 101", "Safely rejected, cleared buffer, re-prompted", "N/A", "Input Rejection", "PASSED (Zero Crash)")
    ]

    for r_idx, row in enumerate(test_data, start=1):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(241, 245, 249) if r_idx % 2 == 1 else COLOR_CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Arial"
            p.font.size = Pt(11)
            p.font.color.rgb = COLOR_TEXT_DARK
            if c_idx == 5:
                p.font.bold = True
                p.font.color.rgb = COLOR_ACCENT_GREEN

    # =========================================================================
    # SLIDE 7: CONCLUSION & FUTURE SCOPE
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_slide_header(s7, "Conclusion & Future Enhancements", "SUMMARY & ROADMAP")

    add_card(s7, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2),
             "Project Accomplishments", [
                 "• Fully Functional C Analyzer: Delivered an end-to-end, standard C menu-driven application adhering to GCC/MinGW standards with zero compiler warnings.",
                 "• Accurate Academic Compliance: Successfully enforces strict subject-wise passing thresholds alongside comprehensive overall grade scales.",
                 "• Enterprise-Grade Resilience: Robust handling of unexpected stdin tokens, edge boundaries, duplicate keys, and empty databases.",
                 "• Actionable Insights: Instantaneous calculation of class performance indices, pass ratios, and automatic topper selection."
             ], accent_color=COLOR_ACCENT_GREEN)

    add_card(s7, Inches(6.9), Inches(1.5), Inches(5.6), Inches(5.2),
             "Future Scope & Roadmap", [
                 "• Persistent Storage: Integrate file I/O (CSV / binary files) to save and reload records across program restarts.",
                 "• Configurable Grading Curves: Enable teachers to dynamically adjust subject pass marks and grading brackets.",
                 "• Graphical User Interface: Upgrade from CLI to a cross-platform desktop UI using Raylib or GTK.",
                 "• PDF / Report Card Generator: Direct export of formatted PDF report cards with institutional watermarks.",
                 "• Cloud / Database Sync: SQLite integration for multi-classroom institution-scale deployments."
             ], accent_color=COLOR_ACCENT_BLUE)

    # Save presentation
    prs.save(output_path)
    print(f"Presentation successfully saved to: {output_path}")

if __name__ == "__main__":
    out_ppt = r"C:\Users\Hp\.gemini\antigravity\scratch\Batch19_TeamAPEXFOUR_StudentResultAnalyzer\presentation.pptx"
    build_presentation(out_ppt)
