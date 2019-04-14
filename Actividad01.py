#Escriba un notebook en Jupyter, usando Python, que calcule la desviación estándar de un conjunto de números leídos desde teclado. Utilice numpy arrays. Explique el algoritmo.

#PRIMERO SE IMPORTA LA LIBRERIA DE NUMPY
import numpy as np;
#AHORA SE SOLICITAN LOS VALOSRES AL SUARIO SEPARADOS POR UNA COMA
datos = input("Ingrese los valores separados por una coma ',' ");
#AHORA EN RESULTS SE ASIGNAN LOS DATOS, QUE HAN SIDO DIVIDIDOS Y CONVERTIDOS EN UNA LISTA CON EL METODO SPLIT
#TAMBIEN ESTA LISTA MEDIANTE UN CASTEO ESTA ALMACENANDO ENTEROS
results = [ int(n) for n in datos.split(",")];
#SE CONVIERTE LA LISTA EN UN ARREGLO  Y SE ASIGNA A LA VARIABLE _array
_array = np.array(results);
#PARA FINALIZAR SE IMPRIME EN PANTALLA LA DESVIACION ESTANDAR, MEDIANTE LA MUNCION std() DE NUMPY
print (" ");
print( "LA DESVIACIÓN ESTANDAR ES: " + str(np.std(_array)) );

#Escriba un notebook en Jupyter, usando Python, que tome como entrada los valores m, n como el número de filas y columnas de una matriz de números A(arreglo numpy) y n la potencia a la que será elevada la matriz. Posteriormente se leen los (m^2) elementos del arreglo. El programa debe calcular (A^n) Explicar el algoritmo.

#PRIMERO SE IMPORTA LA LIBRERIA DE NUMPY
import numpy as np;
#SE CREA LA LISTA QUE TRABAJARÁ COMO MATRIZ
matriz = [];
#SE SOLICITAN LOS DATOS  DE CANTIDAD DE FILAS, COLUMNAS Y POTENCIA A ELEVAR LA MATRIZ
mFilas    = int(input("Ingrese la cantidad de filas: "));
nColumnas = int(input("Ingrese la cantidad de Columnas: "));
nPotencia = int(input("Ingrese la potencia para elevar la matriz: "));
#SE ASIGNA UNA DIMENSION PARA LA MATRIZ Y SE LLENA EN PRINCIPIO CON VALOR DE 0
for i in range(mFilas):
    matriz.append([0]*nColumnas);
#SE RECORRE LA LISTA-MATRIZ Y EN CADA POSICIÓN SE LE ASIGNA UN VALOR DADO POR EL USUARIO          
for i in range(mFilas):
    for j in range (nColumnas):
        matriz[i][j]= int( input("Ingrese el valor para la pareja ordenada (%d, %d): " % (i,j)));
print (" ")
#SE MUESTRA LA MATRIZ CREADA
print("MATRIZ GENERADA: ");
for i in matriz:
    print (i);
print (" ");
#SE CONVIERTE LA LISTA EN UNA MATRIZ PARA PODERLA ELEVAR, Y SE ASIGNA A LA VARIABLE A
A = np.matrix(matriz);
#SE IMPRIME LA MATRIZ ELEVADA A LA POTENCIA DADA POR EL USUARIO, 
#ESTO SI LA MATRIZ ES CUADRADA DE LO CONTRARIO SE LE MUESTRA UN MENSAJE DE ERROR
if(mFilas == nColumnas):
    print( "MATRIZ ELEVADA A LA POTENCIA " + str(nPotencia) + ": \n" + str( pow( A, nPotencia) ));
else:
    print("ERROR: SOLO SE PUEDEN CALCULAR LAS POTENCIAS DE MATRICES CUADRADAS.");



#Escriba un notebook en Jupyter, usando Python, que lea los arreglos A y B, ambos de n dimensiones y los escalares c y d y calcule la combinación lineal C = cA + dB. Grafique los arreglos utilizando matplotlib, los arrays deben ser numpy.

#PRIMERO SE IMPORTA LA LIBRERIA DE NUMPY Y MATPLOTLIB
import matplotlib.pyplot as plt;
import numpy as np;
#SE CREA LA PRIMER LISTA QUE TRABAJARÁ COMO ARREGLO A
_arrayA = [];
#SE SOLICITAN LOS DATOS  DE CANTIDAD DE FILAS, COLUMNAS
mAFilas    = int(input("Ingrese la cantidad de filas del arreglo A: "));
nAColumnas = int(input("Ingrese la cantidad de columnas del arreglo A: "));
#SE ASIGNA UNA DIMENSION PARA LA MATRIZ Y SE LLENA EN PRINCIPIO CON VALOR DE 0
for i in range(mAFilas):
    _arrayA.append([0]*nAColumnas);
#SE RECORRE LA LISTA-MATRIZ Y EN CADA POSICIÓN SE LE ASIGNA UN VALOR DADO POR EL USUARIO          
for i in range(mAFilas):
    for j in range (nAColumnas):
        _arrayA[i][j]= int( input("Ingrese el valor para la pareja ordenada (%d, %d): " % (i,j)));
#SE CREA LA SEGUNDA LISTA QUE TRABAJARÁ COMO ARREGLO B
_arrayB = [];
#SE SOLICITAN LOS DATOS  DE CANTIDAD DE FILAS, COLUMNAS
mBFilas    = int(input("Ingrese la cantidad de filas del arreglo B: "));
nBColumnas = int(input("Ingrese la cantidad de columnas del arreglo B: "));
#SE ASIGNA UNA DIMENSION PARA LA MATRIZ Y SE LLENA EN PRINCIPIO CON VALOR DE 0
for i in range(mBFilas):
    _arrayB.append([0]*nBColumnas);
#SE RECORRE LA LISTA-MATRIZ Y EN CADA POSICIÓN SE LE ASIGNA UN VALOR DADO POR EL USUARIO          
for i in range(mBFilas):
    for j in range (nBColumnas):
        _arrayB[i][j]= int( input("Ingrese el valor para la pareja ordenada (%d, %d): " % (i,j)));
#SE CREAN LOS ARREGLOS A Y B, A PARTIR DE LAS LISTAS ANTERIORES       
arregloA = np.array(_arrayA);
arregloB = np.array(_arrayB);
print (" ");
#SE MUESTRA EL ARREGLO A
print("ARREGLO A GENERADO: ");
for i in _arrayA:
    print (i);
print (" ");
#SE MUESTRA EL ARREGLO B
print("ARREGLO B GENERADO: ");
for i in _arrayB:
    print (i);
print (" ");
#SE SOLICITAN LOS VALORES DE LOS ESCALARES C Y D
C = int(input('Ingrese el escalar C: '));
D = int(input('Ingrese el escalar D: '));
print (" ");
#CALCULO DE LA COMBINACION LINEAL
combinacionLineal = ( (C*arregloA)+(D*arregloB) );
#SE MUESTRA EL VALOR DE LA COMBINACIÓN LINEAL
print("LA COMBINACIÖN LINEAL ES: \n" + str(combinacionLineal) );
#SE CREA LA GRAFICA PARA EL ARREGLO A
plt.plot(arregloA);
plt.xlabel('X');
plt.ylabel('Y');
plt.title('Arreglo A');
#MUESTRA LA GRILLA
plt.grid();
plt.show();
#SE CREA LA GRAFICA PARA EL ARREGLO B
plt.plot(arregloB);
plt.xlabel('X');
plt.ylabel('Y');
plt.title('Arreglo B');
#MUESTRA LA GRILLA
plt.grid();
plt.show();


