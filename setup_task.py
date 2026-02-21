import os
import sys
import subprocess
import getpass

def install_task():
    print("=== Discord Laptop Notification Setup ===")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # path to the compiled
    exe_path = os.path.join(current_dir, "dist", "startup.exe")
    
    if not os.path.exists(exe_path):
        print(f"error: executable not found at {exe_path}")
        print("please compile startup.py with PyInstaller first: pyinstaller --noconsole --onefile startup.py")
        return

    task_name = "DiscordLaptopStartupNotification"
    user_name = getpass.getuser()
    
    # windows task scheduler command to run the executable silently (no black terminal) on system startup
    command = f'schtasks /Create /F /TN "{task_name}" /TR "\\"{exe_path}\\"" /SC ONSTART /RU "SYSTEM"'
    
    try:
        print("registering task in windows task scheduler...")
        
        # run and capture output
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"\n[SUCCESS] designed task '{task_name}' successfully")
            print("the script will now run silently in the background every time your system starts")
            print("\nIMPORTANT: make sure you have added your Webhook URL inside startup.py ")
        else:
            print(f"\n[FAILED] error creating task:\n{result.stderr}")
            print("you might need to right-click this script and 'Run as Administrator'")
    except Exception as e:
        print(f"an unexpected error occurred: {e}")

if __name__ == "__main__":
    install_task()
    input("\npress enter to exit...")
