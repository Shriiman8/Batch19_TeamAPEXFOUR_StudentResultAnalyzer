"""
Generates a crisp, professional flowchart diagram for the Student Result and Grade Analyzer.
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_flowchart(output_path):
    # Dimensions and Palette
    width = 1200
    height = 1750
    bg_color = (248, 250, 252) # Slate-50
    card_bg = (255, 255, 255)
    border_color = (203, 213, 225) # Slate-300
    
    # Theme colors
    primary = (30, 58, 138)       # Deep Blue
    primary_light = (239, 246, 255) # Light Blue
    accent_green = (22, 101, 52)   # Emerald 800
    accent_green_bg = (240, 253, 244)
    accent_red = (153, 27, 27)     # Red 800
    accent_red_bg = (254, 242, 242)
    accent_amber = (180, 83, 9)    # Amber 700
    accent_amber_bg = (254, 252, 232)
    accent_purple = (107, 33, 168) # Purple 800
    accent_purple_bg = (250, 245, 255)
    line_color = (71, 85, 105)     # Slate 600
    text_dark = (15, 23, 42)       # Slate 900
    text_muted = (71, 85, 105)     # Slate 600

    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Try loading clean TrueType fonts, fallback to default
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 26)
        font_subtitle = ImageFont.truetype("arial.ttf", 15)
        font_box_header = ImageFont.truetype("arialbd.ttf", 15)
        font_box_text = ImageFont.truetype("arial.ttf", 13)
        font_badge = ImageFont.truetype("arialbd.ttf", 12)
    except:
        font_title = ImageFont.load_default()
        font_subtitle = font_title
        font_box_header = font_title
        font_box_text = font_title
        font_badge = font_title

    # Header Banner
    draw.rectangle([(0, 0), (width, 100)], fill=primary)
    draw.text((width // 2, 35), "STUDENT RESULT & GRADE ANALYZER - LOGIC FLOWCHART", fill=(255, 255, 255), font=font_title, anchor="mm")
    draw.text((width // 2, 70), "Batch: Batch - 19 | Team: APEX FOUR | Members: Daksh, Shriman Nautiyal, Shivam Rawat", fill=(226, 232, 240), font=font_subtitle, anchor="mm")

    # Helper function to draw rounded box
    def draw_box(x, y, w, h, bg, border, title, lines, title_color=text_dark):
        draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=10, fill=bg, outline=border, width=2)
        cur_y = y + 14
        if title:
            draw.text((x + w // 2, cur_y), title, fill=title_color, font=font_box_header, anchor="mm")
            cur_y += 18
            draw.line([(x + 15, cur_y), (x + w - 15, cur_y)], fill=border, width=1)
            cur_y += 12
        for line in lines:
            draw.text((x + w // 2, cur_y), line, fill=text_dark, font=font_box_text, anchor="mm")
            cur_y += 18

    # Helper function to draw arrow down
    def draw_arrow_down(x, y_start, y_end, label=""):
        draw.line([(x, y_start), (x, y_end)], fill=line_color, width=2)
        # arrowhead
        draw.polygon([(x - 5, y_end - 8), (x + 5, y_end - 8), (x, y_end)], fill=line_color)
        if label:
            draw.text((x + 8, (y_start + y_end) // 2), label, fill=line_color, font=font_badge, anchor="lm")

    # 1. Start Node
    start_x, start_y = width // 2, 130
    draw.rounded_rectangle([(start_x - 100, start_y), (start_x + 100, start_y + 40)], radius=20, fill=primary, outline=primary)
    draw.text((start_x, start_y + 20), "START PROGRAM", fill=(255, 255, 255), font=font_box_header, anchor="mm")

    draw_arrow_down(start_x, start_y + 40, start_y + 70)

    # 2. Main Menu
    menu_y = start_y + 70
    draw_box(start_x - 180, menu_y, 360, 95, primary_light, primary, "DISPLAY MAIN MENU (Loop)", [
        "1. Add Student Records",
        "2. View Summary Table | 3. Class Analytics",
        "4. Search by Roll No  | 5. Exit System"
    ], title_color=primary)

    draw_arrow_down(start_x, menu_y + 95, menu_y + 130)

    # 3. Input Choice Decision
    choice_y = menu_y + 130
    draw_box(start_x - 170, choice_y, 340, 75, accent_amber_bg, accent_amber, "GET USER CHOICE [1 - 5]", [
        "fgets() line buffer validation",
        "sscanf rejects chars / negatives / out-of-range"
    ], title_color=accent_amber)

    # Draw branch lines for choices
    branch_y = choice_y + 75 + 30
    draw.line([(start_x, choice_y + 75), (start_x, branch_y)], fill=line_color, width=2)
    # Horizontal distribution line
    draw.line([(180, branch_y), (1020, branch_y)], fill=line_color, width=2)

    # Connect to columns
    # Col 1: Choice 1 (Add Students) - x = 200
    # Col 2: Choice 2 (Summary Table) - x = 470
    # Col 3: Choice 3 (Analytics & Report) - x = 730
    # Col 4: Choice 4 & 5 (Search & Exit) - x = 990
    
    col_xs = [200, 470, 730, 990]
    for cx in col_xs:
        draw_arrow_down(cx, branch_y, branch_y + 35)

    # ================= COLUMN 1: CHOICE 1 (ADD STUDENTS & GRADING LOGIC) =================
    c1_y = branch_y + 35
    draw_box(col_xs[0] - 120, c1_y, 240, 90, card_bg, border_color, "[1] ADD STUDENTS", [
        "Enter count (1 to capacity)",
        "Prompt details per student",
        "Loop over each student"
    ])
    
    draw_arrow_down(col_xs[0], c1_y + 90, c1_y + 120)

    draw_box(col_xs[0] - 120, c1_y + 120, 240, 115, card_bg, border_color, "INPUT VALIDATION", [
        "- Roll No: Unique & > 0",
        "- Name: Non-empty string",
        "- 5 Subjects: Range [0 - 100]",
        "- Stdin buffer safely flushed"
    ])

    draw_arrow_down(col_xs[0], c1_y + 235, c1_y + 265)

    draw_box(col_xs[0] - 120, c1_y + 265, 240, 85, card_bg, border_color, "CALCULATE METRICS", [
        "totalMarks = Sum(marks[0..4])",
        "percentage = (total / 500) * 100",
        "Check each marks[i] >= 35"
    ])

    draw_arrow_down(col_xs[0], c1_y + 350, c1_y + 380)

    # Decision Diamond for Pass/Fail
    dia_y = c1_y + 380
    dia_cx, dia_cy = col_xs[0], dia_y + 45
    # Diamond shape
    draw.polygon([(dia_cx, dia_cy - 40), (dia_cx + 105, dia_cy), (dia_cx, dia_cy + 40), (dia_cx - 105, dia_cy)], 
                 fill=accent_purple_bg, outline=accent_purple, width=2)
    draw.text((dia_cx, dia_cy - 8), "ANY SUBJECT", fill=accent_purple, font=font_badge, anchor="mm")
    draw.text((dia_cx, dia_cy + 10), "MARKS < 35 ?", fill=accent_purple, font=font_badge, anchor="mm")

    # Diamond Branches: Left (YES - FAIL), Right (NO - PASS)
    fail_x = col_xs[0] - 80
    pass_x = col_xs[0] + 80
    res_y = dia_cy + 75

    # Fail branch
    draw.line([(dia_cx - 105, dia_cy), (fail_x, dia_cy), (fail_x, res_y)], fill=accent_red, width=2)
    draw_arrow_down(fail_x, dia_cy, res_y)
    draw.text((fail_x - 10, dia_cy - 12), "YES", fill=accent_red, font=font_badge, anchor="rm")
    draw_box(fail_x - 65, res_y, 130, 80, accent_red_bg, accent_red, "FAIL STATUS", [
        "isPassed = 0",
        "Grade = 'F'",
        "(Regardless of %)"
    ], title_color=accent_red)

    # Pass branch
    draw.line([(dia_cx + 105, dia_cy), (pass_x, dia_cy), (pass_x, res_y)], fill=accent_green, width=2)
    draw_arrow_down(pass_x, dia_cy, res_y)
    draw.text((pass_x + 10, dia_cy - 12), "NO", fill=accent_green, font=font_badge, anchor="lm")
    draw_box(pass_x - 65, res_y, 130, 80, accent_green_bg, accent_green, "PASS STATUS", [
        "isPassed = 1",
        "A+ (>=90), A (>=80)",
        "B, C, D, E (>=35)"
    ], title_color=accent_green)

    # Join back
    join_y = res_y + 115
    draw.line([(fail_x, res_y + 80), (fail_x, join_y), (col_xs[0], join_y)], fill=line_color, width=2)
    draw.line([(pass_x, res_y + 80), (pass_x, join_y), (col_xs[0], join_y)], fill=line_color, width=2)
    draw_box(col_xs[0] - 110, join_y + 10, 220, 60, card_bg, border_color, "RECORD STORED", [
        "Append to students[] array",
        "Increment studentCount"
    ])

    # ================= COLUMN 2: CHOICE 2 (RESULT SUMMARY TABLE) =================
    draw_box(col_xs[1] - 115, c1_y, 230, 90, card_bg, border_color, "[2] SUMMARY TABLE", [
        "Check: studentCount > 0",
        "If 0: Display empty warning",
        "Else: Render ASCII Table"
    ])
    draw_arrow_down(col_xs[1], c1_y + 90, c1_y + 130)

    draw_box(col_xs[1] - 115, c1_y + 130, 230, 160, card_bg, border_color, "TABLE COLUMNS", [
        "* Roll Number & Name",
        "* Sub 1 to Sub 5 Marks",
        "* Total Marks (out of 500)",
        "* Percentage (%)",
        "* Assigned Grade",
        "* Pass / Fail Status"
    ])

    # ================= COLUMN 3: CHOICE 3 (CLASS PERFORMANCE & TOPPER) =================
    draw_box(col_xs[2] - 115, c1_y, 230, 90, card_bg, border_color, "[3] CLASS REPORT", [
        "Check: studentCount > 0",
        "Iterate all records",
        "Aggregate statistics"
    ])
    draw_arrow_down(col_xs[2], c1_y + 90, c1_y + 130)

    draw_box(col_xs[2] - 115, c1_y + 130, 230, 200, card_bg, border_color, "ANALYTICS GENERATED", [
        "* Total Enrolled Students",
        "* Pass Count & Pass %",
        "* Fail Count & Fail %",
        "* Class Average %",
        "* Class Topper Identification",
        "  (Highest % among PASS)",
        "* Complete Grade Breakdown",
        "  (A+, A, B, C, D, E, F)"
    ])

    # ================= COLUMN 4: CHOICE 4 & 5 (SEARCH & EXIT) =================
    draw_box(col_xs[3] - 115, c1_y, 230, 140, card_bg, border_color, "[4] SEARCH STUDENT", [
        "Enter target Roll Number",
        "Linear search in array",
        "If Found: Display full scorecard",
        "  with per-subject status",
        "Else: Display 'Not Found'"
    ])
    draw_arrow_down(col_xs[3], c1_y + 140, c1_y + 180)

    draw_box(col_xs[3] - 115, c1_y + 180, 230, 110, card_bg, border_color, "[5] EXIT PROGRAM", [
        "Display Closing Credits",
        "Batch - 19 | APEX FOUR",
        "Set running = 0",
        "Graceful termination"
    ])

    # Bottom End Node
    end_y = 1630
    draw.rounded_rectangle([(start_x - 100, end_y), (start_x + 100, end_y + 40)], radius=20, fill=(71, 85, 105), outline=(71, 85, 105))
    draw.text((start_x, end_y + 20), "END PROGRAM", fill=(255, 255, 255), font=font_box_header, anchor="mm")

    # Connect columns back to Loop / End
    footer_line_y = 1580
    draw.line([(col_xs[0], join_y + 70), (col_xs[0], footer_line_y)], fill=line_color, width=2)
    draw.line([(col_xs[1], c1_y + 290), (col_xs[1], footer_line_y)], fill=line_color, width=2)
    draw.line([(col_xs[2], c1_y + 330), (col_xs[2], footer_line_y)], fill=line_color, width=2)
    draw.line([(col_xs[3], c1_y + 290), (col_xs[3], footer_line_y)], fill=line_color, width=2)
    draw.line([(col_xs[0], footer_line_y), (col_xs[3], footer_line_y)], fill=line_color, width=2)
    draw_arrow_down(start_x, footer_line_y, end_y, "Option 5 Chosen")

    # Save image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG", dpi=(300, 300))
    print(f"Flowchart successfully created at {output_path}")

if __name__ == "__main__":
    out = r"C:\Users\Hp\.gemini\antigravity\scratch\Batch19_TeamAPEXFOUR_StudentResultAnalyzer\screenshots\flowchart.png"
    create_flowchart(out)
