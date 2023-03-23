from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Define o caminho para o driver do Chrome
chromedriver_path = 'caminho/para/o/chromedriver.exe'

# Cria uma instância do driver do Chrome
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Acessa a página web desejada
driver.get('https://exemplo.com')

# Preenche campos de formulário
input_username = driver.find_element_by_id('username')
input_username.send_keys('seu_nome_de_usuario')

input_password = driver.find_element_by_id('password')
input_password.send_keys('sua_senha')

# Clica em um botão
button_login = driver.find_element_by_xpath('//button[text()="Entrar"]')
button_login.click()

# Encerra o driver do Chrome
driver.quit()
