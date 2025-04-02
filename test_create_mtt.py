import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import *

# Параметры для подключения к Appium
options = AppiumOptions()
options.load_capabilities(capabilities)


@pytest.fixture(scope="module")
def driver():
    # Инициализация драйвера
    driver = webdriver.Remote(appium_server_url, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver):
    # Авторизация в клубе
    try:
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, id_user_name_field))
        )
        password_field = driver.find_element(By.ID, id_password_field)

        # Клик по полю ввода логина и пароля
        username_field.click()
        username_field.send_keys(username)
        password_field.send_keys(password)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, id_sign_in_button))
        ).click()
    except Exception as e:
        print("Пользователь авторизован")


def get_element_by_id(driver, element_id, timeout):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, element_id))
    )


def get_element_by_xpath(driver, xpath, timeout):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


# Функция вызова формы с списком клубов
def click_on_arrow(driver):
    # Нажатие на стрелку для раскрытия списка клубов
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, arrow_id))).click()


# Функция нажатия на выбранный клуб в форме с списком клубов
def select_club(driver, club_xpath):
    # Нажатие на выбранный клуб
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, club_xpath))).click()


def swipe_bottom(driver):
    size = driver.get_window_size()
    start_x = size['width'] / 2
    start_y = size['height'] * 0.8
    end_y = size['height'] * 0.2
    driver.swipe(start_x, start_y, start_x, end_y, duration=800)


def test_auth_with_valid_data(driver, login):
    assert_user_id = "ID: 974104"
    expected_user_id = get_element_by_id(driver, user_id_in_club_xpath, 10)
    assert expected_user_id.text == assert_user_id


@pytest.mark.parametrize("username, password", [
    ("user017", "1234"),
    ("invalid", "123"),
    (" ", "123"),
    ("user017", " ")
])
def test_auth_by_invalid_password(driver, username, password):
    # Авторизация с неверными данными
    username_field = get_element_by_id(driver, id_user_name_field, 10)
    password_field = driver.find_element(By.ID, id_password_field)

    username_field.send_keys(username)
    password_field.send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, id_sign_in_button))
    ).click()

    # Проверка текста ошибки для имени пользователя
    error_text_username = get_element_by_xpath(driver, xpath_error_text_username, 10)
    assert error_text_username.text == expected_error_text

    # Проверка текста ошибки для пароля
    error_text_password = get_element_by_xpath(driver, xpath_error_text_password, 15)
    assert error_text_password.text == expected_error_text


@pytest.mark.parametrize("username, password", [
    ("", "123"),
    ("user017", ""),
    ("", "")
])
def test_empty_auth_fields(driver, username, password):
    # Инициализация полей авторизации
    username_field = get_element_by_id(driver, id_user_name_field, 10)
    password_field = driver.find_element(By.ID, id_password_field)

    username_field.send_keys(username)
    password_field.send_keys(password)
    button_sign_in = get_element_by_id(driver, id_sign_in_button, 10)
    assert not button_sign_in.is_enabled()


@pytest.mark.parametrize("iteration", [1, 2, 3, 4, 5])  # Параметризация для 5 итераций
def test_create_mtt_tournament(driver, login, iteration):
    # Ожидаемое название клуба
    expected_club_name = "newt"

    # Проверка на статус авторизации пользователя
    try:
        # Получение названия клуба, в котором сейчас находится игрок
        current_club_lobby = get_element_by_id(driver, id_current_lobby, 5)
    except Exception as e:
        print("Пользователь не авторизован")

    # Если пользователь авторизован и находится НЕ в ожидаемом клубе, то клуб меняется на ожидаемый
    if current_club_lobby.text != expected_club_name:
        # Клик по стрелке для вызова формы с списком клубов
        click_on_arrow(driver)
        # Клик по выбранному клубу
        select_club(driver, club_xpath)

    # Если игрок находится в лобби клуба, то происходит нажатие на кнопку "+"
    try:
        # Получение кнопки для вызова меню создания стола
        btn_plus = get_element_by_id(driver, id_plus_button, 2)
        btn_plus.click()
    except Exception as e:
        print("Пользователь находится не в лобби клуба - кнопка '+' недоступна")

    # Получение и тест наличия заголовка формы выбора типа создаваемого стола
    create_table_form_header = get_element_by_xpath(driver, xpath_header_create_table, 2)
    assert create_table_form_header.is_displayed(), "Хеадер формы выбора типа стола не отображается"

    # Получение и нажатие на кнопку вызова формы создания MTT турнира
    btn_create_mtt = get_element_by_xpath(driver, xpath_create_mtt, 2)
    btn_create_mtt.click()

    # Ввод названия турнира
    mtt_name = get_element_by_id(driver, name_field_id, 2)
    mtt_name.send_keys(f"MTT-Appium-{iteration}")  # Использование номера итерации для имени

    # Свайп вниз экрана
    swipe_bottom(driver)

    # Получение кнопки создания турнира и нажатие на неё
    button_create_mtt_tournament = get_element_by_id(driver, id_btn_create_table, 5)
    button_create_mtt_tournament.click()

    # Ожидание исчезновения кнопки после нажатия на неё
    try:
        WebDriverWait(driver, 9).until(EC.invisibility_of_element_located((By.ID, id_btn_create_table)))
        print("Кнопка скрылась после нажатия.")
    except Exception as e:
        pytest.fail(f"Кнопка отображается после нажатия: {str(e)}")

    # Закрытие попап информирующего об успешном создании турнира
    try:
        get_element_by_xpath(driver, xpath_success_create, 5)
        close_form = get_element_by_xpath(driver, xpath_close_btn_success_create_form, 5)
        close_form.click()
    except Exception as e:
        print("Попап об успешном создании турнира не открыт")
