from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
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
        time.sleep(60)
        download_speed = float(self.driver.find_element(By.XPATH, value ='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        upload_speed = float(self.driver.find_element(By.XPATH, value ='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        # print(download_speed)
        # print(upload_speed)
        if download_speed < self.down:
            return f"Heyy ACT!!!Brought {self.down}mbps plan but getting only {download_speed}mbps"

    def tweet_at_provider(self,tweet):
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

        next_button = self.driver.find_element(By.XPATH,value = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_button.click()

        time.sleep(5)
        try:
            username = self.driver.find_element(By.TAG_NAME,value="input")
            username.send_keys("FakeAccForPy")
            time.sleep(2)
            username.send_keys(Keys.ENTER)
            time.sleep(2)
            pass_input = self.driver.find_element(By.NAME, value="password")
            pass_input.send_keys(x_password)
            time.sleep(3)
            log_in = self.driver.find_element(By.XPATH,
                                              value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
            log_in.click()

        except ElementNotInteractableException:
            pass_input = self.driver.find_element(By.NAME,value="password")
            pass_input.send_keys(x_password)
            time.sleep(3)
            log_in = self.driver.find_element(By.XPATH,value = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
            log_in.click()
        time.sleep(13)
        tweet_input = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_input.click()
        time.sleep(2)
        tweet_input.send_keys(tweet)
        time.sleep(2)
        post = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post.click()


ist = InternetSpeedTwitterBot()
ist.tweet_at_provider(ist.get_internet_speed())
