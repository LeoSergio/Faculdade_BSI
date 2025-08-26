import pyodbc

# 1️⃣ Conexão
server = 'localhost'
database = 'TestDB'
username = 'sa'
password = 'SUA_SENHA'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
)
cursor = conn.cursor()

# 2️⃣ Criação da tabela
cursor.execute("""
IF OBJECT_ID('Pacientes', 'U') IS NULL
CREATE TABLE Pacientes (
    id INT PRIMARY KEY IDENTITY(1,1),
    nome NVARCHAR(50),
    idade INT,
    telefone NVARCHAR(20)
)
""")
conn.commit()

# 3️⃣ Funções CRUD
def adicionar_paciente(nome, idade, telefone):
    cursor.execute(
        "INSERT INTO Pacientes (nome, idade, telefone) VALUES (?, ?, ?)",
        (nome, idade, telefone)
    )
    conn.commit()
    print(f"Paciente {nome} adicionado!")

def listar_pacientes():
    cursor.execute("SELECT * FROM Pacientes")
    for row in cursor.fetchall():
        print(row)

def atualizar_paciente(id, nome=None, idade=None, telefone=None):
    sql = "UPDATE Pacientes SET "
    params = []
    updates = []
    if nome:
        updates.append("nome = ?")
        params.append(nome)
    if idade:
        updates.append("idade = ?")
        params.append(idade)
    if telefone:
        updates.append("telefone = ?")
        params.append(telefone)
    sql += ", ".join(updates) + " WHERE id = ?"
    params.append(id)
    cursor.execute(sql, params)
    conn.commit()
    print(f"Paciente {id} atualizado!")

def remover_paciente(id):
    cursor.execute("DELETE FROM Pacientes WHERE id = ?", (id,))
    conn.commit()
    print(f"Paciente {id} removido!")

# 4️⃣ Teste CRUD
adicionar_paciente("João", 30, "99999-1111")
adicionar_paciente("Maria", 25, "98888-2222")
print("Todos os pacientes:")
listar_pacientes()
atualizar_paciente(1, idade=31)
remover_paciente(2)
print("Pacientes após alterações:")
listar_pacientes()

# 5️⃣ Fechamento da conexão
cursor.close()
conn.close()
