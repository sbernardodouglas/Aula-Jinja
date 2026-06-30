from menu import carregar_dados, exibir_menu, calcular_banho

def executar():
    dados_caes = carregar_dados('dados.json')
    
    if not dados_caes:
        return

    while True:
        lista_racas = exibir_menu(dados_caes)
        try:
            escolha = int(input("nEscolha o número do cachorro (ou 0 para sair): "))
            
            if escolha == 0:
                print("Encerrando o sistema...")
                break
            
            if 1 <= escolha <= len(lista_racas):
                raca_escolhida = lista_racas[escolha - 1]
                peso = dados_caes[raca_escolhida]
                valor_final = calcular_banho(peso)
                
                print("-" * 30)
                print(f"RESUMO DO SERVIÇO:")
                print(f"Raça: {raca_escolhida}")
                print(f"Peso: {peso}kg")
                print(f"Valor Total: R$ {valor_final:.2f}")
                print("-" * 30)
            else:
                print("Opção inválid Tente novamente.")
        
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    executar()