
from manutencao.manutencoes import manutencoes
import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS empresa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    pais TEXT,
    cnpj TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS filial (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    pais TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS unidade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    pais TEXT
)
""")




while True:


    print("Bem-vindo ao sistema de controle de estoque!") #só feito as classes de empresa, filial e unidade, este vai ser o menu somente
    print("1. Manutenções")
    print("2. Consultas")
    print("3. Relatórios")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        manutencoes(cursor, conn)
        
    elif escolha == "2":
        print("Opção de Consultas selecionada.")
        # Aqui você pode adicionar as opções de consultas
    elif escolha == "3":
        print("Opção de Relatórios selecionada.")
        # Aqui você pode adicionar as opções de relatórios
    elif escolha == "4":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")    
