from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from connect import conexao, cursor

class Web:
    def __init__(self):
        self.site = 'https://asloterias.com.br/resultados-da-mega-sena-2022'
        self.map = {
            "sorteio":{
                'xpath': '/html/body/main/div[2]/div/div/div[1]/strong[%num_sorteio%]'
            },
            "numero":{
               'xpath': '/html/body/main/div[2]/div/div/div[1]/span[@nums@]'
           }
       }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.abrir_site()

    def abrir_site(self, dois_vinte_dois):
        sorteados = []
        self.driver.get(self.site)
        sleep(5)
        k = 0
        for i in range(110): #NUMERO DO SORTEIO
            nSorteio = self.driver.find_element(By.XPATH, self.map['sorteio']['xpath'].replace('%num_sorteio%',f'{i+4}')).text
            
            for j in range(6): #NUMEROS SORTEADOS
                x = self.driver.find_element(By.XPATH, self.map['numero']['xpath'].replace('@nums@', f'{k+1}')).text
                k += 1
                sorteados.append(x)

            n1, n2, n3, n4, n5, n6 = sorteados
            inserir_num(dois_vinte_dois, nSorteio, n1, n2, n3, n4, n5, n6)
        
def inserir_num(dois_vinte_dois, nSorteio, n1, n2, n3, n4, n5, n6):
    inserir_num = f"""INSERT INTO {dois_vinte_dois}(nSorteio, n1, n2, n3, n4, n5, n6)
    values
    ({nSorteio}, {n1}, {n2}, {n3}, {n4}, {n5}, {n6})"""

    cursor = conexao.cursor()
    cursor.execute(inserir_num)
    conexao.commit()

