#Vamos a crear un codigo que realize por pantalla un calculo de variables,que nos permita sumar 
#restas y hacer operaciones para realizar al final un resultado de cada operacion y a su vez crear una tabla de
#la verdad y cada una de las operaciones usando "bool and y or"

print ("Este programa no se debe hacer por chat gpt el que lo haga le bajo nota")

a= input ("Deme un numero en pantalla    ")
b= input ("Deme un numero mayor que el anterior ")

a=int (a)
b=int (b)

#a=str (a)
#b=str (b)

#print (a+b)
#print (a-b)
#print (a*b)
#print (a/b)
#print (a%b)

# con conjuncion

print ("Tabla de la verdad todo lo relacionado con And o Y")
print ((str(a==a))+"and "+str(a==a)+"---->"+str(a==a))
print ((str(a==a))+"y"+str(a==b)+"---->"+str(a==b))
print ((str(a==b))+"and"+str(a==a)+"---->"+str(a==b))
print ((str(a==b))+"and"+str(a==b)+"---->"+str(a==b))

# con disyuncion

a= str(a)
b= str(b)

print ((str(a==a))+"and" +str(a==a)+"---->"+str(a==a))
print ((str(a==a))+"and "+str(a==b)+"---->"+str(a==a))
print ((str(a==b))+"and "+str(a==a)+"---->"+str(a==a))
print ((str(a==b))+"and "+str(a==b)+"---->"+str(a==b))

#bool

#Conjuncion

print ((bool(a==a)))
print ((bool(a==b)))
print ((bool(a==b)))
print ((bool(a==b)))

#Disyuncion

print ((bool(a==a)))
print ((bool(a==a)))
print ((bool(a==a)))
print ((bool(a==b)))