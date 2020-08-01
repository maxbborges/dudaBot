from conexao import criar_conexao

def consulta(query):
    connection = criar_conexao()
    cursor = connection.cursor()
    linhas = None
    try:
        cursor.execute(query)
        linhas = cursor.fetchall()
        _temporaria = {}
        resultado = {}
        for pos,linha in enumerate(linhas):
            for posicao,coluna in enumerate(cursor.description):
                _temporaria.update({coluna[0]:linha[posicao]})
            resultado.update({pos:_temporaria})
            _temporaria={}

        return resultado
    except Error as e:
        print("ocorreu um erro")
        exit()

def insert(query,parametros):
    connection = criar_conexao()
    cursor = connection.cursor()
    try:
        cursor.execute(query,parametros)
        connection.commit()
        return 'Inserido com sucesso!'
    except Error as e:
        print('Erro ao inserir!')
        connection.rollback()
        exit()
