from connect import con

cursor = con.cursor()
cursor.execute('select database();')
linha = cursor.fetchone()

def listar_sorteio(ano):
    sql = f'SELECT * from sena{ano}'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    return linhas