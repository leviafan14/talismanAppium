import unittest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Задайте параметры для подключения к Appium
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "platformVersion": "11",
    #"app": "C:\\My_files\\app-release.apk",
    "appPackage": "customer_app.talisman_online.ru",
    "appActivity": "com.example.customer_app.talisman_online.ru.MainActivity",
    "appium:automationName": "UIAutomator2",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
    "noReset": True,
    "fullReset": False
})

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url,  options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_registartion_flow(self) -> None:
        xpath_phone_field = '//android.widget.EditText'
        button_xpath = '//android.widget.Button[@content-desc="Далее"]'

        button_send = self.driver.find_element(by=AppiumBy.XPATH, value=button_xpath)
        button_send.click()

        error_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Неправильный номер"]'))
        )


if __name__ == '__main__':
    unittest.main()
