from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from connect import con, cursor
#from janela import Aplicacao

class Web:
    def __init__(self, ano):
        self.ano = str(ano)
        self.site = f'https://asloterias.com.br/resultados-da-mega-sena-{self.ano}'
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
        self.criar_tabela()
        self.abrir_site(self.ano)

    def abrir_site(self, ano):
        sorteados = []
        self.driver.get(self.site)
        sleep(5)
        k = 0
        for i in range(110): #NUMERO DO SORTEIO
            sorteio = self.driver.find_element(By.XPATH, self.map['sorteio']['xpath'].replace('%num_sorteio%',f'{i+4}')).text
            
            for j in range(6): #NUMEROS SORTEADOS
                x = self.driver.find_element(By.XPATH, self.map['numero']['xpath'].replace('@nums@', f'{k+1}')).text
                k += 1
                sorteados.append(x)

            numero1, numero2, numero3, numero4, numero5, numero6 = sorteados
            inserir_num(ano, sorteio, numero1, numero2, numero3, numero4, numero5, numero6)
            sorteados.clear()
        
    def criar_tabela(self):
        cursor.execute(
            f"SELECT * FROM information_schema.tables WHERE table_name = 'sena{self.ano}'")
        table_exists = cursor.fetchone()

        if table_exists:
            cursor.execute(f"DROP TABLE IF EXISTS sena{self.ano}")

        cursor.execute(
            f"""CREATE TABLE sena{self.ano} (sorteio int PRIMARY KEY, 
                                            numero1 int, 
                                            numero2 int, 
                                            numero3 int, 
                                            numero4 int, 
                                            numero5 int, 
                                            numero6 int)""")
        con.commit()


def inserir_num(ano, sorteio, numero1, numero2, numero3, numero4, numero5, numero6):
    inserir_num = f"""INSERT INTO sena{ano}(sorteio, numero1, numero2, numero3, numero4, numero5, numero6)
        values
    ({sorteio}, {numero1}, {numero2}, {numero3}, {numero4}, {numero5}, {numero6})"""

    cursor = con.cursor()
    cursor.execute(inserir_num)
    con.commit()

# def procurar_usuario(id):
#     sql = f"SELECT * from mega{ano} WHERE nSorteio = '{nSorteio}'"
#     cursor.execute(sql)
#     return cursor.fetchall()



