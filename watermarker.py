import os
from PIL import Image, ImageDraw, ImageFont

def get_font(size):
    """
    Attempts to load a default font. Fallbacks to a basic loaded font if none found.
    """
    try:
        # Prioritize Google's "Roboto" (a clean, simple sans-serif like Google Sans)
        font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "Roboto-Regular.ttf")
        if os.path.exists(font_path):
            return ImageFont.truetype(font_path, size)
            
        # Try to load a standard system font fallback
        if os.name == 'nt':
            font_path = "arial.ttf"
        else:
            font_path = "/System/Library/Fonts/Helvetica.ttc"
        return ImageFont.truetype(font_path, size)
    except IOError as e:
        # Fallback to the default bitmap font
        print(f"Error loading truetype font: {e}")
        return ImageFont.load_default()

def process_output(image, output_path, compress):
    """
    Saves the image. Depending on the compress flag, it will either
    save with high quality (maintain resolution) or compress it.
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    # If standard JPEG, apply compression 
    ext = output_path.split('.')[-1].lower()
    
    if compress and ext in ['jpg', 'jpeg']:
        image.save(output_path, quality=60, optimize=True)
    elif compress and ext == 'png':
        # PNG compression (0-9)
        image.save(output_path, compress_level=9)
    else:
        # Maintain high quality
        if ext in ['jpg', 'jpeg']:
            image.save(output_path, quality=95, optimize=True)
        else:
            image.save(output_path)

def add_text_watermark(image_path, text, output_path, compress=False):
    """
    Adds a text watermark to the bottom right of the image.
    """
    try:
        with Image.open(image_path) as img:
            # Convert to RGBA to ensure we can handle transparency if needed
            watermarked = img.convert("RGBA")
            draw = ImageDraw.Draw(watermarked)
            
            # Calculate font size relative to image size (reduced to 1/5th of 0.09)
            width, height = watermarked.size
            font_size = int(height * 0.018)  # Changed from 0.09 to 0.018 (~1/5th size)
            font = get_font(font_size)
            
            # Calculate text size using the drawing context
            left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
            text_width = right - left
            text_height = bottom - top
            
            # Position: bottom right with 20px padding
            x = width - text_width - 20
            y = height - text_height - 20
            
            # Draw semi-transparent shadow (lowered opacity for blending)
            shadow_color = (0, 0, 0, 90)
            draw.text((x+2, y+2), text, font=font, fill=shadow_color)
            
            # Draw white text (~60% opacity for better photo blending)
            text_color = (255, 255, 255, 150)
            draw.text((x, y), text, font=font, fill=text_color)
            
            # Convert back to RGB if saving as JPEG
            ext = output_path.split('.')[-1].lower()
            if ext in ['jpg', 'jpeg']:
                watermarked = watermarked.convert("RGB")
                
            process_output(watermarked, output_path, compress)
            return True
    except Exception as e:
        print(f"Error adding text watermark: {e}")
        return False

def add_logo_watermark(image_path, logo_path, output_path, compress=False):
    """
    Adds an image logo watermark to the bottom right of the image.
    """
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGBA")
            width, height = img.size
            
            # Open logo
            with Image.open(logo_path) as logo:
                
                # Convert black background to transparent and apply 70% opacity
                # Using the grayscale luminance (L mode) as the alpha mask
                luma = logo.convert('L')
                
                # Create a solid white Image to be the color of the text
                transparent_logo = Image.new("RGBA", logo.size, (255, 255, 255, 0))
                
                # Scale the alpha mask by 0.70 to achieve 70% opacity
                alpha = luma.point(lambda p: int(p * 0.70))
                transparent_logo.putalpha(alpha)
                
                logo = transparent_logo
                
                # Resize logo to be relative to the image
                logo_target_width = int(width * 0.15)  # 15% of image width
                aspect_ratio = logo.size[1] / logo.size[0]
                logo_target_height = int(logo_target_width * aspect_ratio)
                
                logo = logo.resize((logo_target_width, logo_target_height), Image.Resampling.LANCZOS)
                
                # Setup position (bottom right)
                x = width - logo_target_width - 20
                y = height - logo_target_height - 20
                
                # Paste the logo using the logo itself as the mask for transparency
                img.paste(logo, (x, y), logo)
                
            # Convert back to RGB if saving as JPEG
            ext = output_path.split('.')[-1].lower()
            if ext in ['jpg', 'jpeg']:
                img = img.convert("RGB")
                
            process_output(img, output_path, compress)
            return True
            
    except Exception as e:
        print(f"Error adding logo watermark: {e}")
        return False
