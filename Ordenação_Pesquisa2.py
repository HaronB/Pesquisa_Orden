import copy

#Global
cont = 0


#Reconstroi o heap 
def refaz_heap(pos, n, lista):
  global cont
  f = 2*pos
  
  while f <= n:
    cont += 1
    
    #Encontra a posição do maior filho
    if f < n and lista[f] > lista[f-1]:
      f += 1
      
    #Se o filho é menor ou igual ao pai, termina
    if lista[f-1] <= lista[pos-1]:
      break
      
    #Se o filho é maior que o pai, troca pai e filho
    aux = lista[pos-1]
    lista[pos-1] = lista[f-1]
    lista[f-1] = aux
    
    #Atualiza as posições de pai e filho para a proxima interação
    pos = f
    f = pos*2
    
#Constroi o heap 
def constroi_heap(n, lista):
  pos = int(n/2)
  while pos >= 1:
    refaz_heap(pos, n, lista)
    pos -= 1
    
#Print o heap em forma de arvore
def print_heap(lista, n):
  x = 0
  a = 1
  tab = 0

  #Calcula a quantidade de tab
  while x < n:
    aux = a
    a = (a - x) * 2
    x = aux
    a = a + x
    tab = x
  x = 0
  a = 1
  
  #Print 
  while x < n:
    flag = True
    for j in lista[x:a]:
      k = 0
      if flag:
        while k <= (tab-1)/2:
          print("\t", end = '')
          k += 1
        print("|{0}|".format(j), end = '')
        flag = False
      else:
        while k <= tab:
          print("\t", end = '')
          k += 1
        print("|{0}|".format(j), end = '')
    tab = (tab-1)/2
    aux = (a - x) * 2
    print()
    x = a
    a = aux + x 
    
    #Limita o 'a' para nao pegar o 2° filho que nao faz parte
    if a > n:
      a = n

#Ordena o heap
def ordena_heap(lista, n):

  i = 2
  
  #Constroi o heap para o vetor de entrada
  constroi_heap(n, lista)
  
  #Exibe o processo da ordenação em forma de arvore 
  print("Arvore 1:", lista)
  print_heap(lista, n)

  while n > 1:
    
    #Troca o primeiro elemento com o ultimo
    aux = lista[0]
    lista[0] = lista[n-1]
    lista[n-1] = aux
    
    #Atualiza o tamanho do heap
    n -= 1

    #Refaz o heap a partir da raiz
    refaz_heap(1, n, lista)
    
    #Exibe o processo da ordenação em forma de arvore
    print("Arvore {0}:".format(i), lista[:n])
    print_heap(lista, n)
    
    i += 1

#Shellsort
def shellsort(lista):

  #Definindo o primeiro valor de h
  h = 1
  n = len(lista)
  cont = 0
  while True:
    h = h*3+1
    if h > n :
      break
  h = int(h/3)
  
  #Inserção
  while h >= 1:
    for i in range(h, n):
      elemento_atual = lista[i]
      j = i- h
      while j >= 0 and elemento_atual < lista[j]:
        cont += 1
        lista[j+h] = lista[j]
        j -= h
      else:
        if j >= 0:
          cont += 1
      lista[j+h] = elemento_atual
      
    #Atualiza o valor de h para o proximo passo
    h = int(h/3)
  print("Comparações: ", cont)

#Pesquisa sequencial
def sequencial(vetor, n, x):
  encontrou = False
  i = 0
  while i<n and not encontrou:
    if vetor[i] == x:
      encontrou = True
    i += 1
  if encontrou:
    print("posição: {0}".format(i-1))
  else:
    print("Não esta na lista")
  print("sequencial comparações: {0}".format(i))

#Pesquisa binaria
def binario(lista, n,x ):
  ordena_heap(lista, n)
  inicio = 0 
  fim = n - 1
  encontrou = False
  i = 0
  while inicio <= fim and not encontrou:
    meio = int((inicio + fim)/2 )
    i += 1
    if lista[meio] == x:
      encontrou = True
    elif x < lista[meio]:
      fim = meio - 1
    else:
      inicio = meio + 1 
  if encontrou:
    print("posição: {0}".format(meio))
  else:
    print("Não esta na lista")
  print("binario comparações: {0}".format(i))

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

conf = 0
conf1 = 0
lista = []

#Menu principal
while (conf != 4):
  conf1 = 0
  conf = int(input("Escolha a opcao:\n1 - Ordenar\n2 - Pesquisar\n3 - Criar lista\n4 - Sair\n"))
    
  #Menu Ordena
  if conf == 1:
    while conf1 != 3:
      conf1 = int(input("Escolha a opcao:\n1 - Shellsort\n2 - heapsort\n3 - voltar\n"))
      
      #Shellsort
      if conf1 == 1:
        if len(lista) != 0:
          listaT = copy.deepcopy(lista)
          shellsort(listaT)
          print("Numero de elementos: {0}\nVetor{1}".format(len(listaT), listaT))
        else:
          print("vetor vazio")
      
      #Heapsort
      elif conf1 == 2:
        if len(lista) != 0:
          cont = 0
          listaT = copy.deepcopy(lista)
          ordena_heap(listaT, len(listaT))
          print("Comparações: {0}\nNumero de elementos: {1}\nVetor{2}".format(cont, len(listaT), listaT))
        else:
          print("vetor vazio")
      
      #Exceção
      elif conf1 != 3:
        print("opcao invalida")
        
  #Menu Pesquisa
  elif conf == 2:
    while conf1 != 3:
      conf1 = int(input("Escolha a opcao:\n1 - Pesquisa Sequencial\n2 - Pesquisa Binária\n3 - voltar\n"))
      
      #Sequencial
      if conf1 == 1:
        if len(lista) != 0:
          x = int(input("Digite o numero que deseja procurar:\n"))
          sequencial(lista, len(lista), x)
          print("Tamanho vetor: {0}\nvetor: {1}".format(len(lista), lista))
        else:
          print("vetor vazio")

      #Binária
      elif conf1 == 2:
        if len(lista) != 0:
          listaT = copy.deepcopy(lista)
          x = int(input("Digite o numero que deseja procurar:\n"))
          binario(listaT, len(listaT), x)
          print("Tamanho vetor: {0}\nvetor: {1}".format(len(listaT), listaT))
        else:
          print("vetor vazio")
      
      #Exceção 
      elif conf1 != 3:
        print("opcao invalida")
        
  #Criação lista
  elif conf == 3:
      lista = []
      criar_lista(lista)
      
  #Exceção 
  elif conf != 4:
    print("opcao invalida")