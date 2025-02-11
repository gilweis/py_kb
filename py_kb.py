import argparse
import time
import pyautogui
import pygetwindow as gw


# Function to find and activate a window
def activate_window(window_title: str) -> bool:
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        target_window = windows[0]
        target_window.activate()
        time.sleep(1)  # Give time for the window to come to the foreground
        return True
    return False


# Function to type content from a file
def type_from_file(file_path: str, interval: float) -> None:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Simulate typing
        pyautogui.write(content, interval)  # Adjust interval for speed control
    except Exception as e:
        print(f"Error reading file: {e}")


# Main function
def main():
    """main()"""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='pyget_chain')
    parser.add_argument('--infile', type=str, required=True, help='Input filename')
    parser.add_argument('--win_title', type=str, required=True, help='Window title')
    parser.add_argument('--interval', type=float, default=0.05, help='interval')

    args: argparse.Namespace = parser.parse_args()

    if activate_window(args.win_title):
        type_from_file(args.infile, args.interval)
    else:
        print(f"Window '{args.win_title}' not found. Make sure the application is open.")


# Run the script
if __name__ == "__main__":
    main()
