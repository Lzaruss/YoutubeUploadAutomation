## YouTube Studio Automation

This script utilizes the PyAutoGUI library to automate certain tasks in YouTube Studio. It is designed to simplify the process of changing and publishing videos on YouTube Studio.

### Features

- Automatically locates and interacts with specific elements on the YouTube Studio interface.
- Changes and publishes videos with a few simple steps.
- Supports batch processing of multiple videos.

### Requirements

- Python 3.x
- PyAutoGUI library

### Installation

1. Clone this repository or download the script file.
2. Install the required dependencies by running the following command:

`pip install pyautogui`


### Usage

1. Ensure that the YouTube Studio interface is visible on your screen.
2. Open a terminal or command prompt and navigate to the directory containing the script file.
3. Run the script.
4. The script will automatically locate the necessary elements on the YouTube Studio interface and perform the specified actions.

### Customization

- You can modify the `howManyVideos` variable in the script to specify the number of videos to process.
- Adjust the confidence level in the `goToImage()` function if you encounter issues with image recognition.

### Disclaimer

Please use this script responsibly and in compliance with YouTube's terms of service. Automating actions on YouTube may have implications on your account, and it is recommended to review and understand YouTube's policies before using this script.

### License

This script is released under the MIT License.

