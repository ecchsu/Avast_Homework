from appium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import HTMLReport
import time
from HTMLReport import logger

class Homework(unittest.TestCase):

	page_load_time = 10
	run_func_time = 1200

	screenshotDir = '%s//report//' % os.getcwd()
	timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

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
		'''To test scan function can complete successfully'''
		logger().info("Launch Avast Antivirus 2018 app")
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/eula_accept').click()
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue').click()
		logger().info("Entered main page")
		logger().info("Click scan button")
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/main_progress_button_button').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
		logger().info("Click permission confirm button")
		self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
		logger().info("Scan started")
		wait_time = 0
		while True:
			try: 
				self.driver.find_element_by_xpath('//android.widget.Button[@text="RESCAN"]')
				logger().info("Scan completed")
				self.driver.save_screenshot(self.screenshotDir + 'test_scan %s.png' % self.timestr)
			except:
				wait_time += 1
				if wait_time == self.run_func_time:
					logger().info("Scan failed")
					self.driver.save_screenshot(self.screenshotDir + 'test_scan %s.png' % self.timestr)
					raise Exception('Scan failed')
			else:
				break
		self.assertIsNotNone(self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/ui_feed_header_title'))
		self.assertIsNotNone(self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/ui_feed_header_subtitle'))

	def test_appVersionNotEmpty(self):
		''' Check version is not empty'''
		logger().info("Launch app")
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/eula_accept').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue')))
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue').click()
		logger().info("Entered main page")
		self.driver.find_element_by_accessibility_id('Open menu').click()
		logger().info("Clicked menu button")
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/drawer_promo_asl')))
		x = self.driver.get_window_size()['width']  
		y = self.driver.get_window_size()['height']
		self.driver.swipe(1/4*x, 6/7*y, 1/4*x, 2/7*y, 2000)
		self.driver.swipe(1/4*x, 6/7*y, 1/4*x, 2/7*y, 2000)
		logger().info("Scrolled down to the bottom of the list")
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/drawer_settings')))
		self.driver.find_element_by_id("com.avast.android.mobilesecurity:id/drawer_settings").click()
		logger().info("Entered Settings page")
		self.driver.swipe(1/4*x, 6/7*y, 1/4*x, 2/7*y, 2000)
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="About"]')))
		self.driver.find_element_by_xpath("//android.widget.TextView[@text='About']").click()
		logger().info("Entered About page")
		self.driver.save_screenshot(self.screenshotDir + 'test_appVersionNotEmpty %s.png' % self.timestr)
		self.assertIsNotNone(self.driver.find_element_by_id("com.avast.android.mobilesecurity:id/settings_about_version"))
		logger().info("Checked app version")

	def test_boostRam(self):
		'''To perform kill-task function'''
		logger().info("Launch app")
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/eula_accept').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue')))
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue').click()
		logger().info("Entered main page")
		self.driver.find_element_by_xpath('//android.widget.TextView[@text="BOOST RAM"]').click()
		logger().info("Boost RAM function started")
		wait_time = 0
		while True:
			try: 
				self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/ui_feed_header_icon')
				logger().info("Boost RAM function completed")
				self.driver.save_screenshot(self.screenshotDir + 'test_boostRam %s.png' % self.timestr)
			except:
				wait_time += 1
				if wait_time == self.run_func_time:
					logger().info("Boost RAM function failed")
					self.driver.save_screenshot(self.screenshotDir + 'test_boostRam %s.png' % self.timestr)
					raise Exception('Boost Ram function failed')
			else:
				break
		self.assertIsNotNone(self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/ui_feed_header_title'))
		self.assertIsNotNone(self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/ui_feed_header_subtitle'))

	def test_cleanJunk(self):
		'''To test cleaning function'''
		logger().info("Launch app")
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/eula_accept').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue')))
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue').click()
		logger().info("Entered main page")
		self.driver.find_element_by_xpath('//android.widget.TextView[@text="CLEAN JUNK"]').click()
		logger().info("Clicked Clean Junk button")
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/cleanup_permission_button').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
		self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
		logger().info("Granted permission")
		logger().info("Clean junk function started")
		wait_time = 0
		while True:
			try: 
				self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/cleanup_safe_clean_button')
				logger().info("Clean junk function completed")
				self.driver.save_screenshot(self.screenshotDir + 'test_cleanJunk %s.png' % self.timestr)
			except:
				wait_time += 1
				if wait_time == self.run_func_time:
					logger().info("Clean junk function failed")
					self.driver.save_screenshot(self.screenshotDir + 'test_cleanJunk %s.png' % self.timestr)
					raise Exception('Clean junk function failed')
			else:
				break

	def test_scanWifi(self):
		'''To perform scan Wi-Fi function'''
		logger().info("Launch app")
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/eula_accept').click()
		WebDriverWait(self.driver, self.page_load_time).until(EC.element_to_be_clickable((By.ID, 'com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue')))
		self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/btn_interstitial_remove_ads_continue').click()
		logger().info("Entered main page")
		self.driver.find_element_by_xpath('//android.widget.TextView[@text="SCAN WI-FI"]').click()
		logger().info("Started to scan Wi-Fi")
		wait_time = 0
		while True:
			try:
				self.driver.find_element_by_id('com.avast.android.mobilesecurity:id/ui_feed_header_title')
				logger().info("Completed Wi-Fi scanning")
				self.driver.save_screenshot(self.screenshotDir + 'test_scanWifi %s.png' % self.timestr)
			except:
				wait_time += 1
				if wait_time == self.run_func_time:
					logger().info("Wi-Fi scanning function failed")
					self.driver.save_screenshot(self.screenshotDir + 'test_scanWifi %s.png' % self.timestr)
					raise Exception('Scan Wi-Fi function failed')
			else:
				break

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(Homework('test_scan'))
	suite.addTest(Homework('test_appVersionNotEmpty'))
	suite.addTest(Homework('test_boostRam'))
	suite.addTest(Homework('test_cleanJunk'))
	suite.addTest(Homework('test_scanWifi'))
	runner = HTMLReport.TestRunner(report_file_name = 'Avast Antivirus 2018 ' + Homework.timestr,
									output_path ='Report',
									description = 'App automation test for Avast Antivirus 2018 basic functions',
									thread_count = 1,
									thread_start_wait = 0,
									sequential_execution = True,
									lang = 'en')
	runner.run(suite)
