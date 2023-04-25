from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Web:
    def __init__(self):
        self.site = 'https://orteil.dashnet.org/cookieclicker/'
        self.map={
            'idioma': {
                'xpath': '/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[10]'
                },
            'biscoito': {
                'xpath': '/html/body/div[2]/div[2]/div[15]/div[8]/button'
            }
        }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.abrir_site()

    def abrir_site(self):
        sleep(2)
        self.driver.get(self.site)
        sleep(5)
        self.driver.find_element(By.XPATH, self.map["idioma"]["xpath"]).click()
        sleep(10)
        for i in range(530):
            self.driver.find_element(By.XPATH, self.map["biscoito"]["xpath"]).click()
        sleep(15)
