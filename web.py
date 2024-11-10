from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep



def setup_browser():
	# Set up ChromeOptions (e.g., headless mode)
	chrome_options = Options()
	#chrome_options.add_argument("--headless")  # Optional: run in headless mode

	# Initialize the WebDriver with Service and Options
	service = Service("/usr/bin/chromedriver")  # Use Service to specify the driver path
	driver = webdriver.Chrome(service=service, options=chrome_options)  # Pass both Service and Options
	return driver

def play_youtube_video(link, driver):
	driver.get(link)
	sleep(10)
	#make window fullscreen
	driver.fullscreen_window()
	#get body for key presses
	body = driver.find_element("tag name","body")
	body.send_keys("f")
	body.send_keys(Keys.SPACE)
	return

	

