import unittest

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

from appium.options.common.base import AppiumOptions
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


class TestApp(unittest.TestCase):

    user_id_in_club_xpath = "io.pokerplatform.poks.poker:id/txtUserId"
    id_sign_in_button = "io.pokerplatform.poks.poker:id/btnLogin"
    id_user_name_field = "io.pokerplatform.poks.poker:id/txtEmail"
    id_password_field = "io.pokerplatform.poks.poker:id/txtPassword"
    username = "user05"
    password = "123"
    # id стрелки для выбора клуба
    arrow_id = "io.pokerplatform.poks.poker:id/arrow"

    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url,  options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    # Авторизация в клубе
    def auth_in_club(self, username, password) -> None:

        # Объявление локаторов
        username_field = self.driver.find_element(By.ID, self.id_user_name_field)
        password_field = self.driver.find_element(By.ID, self.id_password_field)

        # Клик по полю ввода логина или почты
        username_field.click()
        username_field.send_keys(username)
        password_field.send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.id_sign_in_button))).click()

    def test_auth_with_valid_data(self):

        assert_user_id = "ID: 974104"

        self.auth_in_club(self.username, self.password)

        # Ожидание появление ID юзера внутри клуба
        expected_user_id = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, self.user_id_in_club_xpath)))

        assert expected_user_id.text == assert_user_id

    def test_auth_by_invalid_password(self):
        test_cases = [
            ("user017", "1234"),
            ("invalid", "123"),
            (" ", "123"),
            ("user017", " ")
        ]

        xpath_error_text_username = '(//android.widget.TextView[@resource-id="io.pokerplatform.poks.poker:id/textinput_error"])[1]'
        xpath_error_text_password = '(//android.widget.TextView[@resource-id="io.pokerplatform.poks.poker:id/textinput_error"])[2]'
        expected_error_text = "Wrong username or password"

        for username, password in test_cases:
            with self.subTest(username=username, password=password):

                self.auth_in_club(username, password)

                # Ожидание появления текста ошибки для имени пользователя
                error_text_username = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_error_text_username))
                )

                # Проверка текста ошибки для имени пользователя
                self.assertEqual(error_text_username.text, expected_error_text)

                # Ожидание появления текста ошибки для пароля
                error_text_password = WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, xpath_error_text_password))
                )

                # Проверка текста ошибки для пароля
                self.assertEqual(error_text_password.text, expected_error_text)

    def test_empty_auth_fields(self):
        test_cases = [
            ("", "123"),
            ("user017", ""),
            ("", "")
        ]

        for username, password in test_cases:
            with self.subTest(username=username, password=password):
                button_sign_in = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, self.id_sign_in_button)))

                self.assertFalse(button_sign_in.is_enabled())

    # Функция изменения выбранного клуба
    def change_club(self):

        club_xpath = '//android.widget.TextView[@resource-id="io.pokerplatform.poks.poker:id/areaName" and @text="newt"]'

        # Авторизация в приложении
        self.auth_in_club(self.username, self.password)

        # Нажатие на стрелку для раскрытия списка клубов
        WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((By.ID, self.arrow_id))).click()

        # Нажатие на выбранный клуб
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, club_xpath))).click()

    # Тест изменения выбранного клуба
    def test_change_club(self):
        change_club_menu_title_id = "io.pokerplatform.poks.poker:id/title"

        expected_club_id = "io.pokerplatform.poks.poker:id/currentArea"
        expected_club_name = "newt"
        self.change_club()

        # Меню выбора клуба скрылось
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element(By.ID, change_club_menu_title_id)

        # Получение названия выбранного клуба
        actual_club_name = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, expected_club_id))).text

        # Полученное название клуба соответствует ожидаемому
        self.assertEqual(expected_club_name, actual_club_name)

        # Стрелка отображается
        arrow = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, self.arrow_id)))

        self.assertTrue(arrow.is_displayed(),  f"Стрелка '{arrow}' не отображается на странице.")


if __name__ == '__main__':
    unittest.main()