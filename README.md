# Automated-Discord-Dms
An Application to send a Discord message to all your friends with one button click!

## How to Install
- Install [Python](https://www.python.org/downloads/).
- Download the zip file and extract it.
- Install the requirements file using `pip install -r requirements.txt`.
- Open the folder and run the `main.py` file.
- You can also run the `run.bat` file, but you have to modify it so it have `PATH_TO_Python.exe`  `"PATH_TO_main.py"`.

## How to Use
- When you run it, this screen will appear.
<img width="370" alt="image" src="https://user-images.githubusercontent.com/101992888/223509479-01ee9375-9ad1-4145-a6e2-e76c62d4b28d.png">

- Enter your Discord Email, Password, and the message you want to automatically send to all your friends.
- Check the `Run in background` box so that it runs `headless chrome` where you cannot see the tab opened.
- If you got the message `[!] - FAILED TO LOG IN, WRONG CREDENTIALS OR RECAPTCHA APPEARED`, please make sure your credentials are correct. 
  Otherwise, run the program again without checking the `Run in background` box, and complete the Captcha or the 2 Factor Authentication
  yourself (You will have 240 seconds), then close the browser and run it again while checking the `Run in background` box.
- You will have a terminal open, sending a message every time a message was sent, and **DONE** when the program finishes.
