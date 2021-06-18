from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            # o caminho do webdriver baixado:
            executable_path=r"caminho_webdriver")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)

        campo_usuario = driver.find_element_by_xpath(
            "//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(5)
        # O 'código' da foto https://www.instagram.com/p/(código)/
        self.comente_nas_fotos('codigo')

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1, 5)/30)

    def comente_nas_fotos(self, username):
        driver = self.driver
        driver.get("https://www.instagram.com/p/" + username + "/")
        time.sleep(3)

        while True:

            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            try:
                # Aqui, são os comentários que o bot vai fazer.
                comentarios = ['Eu quero', 'teste', 'Eu quero!!!!!!']
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2, 5))
                self.digite_como_uma_pessoa(
                    random.choice(comentarios), campo_comentario)
                time.sleep(random.randint(10, 600))

                driver.find_element_by_xpath(
                    "//button[contains(text(),'Publicar')]").click()
                time.sleep(3)
            except Exception as e:
                print(e)
                time.sleep(5)


PyBot = InstagramBot('SEU_ID', 'SUA_SENHA')
PyBot.login()
