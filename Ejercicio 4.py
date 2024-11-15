paises = []
for i in range (3):
    paises.append(input("Dime un pais que quieras vistar: "))
for i in range (len(paises)):
    print("Pais a visitar?", paises[i])
numeros= input("lista de numeros separada por comas:")
numeros= numeros.split(",")
list(map(int,numeros))
print("es alto",)
print("es bajo",)