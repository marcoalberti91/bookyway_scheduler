import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
import os

# Import the test data
from test_data import test_lessons  

# Load environment variables from .env file
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

class TestSkipBurpees():
  def setup_method(self, method):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280,1024')
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
    print("Starting Chromedriver in headless mode")
  
  def teardown_method(self, method):
    self.driver.quit()
    print("Closing Chromdriver")

  def wait_for_element(self, by, value, timeout=30):
      try:
          return WebDriverWait(self.driver, timeout).until(
              EC.visibility_of_element_located((by, value))
          )
      except TimeoutException:
          raise TimeoutException(f"Element not found: (By.{by}, {value}) after {timeout} seconds")
  
  @pytest.mark.parametrize("day, hour, lesson_type", test_lessons)

  def test_book_lesson(self, day, hour, lesson_type):
      # Open BookyWay app
      self.driver.get("https://m.bookyway.com/#/login")
      self.driver.set_window_size(430, 932)
      time.sleep(2)
      
      # Login
      username = self.wait_for_element(By.ID, "loginuser")
      username.click()
      username.send_keys(EMAIL)
      
      password = self.wait_for_element(By.ID, "loginpassowrd")
      password.click()
      password.send_keys(PASSWORD)

      self.wait_for_element(By.ID, "loginbutton").click()

      # Book course
      card = self.wait_for_element(By.XPATH, "//a[@class='c-card__link']")
      card.click()

      course_xpath = f"//div[@class='schedule-item__details' and .//span[text()='{lesson_type}'] and .//span[contains(text(), '{day}')]/following-sibling::span[contains(text(), '{hour}')]]"
      course = self.wait_for_element(By.XPATH, course_xpath)
      booking_text = course.text

      if "BOOKED" in booking_text:
          print(f"The {lesson_type} class on {day} at {hour} is already booked.")
      else:
          print(f"The {lesson_type} class on {day} at {hour} is not booked. Performing new booking.")
          course.click()
          print(f"Verifying correct course: Corso di {lesson_type}")
          self.wait_for_element(By.XPATH, f"//span[text()='Corso di {lesson_type}']")

          # Check if the "Unsubscribe" button exists
          unsubscribe_button = self.driver.find_elements(By.XPATH, "//span[text()='Unsubscribe']")
          
          if unsubscribe_button:
              print("Already subscribed")
          else:
              print("Not subscribed. Start new booking...")
              book_button = self.wait_for_element(By.XPATH, "//span[text()='Book']")
              book_button.click()
              print("Clicked on Subscribe")
              ok_button = self.wait_for_element(By.XPATH, "//button[text()='Ok']")
              ok_button.click()
              print("Confirmed selection")
