from connect import conexao, cursor


inserir_num = f"""INSERT INTO {table}(nSorteio, n1, n2, n3, n4, n5, n6)
    values
    ({nSorteio}, {n1}, {n2}, {n3}, {n4}, {n5}, {n6})"""

cursor = conexao.cursor()
cursor.execute(inserir_num)
conexao.commit()
