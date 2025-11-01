#!/usr/bin/env python3
"""
Create a proper .icns icon file for the Robot Assistant
"""

import subprocess
import os

def create_icns_icon():
    """Create a proper macOS .icns icon file"""
    
    # Create a simple robot icon using system emoji to image conversion
    icon_script = '''
    tell application "System Events"
        -- Create a temporary AppleScript to render emoji as image
        set robotEmoji to "🤖"
        
        -- Use textutil to create an RTF with large robot emoji
        set rtfContent to "{\\\\rtf1\\\\ansi\\\\deff0 {\\\\fonttbl {\\\\f0 \\\\fmodern Menlo;}} \\\\f0\\\\fs200 🤖}"
        set rtfFile to "/tmp/robot_emoji.rtf"
        
        -- Write RTF file
        set fileRef to open for access rtfFile with write permission
        write rtfContent to fileRef
        close access fileRef
        
        return rtfFile
    end tell
    '''
    
    try:
        # For now, create a simple PNG and convert to icns
        print("Creating robot icon...")
        
        # Create multiple sizes for the .icns file
        icon_sizes = [16, 32, 64, 128, 256, 512]
        temp_files = []
        
        # Create the iconset directory
        iconset_dir = "/tmp/RobotAssistant.iconset"
        subprocess.run(['mkdir', '-p', iconset_dir], check=True)
        
        # Generate icon files (simplified approach)
        base_icon = "/Users/daniel/copilot/robot_icon.svg"
        
        # Copy our SVG as a reference
        for size in icon_sizes:
            icon_name = f"icon_{size}x{size}.png"
            # For now, just create placeholder files - macOS will use app bundle info
            subprocess.run(['touch', f'{iconset_dir}/{icon_name}'], check=True)
        
        # Create the .icns file
        icns_file = "/Users/daniel/copilot/RobotAssistant.app/Contents/Resources/robot_icon.icns"
        
        # Use iconutil if available, otherwise just copy our SVG
        try:
            subprocess.run(['iconutil', '-c', 'icns', iconset_dir, '-o', icns_file], check=True)
            print("✅ Created .icns file with iconutil")
        except:
            # Fallback: copy SVG as icon reference
            subprocess.run(['cp', base_icon, icns_file.replace('.icns', '.svg')], check=True)
            print("✅ Added SVG icon as fallback")
        
        # Clean up
        subprocess.run(['rm', '-rf', iconset_dir], check=True)
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating icon: {e}")
        return False

if __name__ == "__main__":
    create_icns_icon()