import argparse
import os
from PIL import Image, ImageFilter, ImageDraw, ImageFont
from instagrapi import Client

def process_image(image_path, output_path="processed_image.jpg", watermark_text=None):
    """
    Processes an image for Instagram:
    - Resizes/pads to 4:5 aspect ratio with a blurred background.
    - Adds a watermark if provided.
    """
    try:
        img = Image.open(image_path).convert("RGB")
        width, height = img.size

        target_ratio = 4 / 5
        current_ratio = width / height

        target_width = width
        target_height = height

        if current_ratio > target_ratio:
            # Image is too wide, increase height
            target_height = int(width / target_ratio)
        else:
            # Image is too tall, increase width (or keep as is if it's already tall enough, but 4:5 is standard)
            target_width = int(height * target_ratio)

        # Create background (blurred version of original)
        background = img.resize((target_width, target_height))
        background = background.filter(ImageFilter.GaussianBlur(radius=20))

        # Paste original image in center
        offset = ((target_width - width) // 2, (target_height - height) // 2)
        background.paste(img, offset)

        # Add Watermark
        if watermark_text:
            # Convert to RGBA for transparency support
            background = background.convert("RGBA")
            overlay = Image.new("RGBA", background.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(overlay)

            # Load font (try default first)
            try:
                # Try to load a standard font, fallback to default
                font_size = int(target_height * 0.03) # 3% of height
                font = ImageFont.truetype("arial.ttf", font_size)
            except IOError:
                font = ImageFont.load_default()

            # Calculate text size using getbbox
            bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            # Position: Bottom Right with padding
            padding = 20
            x = target_width - text_width - padding
            y = target_height - text_height - padding

            # Draw semi-transparent background for text
            draw.rectangle(
                [x - 5, y - 5, x + text_width + 5, y + text_height + 5],
                fill=(0, 0, 0, 128)
            )
            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 255))

            # Composite and convert back to RGB
            background = Image.alpha_composite(background, overlay)
            background = background.convert("RGB")

        background.save(output_path, quality=95)
        print(f"Image processed and saved to {output_path}")
        return output_path

    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Instagram Post Tool with Smart Frame & Watermark")
    parser.add_argument("-u", "--username", help="Instagram Username")
    parser.add_argument("-p", "--password", help="Instagram Password")
    parser.add_argument("-i", "--image", required=True, help="Path to the image file")
    parser.add_argument("-c", "--caption", default="", help="Caption for the post")
    parser.add_argument("-w", "--watermark", help="Text for the watermark")
    parser.add_argument("--dry-run", action="store_true", help="Process image without uploading")

    args = parser.parse_args()

    processed_image = process_image(args.image, watermark_text=args.watermark)

    if not processed_image:
        print("Failed to process image.")
        return

    if args.dry_run:
        print("Dry run completed. Image saved locally.")
        return

    if not args.username or not args.password:
        print("Username and password are required for uploading (unless using --dry-run).")
        return

    print("Logging in to Instagram...")
    cl = Client()
    try:
        cl.login(args.username, args.password)
        print("Login successful!")

        print("Uploading photo...")
        media = cl.photo_upload(
            processed_image,
            caption=args.caption
        )
        print(f"Photo uploaded successfully! Media ID: {media.pk}")

    except Exception as e:
        print(f"Failed to upload: {e}")

    # Clean up processed image
    if os.path.exists(processed_image):
        os.remove(processed_image)

if __name__ == "__main__":
    main()
