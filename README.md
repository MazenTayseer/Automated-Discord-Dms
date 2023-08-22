# Automated Discord DMs
Automatically send a Discord message to all your friends with just one click!

## Prerequisites:
Before installing the application, ensure that you have:
- Python installed on your system. If not, [download and install Python](https://www.python.org/downloads/).
- Google Chrome browser updated to its latest version.

## Installation:
Follow the step-by-step guide below to set up the Automated Discord DMs application:

1. **Download and Extract**:
   - Download the provided zip file.
   - Extract the zip file to your preferred location on your computer.

2. **Install Required Packages**:
   - Open a terminal or command prompt.
   - Navigate to the extracted folder using the `cd` command.
   - Run the following command to install the necessary Python packages:
     ```
     pip install -r requirements.txt
     ```

3. **Modify `run.bat`** (Optional):
   - If you want to use the `run.bat` file to launch the application, open it using a text editor.
   - Replace `PATH_TO_Python.exe` with the path to your Python executable.
   - Replace `"PATH_TO_main.py"` with the path to the `main.py` file in the extracted folder.

4. **Running the Application**:
   - You can either run the `main.py` file directly or use the modified `run.bat` file.

## Usage:
1. **Launching**:
   - Run the application by executing the `main.py` file or by using the `run.bat` file.
   - The following interface will be displayed:
     ![Interface](https://user-images.githubusercontent.com/101992888/223509479-01ee9375-9ad1-4145-a6e2-e76c62d4b28d.png)

2. **Login Details**:
   - Input your Discord Email and Password.
   - Type the message you wish to send to your friends.

3. **Headless Mode**:
   - If you'd like the application to run without opening the browser window, check the `Run in background` option. This will use the headless mode of Chrome.

4. **Troubleshooting Login Issues**:
   - If you encounter the error: `[!] - FAILED TO LOG IN, WRONG CREDENTIALS OR RECAPTCHA APPEARED`, first ensure that your login credentials are accurate.
   - If the issue persists, uncheck the `Run in background` option and run the program. Manually complete the Captcha or Two Factor Authentication within the provided 240 seconds.
   - Once done, close the browser. Re-check the `Run in background` option and run the program again.

5. **Progress Tracking**:
   - As the program runs, you will see messages in the terminal indicating each successful message sent. Once all messages are sent, you'll see a **DONE** message.

## Keeping Chrome Updated:
It's crucial for the application's smooth functioning to have the latest Chrome version. Here's how you can ensure that:

1. Launch the Google Chrome browser on your computer.
2. Click on the three vertical dots at the top right corner (More options).
3. Navigate to `Help > About Google Chrome`.
4. If an update is available, you'll see the `Update Google Chrome` option. Click on it.
5. Once updated, click `Relaunch` to restart the browser.

## Contribution:
If you'd like to contribute to the development or improvement of this application, follow these steps:

1. **Fork the Repository**: Navigate to the GitHub repository page and click on the 'Fork' button at the top right.
2. **Clone the Forked Repository**: Once forked, clone the repository to your local machine.
3. **Make Changes**: Implement your features or make necessary changes.
4. **Submit a Pull Request**: Once done, push your changes to your forked repository and then submit a pull request. Your changes will be reviewed and, if deemed appropriate, will be merged.

## License:
This software is released under the MIT License. By using or contributing to this project, you agree to the terms and conditions of the license. Always ensure to use such tools responsibly and ethically, respecting the platform's terms of use.

## Final Notes:
Enjoy connecting with your friends on Discord seamlessly!
