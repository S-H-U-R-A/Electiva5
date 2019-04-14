#En un Jupyter Notebook implementar el modelo de regresión lineal.

#PRIMERO SE IMPORTA LA LIBRERIA DE NUMPY Y MATPLOTLIB
import matplotlib.pyplot as plt;
import matplotlib.colors as mcolors
import numpy as np;
#SE DECLARAN LOS ARREGLOS A USAR COMO DATOS DE (X) Y (Y)
_arrayX = [];
_arrayY = [];
print (" ");
#SE LEE LA CANTIDAD DE ELEMENTOS A USAR
x_y_Items = int(input("INGRESE LA CANTIDAD DE ELEMENTOS PARA (X) y (Y): "));
print (" ");
print ("INGRESE LOS VALORES PARA X: ");
#SE INGRESA EL VALOR PARA CADA POSICION EN X
for i in range(x_y_Items):
    _arrayX.append(float( input( "Ingrese el valor X[{}]: ".format(i) ) ));
print (" ");
print ("INGRESE LOS VALORES PARA Y: ");
#SE INGRESA EL VALOR PARA CADA POSICION EN X
for i in range(x_y_Items):
    _arrayY.append(float( input( "Ingrese el valor Y[{}]: ".format(i) ) ));
print (" ");
#SE CONVIERTEN LAS LISTAS EN ARRAYS DE NUMPY, PARA PODER OPERARLOS MATEMATICAMENTE
dataX = np.array(_arrayX);
dataY = np.array(_arrayY);
#VARIABLES A USAR SEGUN LA FORMULA DE REGRESION LINEAL 
sumaX  = sum( dataX );
sumaY  = sum( dataY );
sumaX2 = sum( pow(dataX, 2) );
sumaY2 = sum( pow(dataY, 2) );
sumaXY = sum( dataX*dataY );
promedioX = sumaX / x_y_Items;
promedioY = sumaY / x_y_Items;
#SE CALCULA LA PENDIENTE
m = ( sumaX*sumaY - x_y_Items*sumaXY ) / ( pow(sumaX,2) - x_y_Items*sumaX2);
#SE CALCULA LA INTERSECCION
b = promedioY - m*promedioX;
#SE GRAFICA LA FUNCION Y LOS DATOS SE MUESTRAN COMO PUNTOS
plt.plot(dataX, dataY, 'C3:o', label='DATOS');
plt.plot(dataX, m*dataX + b, color='blue', label='RECTA');
plt.xlabel('X');
plt.ylabel('Y');
plt.title('REGRESIÓN LINEAL');
plt.grid();
plt.legend(loc=7);
plt.show();
#VERIFICACIÓN DEL COEFECIENTE DE DETERMINACIÓN
#SE CALCULA SIGMA DE X
sigmaX = np.sqrt( sumaX2 / x_y_Items - pow(promedioX,2));
#SE CALCULA SIGMA DE Y
sigmaY = np.sqrt( sumaY2 / x_y_Items - pow(promedioY,2));
#SE CALCULA SIGMA DE X por Y
sigmaXY = sumaXY/x_y_Items - promedioX*promedioY;
#R ES EL COEFICIENTE DE DETERMINACION QUE NOS INDICA QUE TAN BUENA ES LA APROXIMACIÓN DEL METODO
R = (sigmaXY / (sigmaX*sigmaY) )**2;
#SE MUESTRA EL VALOR DE R
print("EL COEFICIENTE DE DETERMINACIÓN ES: " + str(R));
