
from classes.empresa import Empresa
from classes.filial import Filial
from classes.unidade import Unidade


def manutencoes(cursor, conn):
    
    empresas= []
    x = 0
    y = 0

    
    empresas = carregar_dados_empresa(cursor, conn)

    filiais = carregar_dados_filiais(cursor, conn)
    
    while x == 0:
        print("\n\n\n\n\n\n\nOpção de Manutenções selecionada.")
        print("1. Manutenção de Empresas")
        print("2. Manutenção de Filiais")
        print("3. Manutenção de Unidades")
        print("4. Voltar")
        escolha_manutencao = input("Escolha uma opção de manutenção: ")
        if escolha_manutencao == "1":
            y = 0
            while y == 0:
                mostrar_empresas(empresas)
                print("\n[I] Incluir   [A] Atualizar   [E] Excluir   [V] Voltar")

                escolha_operacao = input("-->").upper()
                executar_operacao_empresa(cursor, conn, escolha_operacao, empresas)
                empresas = carregar_dados(cursor, conn) 
                limpar_tela()

        elif escolha_manutencao == "2":
            y = 0
            while y == 0:
                mostrar_filiais(filiais)



        elif escolha_manutencao == "3":
            print("Manutenção de Unidades selecionada.")
        elif escolha_manutencao == "4":
            x = 1
        else:
            manutencoes(cursor, conn)


def carregar_dados_empresa(cursor):
    cursor.execute("SELECT id, nome, cnpj, pais FROM empresa")
    empresas = [Empresa(row[0], row[1], row[3], row[2]) for row in cursor.fetchall()]
    return empresas
    
def carregar_dados_filiais(cursor):
    cursor.execute("SELECT id, nome, cnpj, pais FROM filial")
    filiais = [Filial(row[0], row[1], row[3], row[2]) for row in cursor.fetchall()]
    return filiais

def carregar_dados_unidades(cursor):
    cursor.execute("SELECT id, nome, cnpj, pais FROM unidade")
    unidades = [Unidade(row[0], row[1], row[3], row[2]) for row in cursor.fetchall()]
    return unidades

def mostrar_empresas(empresas):
    limpar_tela()
    for empresa in empresas:
        print(f"ID: {empresa.get_id()}, Nome: {empresa.get_nome()}, CNPJ: {empresa.get_cnpj()}, País: {empresa.get_pais()}")

def limpar_tela():
    print("\n" * 100)

def executar_operacao_empresa(cursor, conn, escolha_operacao, empresas):

    if escolha_operacao == "I":
        id = len(empresas) + 1
        nome = input("Digite o nome da empresa: ")
        cnpj = input("Digite o CNPJ da empresa: ")
        pais = input("Digite o país da empresa: ")
        cursor.execute("INSERT INTO empresa (id, nome, cnpj, pais) VALUES (?, ?, ?, ?)", (id, nome, cnpj, pais))
        conn.commit()
        print("Empresa incluída com sucesso!")

    elif escolha_operacao == "A":

        id_empresa = int(input("Digite o ID da empresa que deseja atualizar: "))
        nome = input("Digite o novo nome da empresa: ")
        cnpj = input("Digite o novo CNPJ da empresa: ")
        pais = input("Digite o novo país da empresa: ")
        cursor.execute("UPDATE empresa SET nome = ?, cnpj = ?, pais = ? WHERE id = ?", (nome, cnpj, pais, id_empresa))
        conn.commit()
        print("Empresa atualizada com sucesso!")
        
        
    elif escolha_operacao == "E":
        id_empresa = int(input("Digite o ID da empresa que deseja excluir: "))
        cursor.execute("DELETE FROM empresa WHERE id = ?", (id_empresa,))
        conn.commit()
        print("Empresa excluída com sucesso!")
    elif escolha_operacao == "V":
        y=0
