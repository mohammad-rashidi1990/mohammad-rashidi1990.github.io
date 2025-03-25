from PIL import Image, ImageDraw, ImageFont

def generate_logo(text="STEM Tutor Hub", filename="stemtutorhub_logo_free.png"):
    # Image size and background color
    width, height = 1024, 512
    background_color = "white"
    text_color = "black"

    # Create image
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 80)  # Windows font
    except:
        font = ImageFont.load_default()

    # Calculate text size using textbbox (Pillow 10+)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center the text
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Draw text
    draw.text((x, y), text, fill=text_color, font=font)

    # Save image
    image.save(filename)
    print(f"✅ Logo saved as: {filename}")

if __name__ == "__main__":
    generate_logo()
