import os
import pyfiglet
import time
import customtkinter
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from graphics.colors.bcolors import bcolors

SEND_THE_MESSAGE = True

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.resizable(False, False)
root.title("Automated Discord Messages")
root.iconbitmap("graphics/icons/icon.ico")
root.geometry("500x350")


def send_messages(driver, storedMessage):
    list_of_friends = driver.find_elements(
        By.XPATH, "//div[@class='listItemContents-2n2Uy9']")

    index = 0
    while index != len(list_of_friends):
        current_friend = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='listItemContents-2n2Uy9']"))
        )
        current_friend[index].click()
        time.sleep(1)

        message_friend = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@role='textbox']"))
        )
        message_friend.send_keys(storedMessage)
        time.sleep(1)
        message_check = message_friend.text

        if SEND_THE_MESSAGE:
            message_friend.send_keys(Keys.ENTER)

        print(bcolors.WARNING + f"[>] - MESSAGE SENT ({index + 1})")

        index += 1
        driver.back()
        time.sleep(1)

        list_of_friends = driver.find_elements(
            By.XPATH, "//div[@class='listItemContents-2n2Uy9']")


def log_in(driver, storedEmail, storedPassword):
    driver.get("https://discord.com/login")
    print(bcolors.OKGREEN + "[*] - OPENED THE WEBSITE")
    time.sleep(3)

    email = driver.find_element(By.NAME, "email")
    email.send_keys(storedEmail)

    password = driver.find_element(By.NAME, "password")
    password.send_keys(storedPassword)
    password.send_keys(Keys.ENTER)

    time.sleep(5)
    if driver.current_url != "https://discord.com/login":
        print(bcolors.OKGREEN + "[*] - LOGGED IN")
    else:
        print(bcolors.FAIL + "[!] - FAILED TO LOG IN, WRONG CREDENTIALS OR RECAPTCHA APPEARED")
        exit(1)

    friends_all = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='item-3mHhwr item-2GWPIy themed-qqoYp3']"))
    )
    friends_all.click()


def settings(stored_headless):
    CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
    GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome"

    op = uc.ChromeOptions()
    op.binary_location = os.environ.get(GOOGLE_CHROME_BIN)
    if stored_headless:
        op.add_argument("--headless=chrome")
    op.add_argument("--no-sandbox")
    op.add_argument("--disable-dev-sh-usage")
    op.add_argument('--disable-dev-shm-usage')
    op.add_argument("--start-maximized")
    func_driver = uc.Chrome(options=op, use_subprocess=True,
                            driver_executable_path=os.environ.get(CHROMEDRIVER_PATH))

    return func_driver


def start():
    store_email = user_email.get()
    store_password = user_password.get()
    store_message = message_to_friends.get()
    store_headless = headless_browser.get()

    if store_email != "" and store_message != "" and store_password != "":
        root.destroy()

        Name = pyfiglet.figlet_format("Mazen Tayseer")
        print(bcolors.OKBLUE + Name)

        driverIn = settings(stored_headless=store_headless)
        log_in(driver=driverIn, storedEmail=store_email, storedPassword=store_password)
        send_messages(driver=driverIn, storedMessage=store_message)

        print(bcolors.OKBLUE + pyfiglet.figlet_format("DONE"))


if __name__ == "__main__":
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Automated Discord Messages", font=("Roboto", 24), width=330)
    label.pack(pady=12, padx=10)

    user_email = customtkinter.CTkEntry(master=frame, placeholder_text="Email", width=330)
    user_email.pack(pady=12, padx=25, anchor="w")

    user_password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*", width=330)
    user_password.pack(pady=12, padx=25, anchor="w")

    message_to_friends = customtkinter.CTkEntry(master=frame, placeholder_text="Message", width=330)
    message_to_friends.pack(pady=12, padx=25, anchor="w")

    headless_browser = customtkinter.CTkCheckBox(master=frame, text="Run in background")
    headless_browser.pack(pady=12, padx=25, anchor="w")

    button = customtkinter.CTkButton(master=frame, text="Start", command=start, width=330)
    button.pack(pady=12, padx=25, anchor="w")

    root.mainloop()
