import copy

#Global
comparacoes  = 0
trocas = 0

#Seleção
def selecao(lista, opcao):
  n = len(lista)
  trocas = 0
  comparacoes = 0
  etapas = 0
  for i in range(n-1):

   pos_menor = i
   
   for j in range(i+1, n):
     comparacoes += 1
     if (lista [j] < lista[pos_menor]):
       pos_menor = j
   etapas += 1 
   trocas += 1
   if (lista[pos_menor] != lista[i]):
     if(opcao == 0):
       print("Posição atual: " , i, "\tNumero atual: ", lista[i],"\nPosição menor: ", pos_menor, "\tMenor numero: ", lista[pos_menor])
     aux = lista[i]
     lista[i] = lista[pos_menor]
     lista[pos_menor] = aux 
     print(lista)
  if(opcao == 0):
    print("Selação\nNumero de Elementos: {0}\nNumero de Comparaçoes: {1}\nTrocas: {2}\nEtapas: {3}\nResultado:".format(n, comparacoes, trocas, etapas), lista)
  elif opcao == 1:
    print("Selecao:\t\t{0}\t\t{1}".format(comparacoes, trocas))

#Inserção
def insertion(lista, opcao):
  i=1
  n=len(lista)
  cont = 0
  etapas = 0
  while (i<n):
    current = lista[i]
    if opcao == 0:
      print("posição atual:", i)
    j=i-1
    while(current < lista[j]):
      cont += 1          
      lista[j+1] = lista[j]
      j -= 1
      if(j<0):
        break
    else:
      cont += 1
    lista[j+1] = current
    etapas += 1
    if opcao == 0:
      print("posição correta:", j+1)
      print(lista)
    i+=1
  if opcao == 0:
    print("insertion\nNumero de Elementos: {0}\nNumero de Comparaçoes: {1}\nEtapas: {2}\nResultado:".format(n, cont, etapas), lista)
  elif opcao == 1:
    print("insertion:\t\t{0}\t\t-".format(cont))

#Bolha
def bolha(lista, opcao):
  troca = True
  n = len(lista)
  etapa = -1
  trocas = 0
  comp = 0
  while(troca):
    troca = False
    for i in range(n-1):
      comp += 1
      if(lista[i] > lista[i+1]):  
        if opcao == 0:
          print("Lista: ", lista)
        aux = lista[i]
        lista[i] = lista[i+1]
        lista[i+1] = aux
        if opcao == 0:
          print("posição atual: {0}\tNumero atual: {1}\nLista: {2}".format(i, aux, lista))
        troca = True
        trocas += 1
    etapa += 1
  if opcao == 0:
    print("bolha\nNumero de Elementos: {0}\nNumero de Comparaçoes: {1}\nEtapas: {2}\nTrocas: {3}\nResultado:".format(n, comp, etapa, trocas), lista)
  elif opcao == 1:
    print("bolha:\t\t\t{0}\t\t{1}".format(comp, trocas))

#Quicksort
def quicksort(lista, inicio, fim, opcao):
  global comparacoes
  global trocas
  i = inicio
  j = fim
  if opcao == 0:
    print("pivo:", lista[int((inicio + fim)/2)])
  pivo = lista[int((inicio + fim)/2)]

  while(i<j):
    while(lista[i] < pivo):
     comparacoes += 1
     i += 1
    else:
     comparacoes += 1
    while(lista[j] > pivo):
      comparacoes += 1
      j -= 1
    else:
      comparacoes += 1
    if(i <= j):
      trocas += 1
      aux = lista[i]
      lista[i] = lista[j]
      lista[j] = aux
      i += 1
      j -= 1

  if opcao == 0:
    print(lista,"troca:",  trocas, "comparações:" ,comparacoes)
  if(inicio < j):
    quicksort(lista, inicio, j, opcao)
  if(i < fim):
    quicksort(lista, i, fim, opcao)

#Gera um vetor com os numeros informados 
def criar_lista(lista):
  i = int(input("Informe o tamanho do vetor:"))
  temp = input("Entre com os elementos do vetor separados por espaço:")
  inicio = 0
  for j in range(len(temp)):
    if temp[j] == " " or j == len(temp) - 1:
      if j == len(temp) -1:
        lista.append(int(temp[inicio:]))
      elif inicio != 0:
        lista.append(int(temp[inicio+1:j]))
      else:
        lista.append(int(temp[inicio:j]))
      inicio = j
  if i != len(lista):
    print("Tamanho de lista informado esta errada")
    lista = []
  else:
    print(lista)
    
#Menu principal
conf = 0
lista = []
while(conf != 7):
  conf = int(input("Escolha a opcao:\n1 - Seleção\n2 - Inserção\n3 - Bolha\n4 - Quicksort\n5 - Tabela comparativa\n6 - Inserir um vetor\n7 - Sair\n"))
  
  if len(lista) != 0 and 0<conf<6 :
    #Seleção
    if conf == 1:
      listaT = copy.deepcopy(lista)
      selecao(listaT, 0)

    #Inserção
    elif conf == 2:
      listaT = copy.deepcopy(lista)
      insertion(listaT, 0)

    #Bolha
    elif conf == 3:
      listaT = copy.deepcopy(lista)
      bolha(listaT, 0)

    #Quicksort
    elif conf == 4:
      comparacoes  = 0
      trocas = 0
      listaT = copy.deepcopy(lista)
      quicksort(listaT, 0, len(lista)-1, 0)
      print("quicksort\nNumero de Elementos: {0}\nNumero de Comparaçoes: {1}\nTrocas: {2}\nResultado:".format(len(listaT),comparacoes, trocas), listaT)
    
    #Tabela comparativa
    elif conf == 5: 
      comparacoes  = 0
      trocas = 0
      print("Nome\t\tComparações\t\tTrocas")
      selecao(copy.deepcopy(lista), 1)
      insertion(copy.deepcopy(lista), 1)
      bolha(copy.deepcopy(lista), 1)
      quicksort(copy.deepcopy(lista), 0, len(lista) - 1 , 1)
      print("Quicksort:\t\t{0}\t\t{1}".format(comparacoes, trocas))

  #Cria vetor
  elif conf == 6:
    lista = []
    criar_lista(lista)

  #Vetor vazio
  elif len(lista) == 0:
    print("vetor vazio")
  
  #Exceção
  elif conf != 7:
    print("opcao invalida")
