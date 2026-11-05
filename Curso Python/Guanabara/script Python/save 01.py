lista = []

while True:
    print("[1] Adicionar número")
    print("[2] Mostrar lista")
    print("[3] Mostrar números pares")
    print("[4] Mostrar números ímpares")
    print("[5] Sair")
    opcao = input("Escolha uma opção: ")
    if opcao not in ["1", "2", "3", "4", "5"]:
        print("Opção inválida. Tente novamente.")
        continue
    
    if opcao == "1":
        while True:
            numero = input("Digite um número: ")
            if numero.isdigit():
                lista.append(int(numero))
                print(f"Número {numero} adicionado à lista.")
                retorno = input("Deseja adicionar outro número? (s/n)")
            else:
                print("Digite um número válido.")
            if retorno.lower() != 's':
                break
    elif opcao == "2":
        if not lista:
            print("A lista está vazia.")
        else:
            print(f"Lista completa: {lista}")
    elif opcao == "3":
        if not lista:
            print("A lista está vazia.")
        else:
            pares = [num for num in lista if num % 2 == 0]
            if not pares:
                print("Não há números pares na lista.")
            else:
                print(f"Números pares: {pares}")
    elif opcao == "4":
        if not lista:
            print("A lista está vazia.")
        else:
            impares = [num for num in lista if num % 2 != 0]
            if not impares:
                print("Não há números ímpares na lista.")
            else:
                print(f"Números ímpares: {impares}")
    elif opcao == "5":
        print("Saindo do programa.")
        break
    