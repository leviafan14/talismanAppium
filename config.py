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

# ID заголовка формы подачи заявки в клуб
id_title_join_to_club_form = "io.pokerplatform.poks.poker:id/title"
# Ожидаемое название формы подачи заявки в клуб
expected_title_join_to_club_form = "Join Club"

# ID поля для ввода Club ID в форме подачи заявки на вступление в клуб
id_club_id_in_form_join_to_club = "io.pokerplatform.poks.poker:id/etClubId"
# Ожидаемый плейсхолдер поля для ввода Club ID в форме подачи на вступление в клуб
expected_placeholder_club_id_join_to_club = "Club ID"

# ID поля для ввода Agent ID в форме подачи заявки на вступление в клуб
id_agent_id_in_form_join_to_club  = "io.pokerplatform.poks.poker:id/inputAgentId"
# Ожидаемый плейсхолдер поля для ввода Agent ID в форме подачи на вступление в клуб
expected_placeholder_agent_id_join_to_club = "Agent ID (optional)"

# ID кнопки подачи заявки в клуб
id_btn_join_to_club = "io.pokerplatform.poks.poker:id/btnJoin"
# Ожидаемое название кнопки подачи заявки в клуб
expected_join_btn_name = "Join"

# ID кнопки создания нового клуба в форме подачи заявки в клуб
id_btn_create_club_in_form_joint_to_club = "io.pokerplatform.poks.poker:id/btnCreateClub"
# Ожидаемое название кнопки создания клуба в форме подачи заявки в клуб
expected_create_club_btn_name = "Create new club"

# ID кнопки закрытия форм/экранов
id_close_btn = "io.pokerplatform.poks.poker:id/btnClose"

# ID кнопки вызова меню выбора типа создаваемого стола. Кнопка расположена в лобби клуба
id_plus_button = "io.pokerplatform.poks.poker:id/plusButton"

# xpath заголовка формы выбора типа создаваемого стола
xpath_header_create_table = '//android.widget.TextView[@text="Create game"]'
# xpath элемента в форме "Create game" открывающий форму создания MTT турнира
xpath_create_mtt = '//android.widget.LinearLayout[@resource-id="io.pokerplatform.poks.poker:id/tableGameContainer"]/android.view.ViewGroup[3]'

# ID поля для ввода названия турнира или стола в форме создания турнира / стола
name_field_id = 'io.pokerplatform.poks.poker:id/etName'

# ID кнопки создания стола / турнира
id_btn_create_table = "io.pokerplatform.poks.poker:id/btnCreate"

# ID клуба, лобби которого открыто в данный момент
id_current_lobby = "io.pokerplatform.poks.poker:id/currentArea"

# xpath формы уведомляющей о том что турнир / стол создан
xpath_success_create = '//android.widget.TextView[@resource-id="io.pokerplatform.poks.poker:id/txtTitle"]'
# xpath кнопки закрывающей окно уведомляющее об успешном создании стола / турнира
xpath_close_btn_success_create_form = '//android.widget.ImageView[@resource-id="io.pokerplatform.poks.poker:id/btnClose"]'