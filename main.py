from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
import time

CHROME_DRIVER_PATH = r"C:\Users\ARJUN RAHUL VIJI\OneDrive\Documents\chromedriver_win32\chromedriver.exe"
SIMILAR_ACCOUNT = "herhelloworld" # You can choose your favourite Instagram Page
USERNAME = "<registered-username>"
PASSWORD = "<email id>"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))

    def login(self):
        INSTA = "https://www.instagram.com/accounts/login/"
        link = self.driver.get(INSTA)
        time.sleep(2)
        username = self.driver.find_element(By.NAME , 'username')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        time.sleep(2)
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(15)
        # notifs = self.driver.find_element(By.CSS_SELECTOR, 'button[class="_a9-- _a9_0"]')     # IF SUDDEN NOTIFICATION POPUPS POPUP, USE THIS
        # notifs.click()

    def find_followers(self):
        page = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"
        self.driver.get(page)
        time.sleep(5)
        followers = self.driver.find_element(By.CSS_SELECTOR, 'li a')
        followers.click()
        time.sleep(5)
        # notifs = self.driver.find_element(By.CSS_SELECTOR, 'button[class="_a9-- _a9_0"]') # SAME POPUP
        # notifs.click()
        scr1 = self.driver.find_element(By.CSS_SELECTOR, 'div[class="_aano"')
        for i in range(10):
            self.follow()
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(6)
        # notifs = self.driver.find_element(By.CSS_SELECTOR, 'button[class="_a9-- _a9_0"]') # AGAIN
        # notifs.click()

    def follow(self):
        time.sleep(5)
        follow_action = self.driver.find_elements(By.CSS_SELECTOR,'div[class="_aacl _aaco _aacw _aad6 _aade"]')
        for t in follow_action:
            try:
                t.click()
                time.sleep(2)

            except ElementClickInterceptedException:
                # cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                # cancel_button.click()         # THIS LINE OF CODE IS BUGGED OUT
                continue


i = InstaFollower()
i.login()
time.sleep(2)
i.find_followers()
time.sleep(3)


