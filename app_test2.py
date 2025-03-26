import unittest

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

from appium.options.common.base import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import *

# Параметры для подключения к Appium
options = AppiumOptions()
options.load_capabilities(capabilities)


class TestApp(unittest.TestCase):
    # Авторизация в клубе
    def auth_in_club(self, username, password) -> None:

        # Объявление локаторов
        username_field = self.driver.find_element(By.ID, id_user_name_field)
        password_field = self.driver.find_element(By.ID, id_password_field)

        # Клик по полю ввода логина или почты
        username_field.click()
        username_field.send_keys(username)
        password_field.send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, id_sign_in_button))).click()

    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url,  options=options)
        self.auth_in_club(username, password)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    # Функция получения элемента по его ID
    def get_element_by_id(self, id, timeout):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.ID, id)))
        return element

    # Функция получения элемента по его xpath
    def get_element_by_xpath(self, xpath, timeout):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element

    def test_auth_with_valid_data(self):

        assert_user_id = "ID: 974104"

        self.auth_in_club(username, password)

        # Ожидание появление ID юзера внутри клуба
        expected_user_id = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, user_id_in_club_xpath)))

        assert expected_user_id.text == assert_user_id

    def test_auth_by_invalid_password(self):
        test_cases = [
            ("user017", "1234"),
            ("invalid", "123"),
            (" ", "123"),
            ("user017", " ")
        ]

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
                    EC.presence_of_element_located((By.ID, id_sign_in_button)))

                self.assertFalse(button_sign_in.is_enabled())

    # Функция вызова формы с списком клубов
    def click_on_arrow(self):
        # Нажатие на стрелку для раскрытия списка клубов
        WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((By.ID, arrow_id))).click()

    # Функция нажатия на выбранный клуб в форме с списком клубов
    def select_club(self, club_xpath):
        # Нажатие на выбранный клуб
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, club_xpath))).click()

    # Тест изменения выбранного клуба
    def test_change_club(self):

        # Ожидаемое название клуба
        expected_club_name = "newt"

        # Клик по стрелке для вызова формы с списком клубов
        self.click_on_arrow()

        # Кнопка открытия формы создания клуба отображается
        create_club_button = self.get_element_by_id(create_club_button_id, 2)
        self.assertTrue(create_club_button.is_displayed(), "Кнопка создания клуба отображается")

        # Выбор Global games отображается
        global_games = self.get_element_by_xpath(global_games_xpath, 2)
        self.assertTrue(global_games.is_displayed(), "Global games не отображается в формы выбора клуба")

        # Кнопка открытия формы отравки зааявки на вступление в клуб отображается
        join_club_button = self.get_element_by_id(join_club_button_id, 2)
        self.assertTrue(join_club_button.is_displayed(), "Кнопка открытия формы отравки зааявки на вступление в клуб не отображается")

        # Кнопка открытия формы выхода из клуба отображается
        leave_club_button = self.get_element_by_id(leave_club_button_id, 2)
        self.assertTrue(leave_club_button.is_displayed(), "Кнопка открытия формы выхода из клуба не отображается")

        # Клик по выбранному клубу
        self.select_club(club_xpath)

        # Меню выбора клуба скрылось
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element(By.ID, change_club_menu_title_id)

        # Получение названия выбранного клуба
        actual_club_name = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, expected_club_id))).text

        # Полученное название клуба соответствует ожидаемому из лобби клуба
        self.assertEqual(expected_club_name, actual_club_name)

        # Стрелка отображается
        arrow = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, arrow_id)))

        self.assertTrue(arrow.is_displayed(),  f"Стрелка '{arrow}' не отображается на странице.")

        # Кнопка лобби отображается
        lobby_button = self.get_element_by_xpath(lobby_button_xpath, 5)
        self.assertTrue(lobby_button.is_displayed())

        # Кнопка лобби отображается
        club_button = self.get_element_by_xpath(club_button_xpath, 5)
        self.assertTrue(club_button.is_displayed())

    def test_join_to_club(self):
        # Клик по стрелке для вызова формы с списком клубов
        self.click_on_arrow()

        # Кнопка открытия формы отправки заявки в клуб отображается
        join_club_button = self.get_element_by_id(join_club_button_id, 2)
        self.assertTrue(join_club_button.is_displayed(), "Кнопка открытия формы отравки зааявки на вступление в клуб не отображается")

        # Нажатие на кнопку вызова формы подачи заявки в клуб
        join_club_button.click()

        # Получение заголовка формы подачи заявки в клуб
        title_form_join_to_club = self.get_element_by_id(id_title_join_to_club_form, 2)
        self.assertEqual(title_form_join_to_club.text, expected_title_join_to_club_form)

        # Получение поля для ввода Club ID
        club_id_field = self.get_element_by_id(id_club_id_in_form_join_to_club, 2)
        # Поле для ввода Club ID отображается
        self.assertTrue(club_id_field.is_displayed(), "Поле Club ID не отображается")
        self.assertEqual(club_id_field.text, expected_placeholder_club_id_join_to_club)

        # Получение поля для ввода Agent ID
        agent_id_field = self.get_element_by_id(id_agent_id_in_form_join_to_club, 2)
        # Поле для ввода Agent ID отображается
        self.assertTrue(agent_id_field.is_displayed(), "Поле Agent ID не отображается")
        self.assertEqual(agent_id_field.text, expected_placeholder_agent_id_join_to_club)

        # Получение кнопки для подачи заявки на вступление в клуб
        join_to_club_btn = self.get_element_by_id(id_btn_join_to_club, 2)
        # Кнопка подачи заявки на вступление в клуб отображается
        self.assertTrue(join_to_club_btn.is_displayed())
        # Текст на кнопке подаче заявки на вступление в клуб соответствует ожидаемому
        self.assertEqual(join_to_club_btn.text, expected_join_btn_name)

        # Получение кнопки создания клуба
        create_club_club_btn = self.get_element_by_id(id_btn_create_club_in_form_joint_to_club, 2)

        # Кнопка создания клуба отображается
        self.assertTrue(create_club_club_btn.is_displayed())
        # Текст на кнопке подаче заявки на вступление в клуб соответствует ожидаемому
        self.assertEqual(create_club_club_btn.text, expected_create_club_btn_name)

        # Получение кнопки закрытия экрана подачи заявки на вступление в клуб
        close_btn = self.get_element_by_id(id_close_btn, 2)
        # Кнопка закрытия экрана подачи заявки на вступление в клуб отображается и активна
        self.assertTrue(close_btn.is_displayed())
        self.assertTrue(close_btn.is_enabled())


if __name__ == '__main__':
    unittest.main()