import os
import sys
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def create_sticker(style="new_year", text="Happy Meow Year", output_dir="assets/generated"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_style = "".join(c if c.isalnum() or c in ['-', '_'] else '_' for c in style.lower())
    filename = f"{safe_style}_sticker_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)

    # Canvas: transparent PNG
    width, height = 1024, 1024
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Try to load a font; fallback to default
    try:
        font_large = ImageFont.truetype("arial.ttf", 96)
        font_small = ImageFont.truetype("arial.ttf", 48)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Title (top)
    title = "Sunday Agent"
    title_w, title_h = draw.textbbox((0,0), title, font=font_small)[2:]
    draw.text(((width - title_w) / 2, 80), title, fill=(120,120,120,255), font=font_small)

    # Main text (center)
    lines = text.split("\n") if "\n" in text else [text]
    y = height // 2 - (len(lines) * 60)
    for line in lines:
        w, h = draw.textbbox((0,0), line, font=font_large)[2:]
        draw.text(((width - w) / 2, y), line, fill=(0,0,0,255), font=font_large)
        y += h + 20

    # Footer (style + timestamp)
    footer = f"style: {style} • {timestamp}"
    fw, fh = draw.textbbox((0,0), footer, font=font_small)[2:]
    draw.text(((width - fw) / 2, height - fh - 80), footer, fill=(90,90,90,255), font=font_small)

    img.save(filepath, "PNG")

    print(f"貼紙已儲存至: {filepath}")
    print(f"實際收到 style: '{style}'")
    print(f"實際收到 text : '{text}'")

if __name__ == "__main__":
    print("=== DEBUG: sys.argv 內容 ===")
    print(sys.argv)
    style = sys.argv[1].strip() if len(sys.argv) > 1 and sys.argv[1].strip() else "new_year"
    text = sys.argv[2].strip() if len(sys.argv) > 2 and sys.argv[2].strip() else "Happy Meow Year"
    create_sticker(style=style, text=text)
