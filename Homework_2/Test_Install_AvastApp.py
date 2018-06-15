from appium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class Homework(unittest.TestCase):

	page_load_time = 5
	run_func_time = 1200
	screenshotDir = '%s/' % os.getcwd()

	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '7.1.1'
		desired_caps['deviceName'] = 'Nexus 5 API 25'
		desired_caps['appPackage'] = 'com.android.vending'
		desired_caps['appActivity'] = 'AssetBrowserActivity'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	def tearDown(self):
		self.driver.quit()

	def	test_installAvastAntivirus(self):
		''' Step:
			1. Download Avast Antivirus 2108 from Google Play Store
			2. After installation completes, launch app
		'''
		WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, 'com.android.vending:id/search_box_idle_text')))
		self.driver.find_element_by_id('com.android.vending:id/search_box_idle_text').click()
		self.driver.find_element_by_id('com.android.vending:id/search_box_text_input').send_keys('avast antivirus'+'\n')
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="INSTALL"]')))
		self.driver.find_element_by_xpath('//android.widget.Button[@text="INSTALL"]').click()
		wait_time = 0
		while True:
			try: 
				self.driver.find_element_by_xpath('//android.widget.Button[@text="OPEN"]')
			except:
				wait_time += 1
				if wait_time == self.run_func_time:
					self.driver.save_screenshot(self.screenshotDir + 'test_installAvastAntivirus.png')
					raise Exception('Download/install failed')
			else:
				break

		#launch app and setting
		self.driver.press_keycode(3)
		self.driver.find_element_by_id('com.google.android.apps.nexuslauncher:id/all_apps_handle').click()
		self.driver.find_element_by_accessibility_id("Avast Mobile Security").click()
		try: 
			self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/eula_accept').click()
			WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue')))
			self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue').click()
			self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/main_progress_button_button')
		except:
			self.driver.save_screenshot(self.screenshotDir + 'test_installAvastAntivirus.png')
			raise Exception('Launch failed')

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(Homework('test_installAvastAntivirus'))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)
