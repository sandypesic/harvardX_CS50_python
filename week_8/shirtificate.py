import os
from fpdf import FPDF


def main():
    name = input("Name: ")
    generate_shirtificate(name)


def generate_shirtificate(name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "shirtificate.png")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("Arial", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 20, "CS50 Shirtificate", ln=True, align="C")

    image_width = 100
    x = (210 - image_width) / 2
    y = 80
    pdf.image(image_path, x=x, y=y, w=image_width)

    pdf.set_font("Arial", "B", 12)
    text = f"{name} took CS50"
    text_y = y + 45
    pdf.set_xy(0, text_y)
    pdf.cell(210, 10, text, align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()