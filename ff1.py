import matplotlib.pyplot as plt




matriz = []
letrasdospontos = []
quantpontos = 0
caminhos = []
dronometros = []
new = []

with open('matriz.txt') as f:
    while True:
        linhas,colunas=f.readline().split()
        lines=f.read().splitlines()
        break
    
        
quantcaminhos = 0
linhas=int(linhas)
colunas=int(colunas)

for l in range (linhas):
    a = []
    for k in range (len(lines[0])):
        if lines[l][k]!=' ':
            ponto = lines[l][k]
            a.append(ponto)
            if not (ponto=='R' or ponto=='0'):
                letrasdospontos.append (ponto)
                quantpontos +=1

    matriz.append (a)


def permutacao_gerador (lista):
    if len(lista)<=1:
        yield lista
        return
    for i, atual in enumerate(lista):
        elementos_restantes = lista[:i]+lista[i+1:]
        for p in permutacao_gerador (elementos_restantes):
            yield [atual]+p



for i, p in enumerate(permutacao_gerador(letrasdospontos)):
    caminhos.append (p)
    print (p)
    


for z in range(len(caminhos)):
    for v in range (quantpontos+1):
        if v==0:
            distt=0
            for x in range(linhas):
                for y in range(colunas):
                    if matriz[x][y]=='R':
                        for t in range(linhas):
                            for u in range(colunas):
                                if matriz[t][u]==caminhos[z][v]:
                                    distX = u-y
                                    if u-y<0:
                                        distX=y-u
                                    distY=t-x
                                    if t-x<0:
                                        distY=x-t
                                    distt=distY+distX
        if (v>0 and v<quantpontos):
            for x in range(linhas):
                for y in range(colunas):
                    if matriz[x][y]==caminhos[z][v-1]:
                        for t in range(linhas):
                            for u in range(colunas):
                                if matriz[t][u]==caminhos[z][v]:
                                    distX = u-y
                                    if u-y<0:
                                        distX=y-u
                                    distY=t-x
                                    if t-x<0:
                                        distY=x-t
                                    distt+=distY+distX
        if v==quantpontos:
            for x in range(linhas):
                for y in range(colunas):
                    if matriz[x][y]=='R':
                        for t in range(linhas):
                            for u in range(colunas):
                                if matriz[t][u]==caminhos[z][v-1]:
                                    distX = u-y
                                    if u-y<0:
                                        distX=y-u
                                    distY=t-x
                                    if t-x<0:
                                        distY=x-t
                                    distt+=distY+distX
                                    quantcaminhos +=1
            dronometros.append(distt)
            new.append (quantcaminhos)



resultadoemnumero = min(dronometros)
resultadoemsequencia = ''
for i in range(quantpontos):
    resultadoemsequencia+=(caminhos[dronometros.index(resultadoemnumero)][i])
print ("O melhor ou um dos melhores percursos é o trecho",resultadoemsequencia,",")
print("o qual possui uma distância de", resultadoemnumero, "dronômetros.")



# x axis values

pontosx = []
# corresponding y axis values
pontosy = []
letraspontosgg = []

for i in range(len(resultadoemsequencia)):
    for d in range (linhas):
        for e in range(colunas):
            if matriz[d][e]==resultadoemsequencia[i]:
                pontosx.append(d)
                pontosy.append(e)
                letraspontosgg.append(resultadoemsequencia[i])
                if i==len(resultadoemsequencia)-1:
                    xult=[d]
                    yult=[e]
                
pontosx = xult + pontosx[:quantpontos-1]
pontosy = yult + pontosy[:quantpontos-1]


for i, txt in enumerate (letraspontosgg):
    plt.annotate (txt, (pontosx[i],pontosy[i]), xytext=(pontosx[i-1], pontosy[i-1]))



# plotting the points
plt.plot(pontosx,pontosy, color='green', linestyle='dashed', linewidth = 2,
		marker='o', markerfacecolor='blue', markersize=4, )

# setting x and y axis range
plt.ylim(-1,5)
plt.xlim(-1,4)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Melhor caminho encontrado!')

# function to show the plot
plt.show()




#################################################################





# plotting the points
plt.plot(new,dronometros, color='green', linestyle='solid', linewidth = 2,
		marker='o', markerfacecolor='blue', markersize=4, )

# setting x and y axis range
plt.ylim(min(dronometros)-1,max(dronometros)+1)
plt.xlim(0, len(caminhos)+1)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Função somatório')

# function to show the plot
plt.show()
