from connect import conexao

cursor = conexao.cursor()
cursor.execute('select database();')
linha = cursor.fetchone()

def listar_sorteio():
    sql = 'SELECT * from dois_vinte_dois'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    return linhas