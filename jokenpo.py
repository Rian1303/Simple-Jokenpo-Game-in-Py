import random

perg=str(input('Vamos jogar Jokenpô?'))
player = input('Pedra, Papel ou Tesoura: ').capitalize()  # Garantir que a entrada do jogador tenha a primeira letra maiúscula
opt = ['Pedra', 'Papel', 'Tesoura']
comp = random.choice(opt)

# Verificar quem venceu
if comp == 'Pedra' and player == 'Papel':
    print('\033[4;32mVocê venceu!\033[m')
elif comp == 'Papel' and player == 'Pedra':
    print('\033[4;31mEu venci!\033[m')
elif comp == 'Tesoura' and player == 'Papel':
    print('\033[4;31mEu venci!\033[m')
elif comp == 'Papel' and player == 'Tesoura':
    print('\033[4;32mVocê venceu!\033[m')
elif comp == 'Pedra' and player == 'Tesoura':
    print('\033[4;31mEu venci!\033[m')
elif comp == 'Tesoura' and player == 'Pedra':
    print('\033[4;32mVocê venceu!\033[m')
elif comp == player:
    print('Empate!')
else:
    print('OPÇÃO INVALIDA!')
