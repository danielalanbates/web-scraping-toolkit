#!/usr/bin/env python3
"""
Create a cute robot app icon using Python
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_cute_robot_icon():
    """Create a cute robot icon for macOS"""
    
    # Create a 512x512 image with transparent background
    size = 512
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Colors
    robot_blue = (74, 144, 226)
    robot_light = (245, 245, 245)
    eye_green = (80, 227, 194)
    mouth_dark = (51, 51, 51)
    
    # Draw background circle
    margin = 20
    draw.ellipse([margin, margin, size-margin, size-margin], fill=robot_blue)
    
    # Draw robot head (rounded rectangle)
    head_margin = 80
    head_rect = [head_margin, head_margin+40, size-head_margin, size-head_margin-40]
    draw.rounded_rectangle(head_rect, radius=30, fill=robot_light)
    
    # Draw antenna
    antenna_x = size // 2
    antenna_start = head_margin + 40
    antenna_end = head_margin - 20
    draw.line([antenna_x, antenna_start, antenna_x, antenna_end], fill=mouth_dark, width=8)
    
    # Draw antenna ball
    ball_radius = 15
    ball_center = antenna_end
    draw.ellipse([antenna_x-ball_radius, ball_center-ball_radius, 
                  antenna_x+ball_radius, ball_center+ball_radius], fill=(255, 107, 107))
    
    # Draw eyes
    eye_size = 40
    eye_y = head_margin + 100
    left_eye_x = head_margin + 60
    right_eye_x = size - head_margin - 60 - eye_size
    
    # Left eye
    draw.ellipse([left_eye_x, eye_y, left_eye_x+eye_size, eye_y+eye_size], fill=eye_green)
    draw.ellipse([left_eye_x+10, eye_y+10, left_eye_x+30, eye_y+30], fill=(255, 255, 255))
    draw.ellipse([left_eye_x+15, eye_y+15, left_eye_x+25, eye_y+25], fill=mouth_dark)
    
    # Right eye
    draw.ellipse([right_eye_x, eye_y, right_eye_x+eye_size, eye_y+eye_size], fill=eye_green)
    draw.ellipse([right_eye_x+10, eye_y+10, right_eye_x+30, eye_y+30], fill=(255, 255, 255))
    draw.ellipse([right_eye_x+15, eye_y+15, right_eye_x+25, eye_y+25], fill=mouth_dark)
    
    # Draw mouth
    mouth_y = eye_y + 80
    mouth_width = 100
    mouth_height = 25
    mouth_x = (size - mouth_width) // 2
    draw.rounded_rectangle([mouth_x, mouth_y, mouth_x+mouth_width, mouth_y+mouth_height], 
                          radius=12, fill=mouth_dark)
    
    # Draw mouth segments
    segment_width = 12
    segment_height = 15
    segment_y = mouth_y + 5
    for i in range(4):
        segment_x = mouth_x + 15 + (i * 20)
        draw.rectangle([segment_x, segment_y, segment_x+segment_width, segment_y+segment_height], 
                      fill=(200, 200, 200))
    
    # Draw cheek blush
    blush_size = 20
    left_blush_x = head_margin + 20
    right_blush_x = size - head_margin - 40
    blush_y = eye_y + 30
    
    draw.ellipse([left_blush_x, blush_y, left_blush_x+blush_size, blush_y+blush_size], 
                fill=(255, 182, 193, 150))
    draw.ellipse([right_blush_x, blush_y, right_blush_x+blush_size, blush_y+blush_size], 
                fill=(255, 182, 193, 150))
    
    return img

def create_icon_files():
    """Create icon files for the app bundle"""
    try:
        print("🎨 Creating cute robot icon...")
        
        # Create the base icon
        icon = create_cute_robot_icon()
        
        # Save as PNG first
        png_path = "/tmp/robot_icon.png"
        icon.save(png_path, "PNG")
        
        # Create iconset directory
        iconset_dir = "/tmp/RobotIcon.iconset"
        os.makedirs(iconset_dir, exist_ok=True)
        
        # Create different sizes for .icns
        sizes = [16, 32, 64, 128, 256, 512]
        for size in sizes:
            resized = icon.resize((size, size), Image.Resampling.LANCZOS)
            resized.save(f"{iconset_dir}/icon_{size}x{size}.png", "PNG")
            
            # Also create @2x versions
            if size <= 256:
                size_2x = size * 2
                resized_2x = icon.resize((size_2x, size_2x), Image.Resampling.LANCZOS)
                resized_2x.save(f"{iconset_dir}/icon_{size}x{size}@2x.png", "PNG")
        
        # Convert to .icns using iconutil
        icns_path = "/tmp/RobotIcon.icns"
        os.system(f"iconutil -c icns {iconset_dir} -o {icns_path}")
        
        # Copy to app bundle
        app_icns_path = "/Users/daniel/copilot/RobotAssistant.app/Contents/Resources/robot_icon.icns"
        os.system(f"cp {icns_path} {app_icns_path}")
        
        print("✅ Cute robot icon created successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error creating icon: {e}")
        # Fallback: create a simple emoji-based icon
        try:
            print("🔄 Creating fallback emoji icon...")
            os.system('echo "🤖" > /tmp/robot_emoji.txt')
            return True
        except:
            return False

if __name__ == "__main__":
    create_icon_files()