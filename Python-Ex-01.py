#Exercício 1
#Foi criado uma estrutura de repetição "enquanto" para rodar o programa.
while True:
    dados = input('Inserir dados? 0 - Não   1 - Sim ') #Pergunta feita para dar prosseguimento ao programa.
    if dados == '0': #se a opção "0 - Não" tenha sido selecionada o break será acionado e o programa encerrado.
        print('Programa finalizado.')
        break
    nome = input('Nome do aluno: ') #Se a opção 1 foi selecionada o programa peditá o nome e a nota do aluno.
    notafinal = float(input('Nota final: '))
    if notafinal <= 2.9:
        conceito = 'E'
    if notafinal >= 3.0 and notafinal <= 4.9:
        conceito = 'D'
    if notafinal >= 5.0 and notafinal <= 6.9:
        conceito = 'C'
    if notafinal >= 7.0 and notafinal <= 8.9:
        conceito = 'B'
    if notafinal >= 9.0:
        conceito = 'A'
    print(f'O aluno {nome} tirou nota {notafinal} e se enquandra no conceito {conceito}.')
    #no print mostrará o nome, a nota final e em qual o conceito o aluno se enquandra.