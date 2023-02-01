import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opcoes = Options()
opcoes.add_argument('--headless') # Executar em segundo plano
navegador = Chrome(service=Service(ChromeDriverManager().install()), options=opcoes)
navegador.set_window_size(1280, 1050)
navegador.maximize_window()

navegador.get('http://raspagem.herokuapp.com/contato/') # Site para preencher campos automaticamente com python usando a ferramenta selenium

time.sleep(1)
link_contato = navegador.find_element(By.LINK_TEXT, 'Contato')
link_contato.click()
time.sleep(1)
navegador.save_screenshot('contato.png')

campo_nome = navegador.find_element(By.ID, 'id_name')
campo_email = navegador.find_element(By.ID, 'id_email')
campo_mensagem = navegador.find_element(By.ID, 'id_message')

campo_nome.send_keys('Seu nome')
campo_email.send_keys('Seu email')
campo_mensagem.send_keys('Sua mensasgem')

time.sleep(1)

navegador.save_screenshot('campo_preenchido.png')

botao = navegador.find_element(By.TAG_NAME, 'button')
botao.click()

time.sleep(1)

navegador.save_screenshot('conclusao.png')

navegador.close()
