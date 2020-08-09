import psycopg2
from psycopg2 import Error


def criar_conexao():
    connection = None
    try:
        connection = psycopg2.connect(
            host='ec2-54-197-254-117.compute-1.amazonaws.com',
            user='ojxhppwlnjgqkk',
            password='2b6d536ca210785dd45e0bb739024a31afa48db6ad9d7474938682880a4509e8',
            database='d6buuqaufl8aua',
            port='5432'
        )
        print("Conexao com o banco foi realizada com sucesso!")
    except Error as e:
        print("Deu erro. "+e)

    return connection
