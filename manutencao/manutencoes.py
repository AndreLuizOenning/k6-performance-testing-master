
from classes.empresa import Empresa
from classes.filial import Filial
from classes.unidade import Unidade


def manutencoes():
    print("\n\n\n\n\n\n\nOpção de Manutenções selecionada.")
    print("1. Manutenção de Empresas")
    print("2. Manutenção de Filiais")
    print("3. Manutenção de Unidades")
    escolha_manutencao = input("Escolha uma opção de manutenção: ")
    if escolha_manutencao == "1":
        print("Manutenção de Empresas selecionada.")
    

        print("1. Cadastrar Empresa")
        print("2. Atualizar Empresa")

    elif escolha_manutencao == "2":
        print("Manutenção de Filiais selecionada.")
        # Aqui você pode adicionar as opções de manutenção de filiais
    elif escolha_manutencao == "3":
        print("Manutenção de Unidades selecionada.")
        # Aqui você pode adicionar as opções de manutenção de unidades

