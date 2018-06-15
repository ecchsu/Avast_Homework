from appium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class Homework(unittest.TestCase):

	page_load_time = 10
	run_func_time = 1200

	screenshotDir = '%s/' % os.getcwd()

	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '7.1.1'
		desired_caps['deviceName'] = 'Nexus 5 API 25'
		desired_caps['appPackage'] = 'com.avast.android.mobilesecurity'
		desired_caps['appActivity'] = 'app.main.MainActivity'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	def tearDown(self):
		self.driver.quit()

	def test_scan(self):
		''' Step:
			1. Launch Avast Antivirus 2108 
			2. Start scan
		'''
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/eula_accept').click()
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue').click()
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/main_progress_button_button').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
		self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
		wait_time = 0
		while True:
			try: 
				self.driver.find_element_by_xpath('//android.widget.Button[@text="RESCAN"]')
			except:
				wait_time += 1
				if wait_time == self.run_func_time:
					self.driver.save_screenshot(self.screenshotDir + 'test_scan.png')
					raise Exception('Scan failed')
			else:
				break

	def test_appVersionNotEmpty(self):
		''' Step:
			1. Launch Avast Antivirus 2108 
			2. Go to Settings>About
			3. Check app version
		'''
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/eula_accept').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue')))
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue').click()
		self.driver.find_element_by_accessibility_id('Open menu').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/drawer_promo_asl')))
		x = self.driver.get_window_size()['width']  
		y = self.driver.get_window_size()['height']
		self.driver.swipe(1/4*x, 6/7*y, 1/4*x, 2/7*y, 2000)
		self.driver.swipe(1/4*x, 6/7*y, 1/4*x, 2/7*y, 2000)
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/drawer_settings')))
		self.driver.find_element_by_id("com.avast.android.mobilesecurity:id/drawer_settings").click()
		self.driver.swipe(1/4*x, 6/7*y, 1/4*x, 2/7*y, 2000)
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="About"]')))
		self.driver.find_element_by_xpath("//android.widget.TextView[@text='About']").click()
		self.assertIsNotNone(self.driver.find_element_by_id("com.avast.android.mobilesecurity:id/settings_about_version"))

	def test_boostRam(self):
		''' Step:
			1. Launch Avast Antivirus 2108 
			2. Start boost Ram function
		'''
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/eula_accept').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue')))
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue').click()
		self.driver.find_element_by_xpath('//android.widget.TextView[@text="BOOST RAM"]').click()
		wait_time = 0
		while True:
			try: 
				self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/ui_feed_header_title')
			except:
				wait_time += 1
				if wait_time == self.run_func_time:
					self.driver.save_screenshot(self.screenshotDir + 'test_boostRam.png')
					raise Exception('Boost Ram function failed')
			else:
				break
		
	def test_cleanJunk(self):
		''' Step:
			1. Launch Avast Antivirus 2108 
			2. Start clean junk function
		'''
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/eula_accept').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue')))
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue').click()
		self.driver.find_element_by_xpath('//android.widget.TextView[@text="CLEAN JUNK"]').click()
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/cleanup_permission_button').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
		self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
		wait_time = 0
		while True:
			try: 
				self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/cleanup_safe_clean_button')
			except:
				wait_time += 1
				if wait_time == self.run_func_time:
					self.driver.save_screenshot(self.screenshotDir + 'test_cleanJunk.png')
					raise Exception('Clean junk function failed')
			else:
				break

	def test_scanWifi(self):
		''' Step:
			1. Launch Avast Antivirus 2108 
			2. Start scan Wi-Fi function
		'''
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/eula_accept').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue')))
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue').click()
		self.driver.find_element_by_xpath('//android.widget.TextView[@text="SCAN WI-FI"]').click()
		wait_time = 0
		while True:
			try:
				self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/ui_feed_header_title')
			except:
				wait_time += 1
				if wait_time == self.run_func_time:
					self.driver.save_screenshot(self.screenshotDir + 'test_cleanJunk.png')
					raise Exception('Scan Wi-Fi function failed')
			else:
				break

if __name__ == '__main__':
	suite = unittest.TestSuite()
	# suite.addTest(Homework('test_scan'))
	# suite.addTest(Homework('test_appVersionNotEmpty'))
	# suite.addTest(Homework('test_boostRam'))
	# suite.addTest(Homework('test_cleanJunk'))
	suite.addTest(Homework('test_scanWifi'))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)







