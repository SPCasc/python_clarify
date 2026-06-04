import sqlite3 

# Criar o banco de dados (ou criar se caso não existir)
def conectarBanco() :
    conexao = sqlite3.connect('meu_banco.db')
    return conexao

# criaremos uma tabela nesse banco de dados
def criarTabela() :
    conexao = conectarBanco()
    # aqui temos que identificar o que será apontado e o que fazer / executar
    cursor = conexao.cursor()
    # na linha abaixo é tudo SQL (tudo que estiver em maiúsculo é função e minusculos são os termos)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
        )
    ''')
    conexao.commit()
    conexao.close()

def inserirUsuarios(nome, idade) :
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade)
            VALUES(?, ?)      
    ''', (nome, idade))
    conexao.commit()
    conexao.close()


def listarUsuarios() :
    conexao = conectarBanco()
    cursor = conexao.cursor()
    # linha abaixo é Selecione tudo que é da tabela usuários
    cursor.execute('SELECT * FROM usuarios')
    usuarios =cursor.fetchall()
    # a função fetch é um olhar sem compromisso - você está apenas olhando a informação
    for usuario in usuarios:
        print(usuario)
    conexao.close()

criarTabela()

inserirUsuarios("Caio",39)
inserirUsuarios("Leandro",39)
inserirUsuarios("Carlos",58)
inserirUsuarios("Guilherme",25)
inserirUsuarios("Daniel",30)
inserirUsuarios("Vinicius",22)
listarUsuarios()