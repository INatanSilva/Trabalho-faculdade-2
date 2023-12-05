# TABELA PRINCIPAL 
print('Bem-vindo a Loja de Gelados do Natan dos Santos Silva')
print('-' * 22, 'Cardápio', '-' * 22)
print('-' * 7, '| Tamanho | Cupuaçu (CP) | Açaí (AC) |', '-' * 7)
print('-' * 7, '|    P    |   R$ 10,00   |  R$ 12,00 |', '-' * 7)
print('-' * 7, '|    M    |   R$ 15,00   |  R$ 17,00 |', '-' * 7)
print('-' * 7, '|    G    |   R$ 19,00   |  R$ 21,00 |', '-' * 7)
print('-' * 54)

# Inicializando acumulador de valores dos pedidos
total_pedido = 0

# Loop principal
while True:
    sabor = input('Escolha o sabor (CP/AC): ').upper()
    
    # Verifica se o sabor é válido
    if sabor not in ['CP', 'AC']:
        # Saída de console para sabor inválido
        print('Sabor inválido. Tente novamente...')
        continue  # Reinicia o loop

    tamanho = input('Escolha o tamanho (P/M/G): ').upper()
    
    # Verifica se o tamanho é válido
    if tamanho not in ['P', 'M', 'G']:
        # Saída de console para tamanho inválido
        print('Tamanho inválido. Tente novamente...')
        continue  # Reinicia o loop
    
    # Mapeia os códigos para os nomes completos
    nome_sabor = {'CP': 'Cupuaçu', 'AC': 'Açaí'}

    # Combinações de sabor e tamanho
    if sabor == 'CP' and tamanho == 'P':
        preco = 10
    elif sabor == 'CP' and tamanho == 'M':
        preco = 15
    elif sabor == 'CP' and tamanho == 'G':
        preco = 19
    elif sabor == 'AC' and tamanho == 'P':
        preco = 12
    elif sabor == 'AC' and tamanho == 'M':
        preco = 17
    elif sabor == 'AC' and tamanho == 'G':
        preco = 21

    # Acumulador para somar os valores dos pedidos
    total_pedido += preco
    
    # Print dizendo qual tamanho e preço que o usuário escolheu 
    print('Você pediu {} no tamanho {}: R$ {:.2f}'.format(nome_sabor[sabor], tamanho, preco))

    # Input para pedir mais alguma coisa
    mais_pedidos = input('Deseja pedir mais alguma coisa? (Sim/Não): ').upper()
    
    if mais_pedidos == 'NÃO':
        print('Total do Pedido: R$ {:.2f}'.format(total_pedido))
        print('Obrigado por usar o nosso aplicativo. Volte sempre!')
        break  # Sai do loop principal
    
    # Verifica se o usuário deseja pedir mais alguma coisa
    elif mais_pedidos == 'SIM':
        # Volta para os pedidos
        continue  # Continua o loop principal
    else:
        print('Opção inválida. Encerrando o programa.')
        break  # Sai do loop principal