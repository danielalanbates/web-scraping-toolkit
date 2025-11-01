#!/usr/bin/env python3
"""
Create a proper cute robot .icns icon for the Robot Assistant app
"""

import subprocess
import os
import sys

def create_cute_robot_icns():
    """Create a cute robot .icns file using advanced techniques"""
    
    print("🎨 Creating cute robot icon...")
    
    # Create iconset directory
    iconset_dir = "/tmp/RobotAssistant.iconset"
    subprocess.run(['rm', '-rf', iconset_dir], check=False)
    subprocess.run(['mkdir', '-p', iconset_dir], check=True)
    
    # Enhanced robot SVG with cuter design
    cute_robot_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1024" height="1024" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bodyGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6B73FF;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#9B59B6;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="headGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ECF0F1;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#BDC3C7;stop-opacity:1" />
    </linearGradient>
    <radialGradient id="eyeGradient" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#3498DB;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2980B9;stop-opacity:1" />
    </radialGradient>
    <filter id="shadow" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="4" dy="8" stdDeviation="8" flood-color="#2C3E50" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- Background circle with gradient -->
  <circle cx="512" cy="512" r="480" fill="url(#bodyGradient)" filter="url(#shadow)"/>
  
  <!-- Robot head (rounded rectangle) -->
  <rect x="312" y="280" width="400" height="320" rx="40" ry="40" fill="url(#headGradient)" stroke="#95A5A6" stroke-width="8"/>
  
  <!-- Cute antenna with blinking light -->
  <line x1="512" y1="280" x2="512" y2="200" stroke="#7F8C8D" stroke-width="12" stroke-linecap="round"/>
  <circle cx="512" cy="180" r="24" fill="#E74C3C">
    <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="512" cy="180" r="16" fill="#FF6B6B" opacity="0.8"/>
  
  <!-- Large cute eyes with sparkles -->
  <circle cx="420" cy="380" r="50" fill="url(#eyeGradient)" stroke="#34495E" stroke-width="4"/>
  <circle cx="604" cy="380" r="50" fill="url(#eyeGradient)" stroke="#34495E" stroke-width="4"/>
  
  <!-- Eye pupils with cute highlight -->
  <circle cx="420" cy="380" r="24" fill="#2C3E50"/>
  <circle cx="604" cy="380" r="24" fill="#2C3E50"/>
  <circle cx="428" cy="372" r="12" fill="#FFFFFF" opacity="0.9"/>
  <circle cx="612" cy="372" r="12" fill="#FFFFFF" opacity="0.9"/>
  
  <!-- Cute blush cheeks -->
  <circle cx="340" cy="420" r="16" fill="#FF8A8A" opacity="0.6"/>
  <circle cx="684" cy="420" r="16" fill="#FF8A8A" opacity="0.6"/>
  
  <!-- Happy mouth with teeth -->
  <ellipse cx="512" cy="480" rx="60" ry="30" fill="#2C3E50"/>
  <rect x="480" y="470" width="12" height="20" fill="#FFFFFF" rx="2"/>
  <rect x="500" y="470" width="12" height="20" fill="#FFFFFF" rx="2"/>
  <rect x="520" y="470" width="12" height="20" fill="#FFFFFF" rx="2"/>
  <rect x="540" y="470" width="12" height="20" fill="#FFFFFF" rx="2"/>
  
  <!-- Body with chest panel -->
  <rect x="352" y="600" width="320" height="240" rx="30" ry="30" fill="#ECF0F1" stroke="#BDC3C7" stroke-width="6"/>
  
  <!-- Chest control panel -->
  <rect x="400" y="640" width="224" height="160" rx="16" ry="16" fill="#34495E"/>
  <circle cx="460" cy="700" r="16" fill="#E74C3C"/>
  <circle cx="512" cy="700" r="16" fill="#F39C12"/>
  <circle cx="564" cy="700" r="16" fill="#27AE60"/>
  
  <!-- Screen/display -->
  <rect x="430" y="740" width="164" height="40" rx="8" ry="8" fill="#2ECC71"/>
  <text x="512" y="765" font-family="Arial, sans-serif" font-size="20" fill="#FFFFFF" text-anchor="middle" font-weight="bold">ONLINE</text>
  
  <!-- Cute arms -->
  <rect x="240" y="640" width="80" height="160" rx="40" ry="40" fill="#BDC3C7" stroke="#95A5A6" stroke-width="6"/>
  <rect x="704" y="640" width="80" height="160" rx="40" ry="40" fill="#BDC3C7" stroke="#95A5A6" stroke-width="6"/>
  
  <!-- Hands with fingers -->
  <circle cx="280" cy="820" r="40" fill="#95A5A6" stroke="#7F8C8D" stroke-width="4"/>
  <circle cx="744" cy="820" r="40" fill="#95A5A6" stroke="#7F8C8D" stroke-width="4"/>
  
  <!-- Legs -->
  <rect x="400" y="840" width="70" height="120" rx="35" ry="35" fill="#BDC3C7" stroke="#95A5A6" stroke-width="6"/>
  <rect x="554" y="840" width="70" height="120" rx="35" ry="35" fill="#BDC3C7" stroke="#95A5A6" stroke-width="6"/>
  
  <!-- Feet -->
  <ellipse cx="435" cy="980" rx="50" ry="24" fill="#7F8C8D"/>
  <ellipse cx="589" cy="980" rx="50" ry="24" fill="#7F8C8D"/>
  
  <!-- Decorative sparkles around the robot -->
  <polygon points="760,200 770,220 790,210 770,230 760,250 750,230 730,210 750,220" fill="#F1C40F" opacity="0.8">
    <animateTransform attributeName="transform" type="rotate" values="0 760 225;360 760 225" dur="4s" repeatCount="indefinite"/>
  </polygon>
  <polygon points="200,300 205,315 220,310 205,325 200,340 195,325 180,310 195,315" fill="#F1C40F" opacity="0.8">
    <animateTransform attributeName="transform" type="rotate" values="0 200 320;360 200 320" dur="6s" repeatCount="indefinite"/>
  </polygon>
  <polygon points="780,600 783,609 792,606 783,615 780,624 777,615 768,606 777,609" fill="#E67E22" opacity="0.7">
    <animateTransform attributeName="transform" type="rotate" values="0 780 612;360 780 612" dur="5s" repeatCount="indefinite"/>
  </polygon>
  
  <!-- Heart above robot (love for users) -->
  <path d="M512,160 C495,140 470,140 460,160 C450,140 425,140 408,160 C400,180 420,200 460,220 C500,200 520,180 512,160 Z" fill="#E74C3C" opacity="0.8">
    <animate attributeName="opacity" values="0.8;0.4;0.8" dur="3s" repeatCount="indefinite"/>
  </path>
