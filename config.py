appium_server_url = 'http://localhost:4723'

capabilities = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "platformVersion": "11",
    "app": "C:\\My_files\\POKS_DEV_V_1_6_4.apk",
    "appPackage": "io.pokerplatform.poks.poker",
    "appActivity": "io.pokerplatform.poks.poker.MainActivity",
    "appium:automationName": "UIAutomator2",
    "noReset": True,
    "fullReset": False
}

user_id_in_club_xpath = "io.pokerplatform.poks.poker:id/txtUserId"
id_sign_in_button = "io.pokerplatform.poks.poker:id/btnLogin"
id_user_name_field = "io.pokerplatform.poks.poker:id/txtEmail"
id_password_field = "io.pokerplatform.poks.poker:id/txtPassword"
username = "user05"
password = "123"
# id стрелки для выбора клуба
arrow_id = "io.pokerplatform.poks.poker:id/arrow"
# xpath выбранного клуба
club_xpath = '//android.widget.TextView[@resource-id="io.pokerplatform.poks.poker:id/areaName" and @text="newt"]'
# ID кнопки вызова формы создания клуба
create_club_button_id = "io.pokerplatform.poks.poker:id/btnCreateClub"
# ID кнопки вызова формы подачи заявки на вступление в клуб
join_club_button_id = "io.pokerplatform.poks.poker:id/btnJoinClub"
# ID кнопки вызова формы выхода из клуба
leave_club_button_id = "io.pokerplatform.poks.poker:id/leaveClub"
# xpath выбора Global games
global_games_xpath = '//android.widget.TextView[@resource-id="io.pokerplatform.poks.poker:id/areaName" and @text="Global games"]'
# xpath кнопки Lobby в лобби клуба
lobby_button_xpath = '//android.widget.TextView[@text="Lobby"]'
# xpath кнопки Club в лобби клуба
club_button_xpath = '//android.widget.TextView[@text="Club"]'

xpath_error_text_username = '(//android.widget.TextView[@resource-id="io.pokerplatform.poks.poker:id/textinput_error"])[1]'
xpath_error_text_password = '(//android.widget.TextView[@resource-id="io.pokerplatform.poks.poker:id/textinput_error"])[2]'
expected_error_text = "Wrong username or password"

# Селектор заголовка формы с списком клубов
change_club_menu_title_id = "io.pokerplatform.poks.poker:id/title"
# Селектор выбора клуба
expected_club_id = "io.pokerplatform.poks.poker:id/currentArea"