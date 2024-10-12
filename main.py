from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time
load_dotenv("C:/Python/Environmental variables/.env")
x_email = os.getenv("x_email")
x_password = os.getenv("x_password")
class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 10
        self.down = 75
        self.test_url = "https://www.speedtest.net/"
        self.twitter_url = "https://x.com/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
    def get_internet_speed(self):
        self.driver.get(self.test_url)
        time.sleep(5)
        start = self.driver.find_element(By.CLASS_NAME, value="js-start-test")
        start.click()
        time.sleep(40)
        try:
            download_speed = float(self.driver.find_element(By.XPATH, value ='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
            upload_speed = float(self.driver.find_element(By.XPATH, value ='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
            print(download_speed)
            print(upload_speed)
            if download_speed < self.down:
                print(f"Brought {self.down}mbps plan but getting only {download_speed}mbps")
        except NoSuchElementException:
            time.sleep(10)

    def tweet_at_provider(self):
        self.driver.get(self.twitter_url)
        time.sleep(3)
        sign_in = self.driver.find_element(By.LINK_TEXT,value="Sign in")
        sign_in.click()
        time.sleep(5)
        # base_window = self.driver.window_handles[0]
        # x_login_window = self.driver.window_handles[1]
        # self.driver.switch_to.window(x_login_window)
        # print(self.driver.title)
        email = self.driver.find_element(By.TAG_NAME,value="input")
        email.send_keys(x_email)


ist = InternetSpeedTwitterBot()
ist.tweet_at_provider()
