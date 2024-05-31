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