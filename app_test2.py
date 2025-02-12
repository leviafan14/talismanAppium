import time
import unittest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Задайте параметры для подключения к Appium
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "platformVersion": "11",
    "app": "C:\\My_files\\POKS_DEV_V_1_6_4.apk",
    "appPackage": "io.pokerplatform.poks.poker",
    "appActivity": "io.pokerplatform.poks.poker.MainActivity",
    "appium:automationName": "UIAutomator2",
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



    # Авторизация по номеру телефона
    def auth_in_club(self, username, password) -> None:

        user_id_in_club_xpath = "io.pokerplatform.poks.poker:id/txtUserId"

        # Объявление локаторов и тестовых данных
        username_field = self.driver.find_element(By.ID, 'io.pokerplatform.poks.poker:id/txtEmail')
        password_field = self.driver.find_element(By.ID, 'io.pokerplatform.poks.poker:id/txtPassword')

        # Клик по полю ввода номера телефона
        username_field.click()
        username_field.send_keys(username)
        password_field.send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'io.pokerplatform.poks.poker:id/btnLogin'))
        ).click()

        # Ожидание появление ID юзера внутри клуба
        user_id_in_club = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, user_id_in_club_xpath))
        )

        return user_id_in_club.text

    def test_assert_user_id(self):
        username = "user05"
        password = "123"
        assert_user_id = "ID: 974104"

        expected_user_id = self.auth_in_club(username, password)

        assert expected_user_id == assert_user_id


if __name__ == '__main__':
    unittest.main()