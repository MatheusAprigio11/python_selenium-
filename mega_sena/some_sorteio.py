from connect import cursor, conexao

def inserir_num(dois_vinte_dois, nSorteio, n1, n2, n3, n4, n5, n6):
    inserir_num = f"""INSERT INTO {dois_vinte_dois}(nSorteio, n1, n2, n3, n4, n5, n6)
    values
    ({nSorteio}, {n1}, {n2}, {n3}, {n4}, {n5}, {n6})"""


    cursor.execute(inserir_num)
    conexao.commit()