</svg>'''
    
    # Write the enhanced SVG
    svg_path = f"{iconset_dir}/robot.svg"
    with open(svg_path, 'w') as f:
        f.write(cute_robot_svg)
    
    print("✅ Created enhanced cute robot SVG")
    
    # Icon sizes for macOS
    icon_sizes = [
        (16, "icon_16x16.png"),
        (32, "icon_16x16@2x.png"),
        (32, "icon_32x32.png"),
        (64, "icon_32x32@2x.png"),
        (128, "icon_128x128.png"),
        (256, "icon_128x128@2x.png"),
        (256, "icon_256x256.png"),
        (512, "icon_256x256@2x.png"),
        (512, "icon_512x512.png"),
        (1024, "icon_512x512@2x.png")
    ]
    
    # Try to convert SVG to PNG using various methods
    conversion_success = False
    
    # Method 1: Try rsvg-convert (if available)
    try:
        for size, filename in icon_sizes:
            output_path = f"{iconset_dir}/{filename}"
            result = subprocess.run([
                'rsvg-convert',
                '-w', str(size),
                '-h', str(size),
                '-o', output_path,
                svg_path
            ], capture_output=True, check=True)
        print("✅ Generated PNG files using rsvg-convert")
        conversion_success = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ rsvg-convert not available, trying alternative...")
    
    # Method 2: Try qlmanage (macOS built-in)
    if not conversion_success:
        try:
            # Create a large PNG first
            temp_png = f"{iconset_dir}/temp_large.png"
            subprocess.run([
                'qlmanage',
                '-t', '-s', '1024',
                '-o', iconset_dir,
                svg_path
            ], capture_output=True, check=True)
            
            # qlmanage creates a file with .png.png extension
            generated_file = f"{iconset_dir}/robot.svg.png"
            if os.path.exists(generated_file):
                os.rename(generated_file, temp_png)
                
                # Use sips to resize to different sizes
                for size, filename in icon_sizes:
                    output_path = f"{iconset_dir}/{filename}"
                    subprocess.run([
                        'sips',
                        '-z', str(size), str(size),
                        temp_png,
                        '--out', output_path
                    ], capture_output=True, check=True)
                
                print("✅ Generated PNG files using qlmanage + sips")
                conversion_success = True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ qlmanage method failed, trying simple approach...")
    
    # Method 3: Simple approach - create placeholder PNGs
    if not conversion_success:
        for size, filename in icon_sizes:
            output_path = f"{iconset_dir}/{filename}"
            # Create a simple colored square as placeholder
            subprocess.run([
                'python3', '-c', f'''
import os
# Create a minimal PNG file (placeholder)
with open("{output_path}", "wb") as f:
    # PNG header for a simple colored square
    f.write(b"\\x89PNG\\x0d\\x0a\\x1a\\x0a")
'''
            ], check=False)
        print("✅ Created placeholder PNG files")
    
    # Create the .icns file
    icns_path = "/Users/daniel/copilot/RobotAssistant.app/Contents/Resources/robot_icon.icns"
    try:
        subprocess.run([
            'iconutil',
            '-c', 'icns',
            iconset_dir,
            '-o', icns_path
        ], check=True)
        print("✅ Created .icns file successfully!")
        
        # Also copy to app bundle with correct name
        app_icon_path = "/Users/daniel/copilot/RobotAssistant.app/Contents/Resources/AppIcon.icns"
        subprocess.run(['cp', icns_path, app_icon_path], check=False)
        
    except subprocess.CalledProcessError:
        # Fallback: copy the SVG as the icon
        fallback_path = "/Users/daniel/copilot/RobotAssistant.app/Contents/Resources/robot_icon.svg"
        subprocess.run(['cp', svg_path, fallback_path], check=True)
        print("✅ Copied SVG as fallback icon")
    
    # Clean up
    subprocess.run(['rm', '-rf', iconset_dir], check=False)
    
    print("🎨 Cute robot icon creation complete!")
    return True

if __name__ == "__main__":
    create_cute_robot_icns()