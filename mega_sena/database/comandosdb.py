from connect import conexao, cursor


def criar_tabelas(ano):
        f"""CREATE TABLE sena{ano}(
        nSorteio int primary key,
        ano int,
        n1 int,
        n2 int,
        n3 int,
        n4 int,
        n5 int,
        n6 int
        );"""
        cursor = conexao.cursor()
        cursor.execute(criar_tabelas)
        conexao.commit()

def update_table():
        
