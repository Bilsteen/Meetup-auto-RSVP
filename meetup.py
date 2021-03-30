from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
from scrape import get_events_links

class Browser():
	def __init__(self,link,email,password):
		self.chrome_browser = webdriver.Chrome("./chromedriver")
		self.chrome_browser.get("https://www.meetup.com"+link)
		self.email = email
		self.password = password

	def attend_meetup(self):
		"""
		This function is used for making an RSVP to the event
		"""
		sleep(6)
		attend_button = self.chrome_browser.find_element_by_xpath("//button[@data-swarm-button='primary']")
		attend_button.click()
		self.__fb_login__()
		self.chrome_browser.close()

	def __fb_login__(self):
		"""
		This function is used for logging in on the meetup website using a facebook account 
		"""
		sleep(6)
		fb = self.chrome_browser.find_element_by_class_name("signUpModal-facebook")
		fb.click()
		sleep(6)
		email_box = self.chrome_browser.find_element_by_id("email")
		email_box.send_keys(self.email)
		sleep(6)
		password_box = self.chrome_browser.find_element_by_id("pass")
		password_box.send_keys(self.password)
		sleep(6)
		login_button = self.chrome_browser.find_element_by_id("loginbutton")
		login_button.click()
		sleep(30)

if __name__ == "__main__":
	"""
	Every 30 minutes a check has been made whether new events have been added 
	by the group 
	"""
	email = input("Enter your facebook email-id: ")
	password = input("Enter your facebook password: ")
	while True:
		link_check = {}
		for link in get_events_links("https://www.meetup.com/Mumbai-Travel-Club/events/"):
			if link_check.get(link):
				continue
			link_check[link] = True
			browser_instance = Browser(link,email,password)
			browser_instance.attend_meetup()
			sleep(6)
		sleep(30*60)
