#!/usr/bin/env python
# coding: utf-8

# # Práctica Final
# 
# Enhorabuena!!! Ya el haber llegado hasta aquí es un logro más en tu camino para ser un experto del Big Data y del Machine Learning!! 
# 
# 
# <img src="./Images/happy.gif" alt="Drawing" style="width: 300px;"/>
# 
# Con esta práctica pondremos en valor todo lo que hemos visto a lo largo del módulo. Vamos allá!! 😄

# ## 1. Multiconjuntos
# 
# Este ejercicio pondrá a prueba tu habilidad resolver un problema usando vectores.
# 
# **Objetivos**:
# - Usar `Python`
# - Asegurar los fundamentos matemáticos detrás de las operaciones con conjuntos.
# 
# **Problema**: Implementar las operaciones de los multiconjuntos (utilizando las librerías y estructuras de datos vistas en el curso).
# 
# **Datos:**
# 
# Un multiconjunto es un conjunto en el que un elemento puede repetirse, es decir, cada elemento posee una multiplicidad (un número natural) que indica cuántas veces el elemento es miembro del conjunto. Por ejemplo, en el multiconjunto `{a, a, b, b, b, c}`, las multiplicidades de los miembros a, b, y c son 2, 3, y 1, respectivamente.
# 
# Al igual que los conjuntos, poseen las siguientes características y operaciones:
# - Cardinalidad: indica el número de elementos del multiconjunto. Por ejemplo, la cardinalidad del multiconjunto `{a, a, b, b, b, c}` es 6 (la suma de sus multiplicidades).
# - Inserción: permite insertar una ocurrencia de un elemento en el multiconjunto.
# - Eliminación: permite eliminar una ocurrencia de un elemento del multiconjunto.
# - Comparación: compara dos multiconjuntos para determinar si son iguales.
# - Pertenencia: determina si un elemento pertenece al multiconjunto.
# - Subconjunto: determina si un multiconjunto es subconjunto de otro.
# - Unión: conjunción de todos los elementos de dos multiconjuntos (sumando sus multiplicidades si un elementos está en los dos).
# - Intersección: elementos que están en los dos multiconjuntos quedándonos con la multiplicidad más pequeña.
# - Diferencia: restar a un multiconjunto los elementos de otro.

# In[45]:


### TODO: Crear una función que dada una lista devuelva un multiconjunto
### El multiconjunto que devuelve puede crearse con la estructura de datos que se quiera (incluso una lista)
### TU RESPUESTA ABAJO

def multiconjunto(elementos):
   
    mc = {}
    for element in elementos:
        if element in mc:
           mc[element] += 1
        else: 
            mc[element] = 1
           
    return mc
multiconjunto([1,1,1,3,3,1,4,5,1,5])


# In[ ]:





# 

# In[46]:


### TODO: Crear una función que dado un multiconjunto devuelva su cardinalidad
### TU RESPUESTA ABAJO

def cardinalidad(multiconjunto):
    mc = multiconjunto
    cardinalidad = len(mc)
    return cardinalidad

cardinalidad([1,1,1,3,3,1,4,5,1,5])


# In[49]:


### TODO: Crear una función que dado un multiconjunto y un elemento devuelva el multiconjunto con el elemento insertado
### TU RESPUESTA ABAJO

def inserta(multiconjunto, elemento):
    """
    Devuelve el multiconjunto habiendo insertado el elemento dado
    
    Argumentos:
        multiconjunto -- multiconjunto devuelto por la función creada anteriormente
        elemento -- elemento a insertar
    """
    mc=multiconjunto
def inserta(multiconjunto, elemento):
    if elemento in mc:
        mc[elemento] += 1
    else:
        mc[elemento]= 1

    return mc

inserta(mc,9)


# In[50]:


def multiconjunto(elementos):
   
    mc = {}
    for element in elementos:
        if element in mc:
           mc[element] += 1
        else: 
            mc[element] = 1
           
    return mc
multiconjunto([1,1,1,3,3,1,4,5,1,5])


# In[56]:


def cardinalidad(multiconjunto):
    mc = multiconjunto
    cardinalidad = len(mc)
    return cardinalidad

cardinalidad([1,1,1,3,3,1,4,5,1,5])


# In[67]:


def multiconjunto(elementos):
   
    mc = {}
    for element in elementos:
        if element in mc:
            mc[element] += 1
        else: 
            mc[element] = 1
           
    return mc

def inserta(multiconjunto, elemento):
    if elemento in multiconjunto:
        multiconjunto[elemento] += 1
    else:
        multiconjunto[elemento]= 1

    return multiconjunto

def elimina(multiconjunto, elemento):
    if elemento in multiconjunto:
        multiconjunto[elemento] -= 1
    return mc
mc= multiconjunto([1,1,1,3,3,1,4,5,1,5])
mc = inserta(mc,9)
mc


# mc = multiconjunto([1,1,1,3,3,1,4,5,1,5])
# mc = inserta(mc,9)

# In[62]:


mc


# In[68]:


### TODO: Crear una función que dado un multiconjunto y un elemento devuelva el multiconjunto con el elemento eliminado
### TU RESPUESTA ABAJO

def elimina(multiconjunto, elemento):
    """
    Devuelve el multiconjunto habiendo eliminado una ocurrencia del elemento dado
    
    Argumentos:
        multiconjunto -- multiconjunto devuelto por la función creada anteriormente
        elemento -- elemento a eliminar
    """
    def elimina(multiconjunto, elemento):
    if elemento in multiconjunto:
        multiconjunto[elemento] -= 1
    return mc

mc = elimina(mc, 9)
mc


# In[76]:


### TODO: Crear una función que dado un multiconjunto y un elemento devuelva si el elemento pertenece al multiconjunto
### TODO: Crear una función que dados dos multiconjuntos devuelva si el primero es subconjunto del segundo
### TODO: Crear una función que dados dos multiconjuntos devuelva si son iguales
### TU RESPUESTA ABAJO

def pertenece(multiconjunto, elemento):
    """
    Devuelve si el elemento pertenece al multiconjunto
    
    Argumentos:
        multiconjunto -- multiconjunto devuelto por la función creada anteriormente
        elemento -- elemento a determinar si pertenece
    """
    for elemento in multiconjunto:
        if elemento in multiconjunto:
            print("El elemento pertenece al multiconjunto")

def subconjunto(multiconjunto1, multiconjunto2):
    """
    Devuelve si multiconjunto1 es subconjunto de multiconjunto2
    
    Argumentos:
        multiconjunto1 -- multiconjunto devuelto por la función creada anteriormente
        multiconjunto2 -- multiconjunto devuelto por la función creada anteriormente
    """
    for elemento, frecuencia in multiconjunto2.items():
        if multiconjunto1 not in multiconjunto2 or multiconjunto1[elemeto]<frecuencia:
            return False

def iguales(multiconjunto1, multiconjunto2):
    """
    Devuelve si multiconjunto1 es igual a multiconjunto2
    
    Argumentos:
        multiconjunto1 -- multiconjunto devuelto por la función creada anteriormente
        multiconjunto2 -- multiconjunto devuelto por la función creada anteriormente
    """
    if len(multiconjunto1) != len(multiconjunto2):
        return False
    for elemento, frecuencia in multiconjunto2.items():
        if elemento not in multiconjunto1 or multiconjunto1[elemento] != frecuencia:
            return False
print(pertenece(mc, 1))
print(subconjunto(multiconjunto([1,3,4]), mc))
print(iguales(multiconjunto([1,3,4]), mc))


# In[82]:


### TODO: Crear una función que dados dos multiconjuntos devuelva su unión
### TODO: Crear una función que dados dos multiconjuntos devuelva su intersección
### TODO: Crear una función que dados dos multiconjuntos devuelva su diferencia
### TU RESPUESTA ABAJO

def union(multiconjunto1, multiconjunto2):
    """
    Devuelve la unión de los multiconjuntos
    
    Argumentos:
        multiconjunto1 -- multiconjunto devuelto por la función creada anteriormente
        multiconjunto2 -- multiconjunto devuelto por la función creada anteriormente
    """
    union = multiconjunto1
    for elemento, frecuencia in multiconjunto2.items():
        if elemento in union:
             union[elemento] = max(union[elemento], frecuencia)
        else:
            union[elemento] = frecuencia
    return union

def interseccion(multiconjunto1, multiconjunto2):
    """
    Devuelve la intersección de los multiconjuntos
    
    Argumentos:
        multiconjunto1 -- multiconjunto devuelto por la función creada anteriormente
        multiconjunto2 -- multiconjunto devuelto por la función creada anteriormente
    """
    interseccion={}
for elemento, frecuencia in multiconjunto1.items():
    if elemento in multiconjunto2:
            interseccion[elemento]= min(frecuencia,multiconjunto2[elemento])
return interseccion
def diferencia(multiconjunto1, multiconjunto2):
    """
    Devuelve la diferencia de los multiconjuntos
    
    Argumentos:
        multiconjunto1 -- multiconjunto devuelto por la función creada anteriormente
        multiconjunto2 -- multiconjunto devuelto por la función creada anteriormente
          """
diferencia = {}   
for elemento,frecuencia in multiconjunto1:
    if elemento not in multiconjunto2:
            diferencia[elemento]= diferencia
return diferencia

print(union(multiconjunto([1,3,4]), mc))
print(interseccion(multiconjunto([1,3,4]), mc))
print(diferencia(mc, multiconjunto([1,2,3,4])))


# ## 2. Singular Value Decomposition
# 
# Este ejercicio pondrá a prueba tu habilidad para usar Singular Value Decomposition para comprimir una imagen.
# 
# **Objetivos**
# - Usar `Python`
# - Entender los fundamentos de `SVD`.
# 
# **Problema:** Usar `SVD` para comprimir una imagen en blanco y negro.

# La imagen que deberas usar es la siguiente:

# In[31]:


import matplotlib.pyplot as plt
from scipy import misc
get_ipython().run_line_magic('matplotlib', 'inline')

# Load image
A = misc.face(gray=True)

plt.imshow(A, cmap=plt.cm.gray)


# Deberas crear tu propia función para calcular el error de reconstrucción, que viene definido por:
# 
# $$SSE =  \sum_{n}^{i=1}  \begin{Vmatrix}x_{i} -  \widehat{x}_i \end{Vmatrix} ^2 $$
# 
# Donde:
# 
# - $x_i$ son los valores de la matriz original X
# - $\widehat{x}_i$ son los valores de la matriz reconstruida

# In[83]:


### TODO: Función para calcular el error de reconstrucción
### TU RESPUESTA ABAJO

import numpy as np

def sse_score(X, X_hat):
    """
    Función para calcular el error de reconstrucción
    
    Argumentos:
        X -- Matriz Original
        X_hat -- Matriz Reconstruida
        
    Ejemplo:
        X = np.array([[1, 2], [3, 4]])
        X_hat = np.array([[1.01, 1.75], [2.81, 3.99]])
        sse = sse_score(X, X_hat) # -> 0.09879
    """
    diferencia = X-X_hat
    sse=np.sum(np.square(diferenca))
    return sse


# Una vez que ya tenemos la función `sse` hecha, podemos pasar a construir la función que ejecutará `SVM`.

# In[84]:


### TODO: Función para ejecutar SVM
### Tiene como entrada una matriz X
### Devuelve U, s, Vt

### Hint: S debe ser una matriz diagonal
### TU RESPUESTA ABAJO

def svm(X):
    """
    Función que ejecuta SVM y devuelve U, S, Vt
    
    Argumentos:
        X -- Matriz Original
        
    Ejemplo:
        X = np.array([[1, 2], [3, 4]])
        U, S, Vt = svm(X)  
        
        # -> U = array([[-0.40455358, -0.9145143 ],
        #               [-0.9145143 ,  0.40455358]])
        # -> S = array([[5.4649857 , 0.        ],
        #               [0.        , 0.36596619]])   
        # -> Vt = array([[-0.57604844, -0.81741556],
        #                [ 0.81741556, -0.57604844]])          
    """ 
    U, S, Vt = np.linalg.svd(X)
    k = min(X.shape)
    X_hat = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))
    sse = sse_score(X, X_hat)
    
    return U, np.diag(S), Vt, sse


# In[85]:


U


# In[86]:


S


# In[87]:


Vt


# Como hemos visto en clase, las matrices obtenidas a partir de `SVM` nos sirven para reconstruir la matriz original `X`. Para ello, construye una función que permita reconstruir la matriz original `X` a partir de `U, s, Vt`.

# In[ ]:


### TODO: Función para reconstruir la matriz original a partir de U, s, Vt
### Tiene como entrada U, s, Vt
### Devuelve X_hat
### TU RESPUESTA ABAJO


def reconstruction(U, S, Vt):
    """
    Función que reconstruye la matriz original a partir de U, s, Vt
    
    Argumentos:
        U -- Matriz de Singular Vectors
        s -- Matriz de Eigenvalues
        Vt -- Matriz de Singular Vectors
        
    Ejemplo:
        U = np.array([[-0.40455358, -0.9145143 ],
                      [-0.9145143 ,  0.40455358]])
        S = np.array([[5.4649857 , 0.        ],
                      [0.        , 0.36596619]])
        Vt = np.array([[-0.57604844, -0.81741556],
                       [ 0.81741556, -0.57604844]])
        X_hat = reconstruction(U, S, Vt)
        
        # X_hat -> array([[0.99999999, 1.99999998],
        #                 [3.00000003, 4.00000001]])
        
    """
    X_hat = np.dot(U, np.dot(S, Vt))
    
    return X_hat


# Calcula el error de reconstrucción usando la función `sse` que has programado anteriormente.

# In[ ]:


def sse_score(X,X_hat):
diferencia= X-X_hat
sse = np.sum(np.square(diferencia))
    
return sse

def error(X,X_hat):
     return sse_score(X, X_hat)


# Una vez que hemos programado todas las funciones necesarias para realizar `SVM` y medir el error de reconstrucción, podemos proceder a realizar la compresión de la imagen. Esta [página web](http://timbaumann.info/svd-image-compression-demo/) te ayudará a repasar y a entender como calcular la compresión.
# 
# Debes usar la siguiente imagen: 

# In[32]:


# Load image
A = misc.face(gray=True)

plt.imshow(A, cmap=plt.cm.gray)


# In[88]:


### TODO: Función que recibe una imagen A y devuelve la imagen comprimida
### Tiene como entrada A y el número de componentes para realizar la reducción de dimensionalidad
### Devuelve la imagen comprimidad, el error de reconstrucción y el ratio de compresión

### Hint: Usa las funciones anteriormente construidas
### TU RESPUESTA ABAJO


def image_compression(A, n_components):
    """
    Función para comprimir una imagen A
    
    Argumentos:
        A -- Imagen original
        n_components -- Número de componentes
        
    Ejemplo:
        A_hat, sse, comp_ratio = image_compression(A, n_components=50)
    """
    U, S, Vt = np.linalg.svd(A)
    
    U_red = U[:, :num_componentes]
    S_red = np.diag(S[:num_componentes])
    Vt_red = Vt[:num_componentes, :]
    
    imagen_comprimida = np.dot(U_red, np.dot(S_red, Vt_red))
    error_reconstruccion = sse_score(A, imagen_comprimida)
    
    tamaño_original = A.shape[0] * A.shape[1]
    tamaño_comprimido = U_red.size + S_red.size + Vt_red.size
    ratio_compresion = tamaño_original / tamaño_comprimido
    
    return imagen_comprimida, error_reconstruccion, ratio_compresion


# Grafica la imagen original `X` y la imagen reconstruida `X_hat`, y imprime el error de reconstrucción `sse` y el `ratio de compresion`.

# In[ ]:


imagenA = cv2.imread("imagen.jpg", cv2.IMREAD_GRAYSCALE)

num_componentes = 50
imagen_comprimida, error_reconstruccion, ratio_compresion = comprimir_imagen(imagen_original, num_componentes)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagen_original, cmap='gray')
plt.title('Imagen Original')

plt.subplot(1, 2, 2)
plt.imshow(imagen_comprimida, cmap='gray')
plt.title('Imagen Reconstruida')

plt.show()


# ## 3. Linear Regression - Least Squares
# 
# Este ejercicio pondrá a prueba tu habilidad para programar tu propia versión de mínimos cuadrados en Python.
# 
# **Objetivos**:
# - Usar `Python` + `Pandas` para leer y analizar los datos.
# - Asegurar los fundamentos matemáticos detrás del método de los mínimos cuadrados.
# 
# **Problema**: Usando datos sobre el precio de la vivienda, intentaremos predecir el precio de una casa en base a la superficie habitable con un modelo de regresión.
# 
# **Datos:** [Kaggle's House Prices Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)

# ### Repaso
# 
# Usaremos la versión matricial de la solución de los **métodos de los mínimos cuadrados** para resolver este problema. Como recordatorio, expresamos los coeficientes $w_{LS}$ como un vector, y calculamos ese vector en base a la matriz de entrada $X$ y en base a $y$.<br><br>
# 
# 
# 
# Como mostramos en clase, la matriz $X$ siempre contiene un vector de valores $1$ en la primera columna. En otras palabras:<br><br>
# 
# <center>$
# X = \begin{bmatrix}
# 1 \  x_{11}  \\
# 1 \  x_{21}  \\
# \vdots \ \vdots \\
# 1 \ x_{n1}
# \end{bmatrix} 
# $</center>
# 
# Para dos variables, $X$ tomará esta forma:
#  
# <center>$
# X = \begin{bmatrix}
# 1 \  x_{11} \  x_{12} \\
# 1 \  x_{21} \  x_{22} \\
# \vdots \ \vdots \\
# 1 \ x_{n1} \  x_{n2}
# \end{bmatrix} 
# $</center>
# 
# ### Exploratorio de datos

# In[89]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)


# In[90]:


### Leer los datos
tr_path = './data/train.csv'
data = pd.read_csv(tr_path)


# In[35]:


### La función .head() muestras las primeras lineas de los datos
data.head()


# In[ ]:


### Lista con los nombres de las columnas
data.columns
import pandas as pd

data = pd.read_csv("house_prices.csv")
nombres_columnas = data.columns.tolist()
print(nombres_columnas)


# In[ ]:


### TODO: Numero de columnas 
### Asignar int variable a: ans1
### TU RESPUESTA ABAJO
import pandas as pd
data = pd.read_csv("house_prices.csv")
num_columnas = data.shape[1]
ans1 = num_columnas


# #### Visualizaciones

# In[91]:


### Podemos graficar los datos price vs living area - Matplotlib

Y = data['SalePrice']
X = data['GrLivArea']

plt.scatter(X, Y, marker = "x")

### Anotaciones
plt.title("Sales Price vs. Living Area (excl. basement)")
plt.xlabel("GrLivArea")
plt.ylabel("SalePrice");


# In[ ]:


### price vs year - Pandas

data.plot('YearBuilt', 'SalePrice', kind = 'scatter', marker = 'x');
data = pd.read_csv("house_prices.csv")
data.plot(x='YearBuilt', y='SalePrice', kind='scatter', marker='x')
lt.title("Precio de Venta vs. Año de Construcción")
plt.xlabel("Año de Construcción")
plt.ylabel("Precio de Venta")

plt.show()


# ### Regresión Lineal
# 
# Ya que conocemos la ecuación para $w_{LS}$ tenemos todo lo necesario para resolver la regresión lineal. Vamos allá!<br><br>
# 
# <center>$w_{LS} = (X^T X)^{-1}X^T y,$</center>
# 

# In[92]:


### TODO: Función para invertir una matriz
### Contruye una función que toma como input una matriz
### Devuelve la inversa de dicha matriz
### TU RESPUESTA ABAJO

def inverse_of_matrix(mat):
    """Calcula y devuelve la inversa de la matriz
    
    Argumentos:
        mat -- Matriz cuadrada a invertir
        
    Ejemplo:
        sample_matrix = [[1, 2], [3, 4]]
        the_inverse = inverse_of_matrix(sample_matrix)  
        # -> the_inverse = [[-2.   1. ]
        #                   [ 1.5 -0.5]]
    
    Requerimientos:
        Esta función depende de 'numpy.linalg.inv'
    """
   
    mat= np.linalg.inv(matriz)
    
    return mat


# #### Leer los datos
# 
# Lo primero que debemos hacer es leer los datos, para ello construye una función que reciba el directorio de un archivo .csv `file_path` y lo lea usando `pandas`, la función debe devolver el dataframe.

# In[ ]:


### TODO: Función para leer un .csv
### La función recibe un file_path y debe devolver el dataframe
### TU RESPUESTA ABAJO

import pandas as pd

def read_to_df(file_path):
    """Leer un archivo .csv"""

dataframe = read_to_df(tr_path)
dataframe = pd.read_csv(file_path)
    
    return dataframe


# #### Subset del dataframe por columnas
# 
# Queremos construir una función que nos permita obtener los datos de ciertas columnas. Por ello, le pasaremos como argumento un `dataframe` y una lista con los nombres de las columnas que queremos extraer `column_names` y nos devolverá un dataframe con solo esas columnas.

# In[93]:


### TODO: Función para extraer los datos de ciertas columnas
### Como argumentos, recibe un dataframe `data_frame`y una lista con los nombres de las columnas `column_names`
### Devuelve un dataframe con solo las columnas que le hemos especificado
### TU RESPUESTA ABAJO

def select_columns(data_frame, column_names):
    """Devuelve un subset del dataframe en base a los nombres de las columnas
    
    Argumentos:
        data_frame -- Dataframe Object
        column_names -- Lista con los nombres de las columnas a seleccionar
        
    Ejemplo:
        data = read_into_data_frame('train.csv')
        selected_columns = ['SalePrice', 'GrLivArea', 'YearBuilt']
        sub_df = select_columns(data, selected_columns)
    """
    new_data_frame = data_frame[column_names]
    
    return new_data_frame


# #### Subset del dataframe por valores
# 
# El siguiente paso es construir una función que recibe un `data_frame`, el nombre de una columna, un valor mínimo y un valor máximo `cutoffs`. Nos devuelve un dataframe excluyendo las filas donde el valor de la columna indica está fuera de los valores mínimos y máximos que le hemos indicado.

# In[94]:


### TODO: Función para crear un nuevo subset en base a valores
### Como argumento recibe un dataframe y una lista de tuples
### Tuples: (column_name, min_value, max_value)
### Devuelve un dataframe que excluye las filas donde los valores, en la columna que le hemos indicado, exceden los valores
### que le hemos indicado
### No eliminar la fila si los valores son iguales al min/max valor
### TU RESPUESTA ABAJO

def column_cutoff(data_frame, cutoffs):
    """Crea un nuevo dataframe en base a unos límites
    
    Argumentos:
        data_frame -- Dataframe Object
        cutoffs -- Lista de tuples con el siguiente formato:
        (column_name, min_value, max_value)
        
    Ejemplo:
        data_frame = read_into_data_frame('train.csv')
        # Remove data points with SalePrice < $50,000
        # Remove data points with GrLiveAre > 4,000 square feet
        cutoffs = [('SalePrice', 50000, 1e10), ('GrLivArea', 0, 4000)]
        selected_data = column_cutoff(data_frame, cutoffs)
    """
    nuevo_data_frame = data_frame.copy()
    
    for columna, min_valor, max_valor in cutoffs:
        nuevo_data_frame = nuevo_data_frame[(nuevo_data_frame[columna] >= min_valor) & 
                                            (nuevo_data_frame[columna] <= max_valor)]
    
    return nuevo_data_frame


# #### Mínimos Cuadrados / Least Squares
# 
# Ahora, implementarás la ecuación $w_{LS}$:
# 
# <center>$w_{LS} = (X^T X)^{−1}X^T y,$</center>

# In[ ]:


### TODO: Función para resolver la ecuación wLS
### Toma como argumentos dos matrices, una para X y otra para y
### Asumimos que las matrices tienen las dimensiones correctas

### Paso 1: Asegurate que n > d. 
### Es decir, que el número de observaciones es mayor que el número de dimensiones.
### O lo que es lo mismo, que el número de filas de cada matriz sea mayor que el número de columnas
### Si no es así, debes transponer las matrices

### Paso 2: Debes añadir a la matriz X un vector columna del tamaño (n x 1)

### Paso 3: Usa la ecuación de arriba para obtener wLS

### TU RESPUESTA ABAJO


def least_squares_weights(input_x, target_y):
    """Resuelve la ecuación para wLS
    
    Argumentos:
        input_x -- Matriz con los datos de entrenamiento
        target_y -- Vector con los datos de salida
        
    Ejemplo:
        import numpy as np
        training_y = np.array([[208500, 181500, 223500, 
                                140000, 250000, 143000, 
                                307000, 200000, 129900, 
                                118000]])
        training_x = np.array([[1710, 1262, 1786, 
                                1717, 2198, 1362, 
                                1694, 2090, 1774, 
                                1077], 
                               [2003, 1976, 2001, 
                                1915, 2000, 1993, 
                                2004, 1973, 1931, 
                                1939]])
        weights = least_squares_weights(training_x, training_y)
        
        print(weights)  #--> np.array([[-2.29223802e+06],
                        #              [ 5.92536529e+01],
                        #              [ 1.20780450e+03]])
                           
        print(weights[1][0]) #--> 59.25365290008861
    
    Asumimos:
        -- target_y es un vector con el mismo número de observaciones que input_x
    """
     n, d = X.shape
    if n <= d:
        X = X.T
        n, d = X.shape
    
    X = np.hstack((X, np.ones((n, 1))))
    
    XTX_inv = np.linalg.inv(X.T @ X)
    wLS = XTX_inv @ X.T @ y
    
return wLS


# #### Testing en datos reales
# 
# Ahora que ya hemos programado todas las funciones necesarias para calcular la regresión lineal vamos a aplicar al conjunto de datos que habíamos seleccionado al principio. 
# 
# **Datos:** [Kaggle's House Prices Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
# 
# Si tus funciones están correctamente programadas, la siguiente celda correrá sin problemas 😃

# In[95]:


test_path = './data/train.csv'
df = read_to_df(test_path)
df_sub = select_columns(df, ['SalePrice', 'GrLivArea', 'YearBuilt'])

cutoffs = [('SalePrice', 50000, 1e10), ('GrLivArea', 0, 4000)]
df_sub_cutoff = column_cutoff(df_sub, cutoffs)

X = df_sub_cutoff['GrLivArea'].values
Y = df_sub_cutoff['SalePrice'].values

### reshaping for input into function
training_y = np.array([Y])
training_x = np.array([X])

weights = least_squares_weights(training_x, training_y)
print(weights)


# In[96]:


max_X = np.max(X) + 500
min_X = np.min(X) - 500

### Choose points evenly spaced between min_x in max_x
reg_x = np.linspace(min_X, max_X, 1000)

### Use the equation for our line to calculate y values
reg_y = weights[0][0] + weights[1][0] * reg_x

plt.plot(reg_x, reg_y, color='#58b970', label='Regression Line')
plt.scatter(X, Y, c='k', label='Data')

plt.xlabel('GrLivArea')
plt.ylabel('SalePrice')
plt.legend()
plt.show()


# #### Implementación con sklearn
# 
# Podemos comprobar como el resultado de nuestro código es exactamente igual al resultado de `sklearn`. Enhorabuena! Has programado tu propia **regresión lineal!!** 😃

# In[97]:


from sklearn.linear_model import LinearRegression

lr = LinearRegression()

### SKLearn requiere un array 2-dimensional X y 1 dimensional y.
### skl_X = (n,1); skl_Y = (n,)
skl_X = df_sub_cutoff[['GrLivArea']]
skl_Y = df_sub_cutoff['SalePrice']

lr.fit(skl_X,skl_Y)
print("Intercept:", lr.intercept_)
print("Coefficient:", lr.coef_)


# ## 4. Linear Regression - Gradient Descent
# 
# En este ejercicio resolveras el mismo problema anterior pero usando **Gradient Descent**
# 
# **Objetivos**:
# - Asegurar los fundamentos matemáticos detrás del Gradient Descent.
# 
# **Problema**: Usando datos sobre el precio de la vivienda, intentaremos predecir el precio de una casa en base a la superficie habitable con un modelo de regresión.
# 
# **Datos:** [Kaggle's House Prices Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
# 
# **Repaso:**
# 
# $$ RSS(w) = \sum_{n=1}^{N}[y_n-f(x_n)]^2 =  \sum_{n=1}^{N}[y_n- (w_0 + \sum_{d=1}^{D}w_dx_{nd}) ]^2 .$$
# 
# Loss function:
# 
# $$ RSS(w) = \frac{1}{2}\sum_{n=1}^{N}[y_n-f(x_n)]^2$$
# 
# Y lo que queremos es minimizar esta distancia, para que el modelo se acerque lo máximo posible a los valores verdaderos.
# 
# $$\nabla RSS(w) = X^T(Xw^t-y)$$
# 
# En resumen, el gradient descendiente para una regresión lineal, se basa en resolver esta ecuación de forma iterativa:
# 
# $$w^{t+1} = w^t - \eta * \nabla RSS(w)$$

# #### Leer Datos

# In[ ]:


import pandas as pd
import numpy as np

# Leer datos
data = pd.read_csv('./data/train.csv')

# Extraer dichas columnas
newData = data[['GrLivArea','SalePrice']]
print(newData.head())

# Contruir x - y
x = newData['GrLivArea']
y = newData['SalePrice']

# Standarizar los datos
x = (x - x.mean()) / x.std()
x = np.c_[np.ones(x.shape[0]), x] 

print("Shape of X: ", x.shape)
print("Shape of y:", y.shape)


# #### Gradient Descent

# In[101]:


### TODO: Función para encontrar los valores w usando Gradient Descent
### Toma como argumentos: X, y, w, n_iterations, eta
### Completa la función añadiendo la loss función y la updating rule
### TU RESPUESTA ABAJO

def gradient_descent(x, y, w, iterations, eta):
    """Gradient descent
    
    Argumentos:
        x -- Matriz con los datos de entrenamiento
        y -- Vector con los datos de salida
        w -- Vector aleatoriamente inicializado
        iterations -- Número de iteraciones
        eta -- Learning Rate
        
    Ejemplo:
        import numpy as np

        # Learning rate
        eta = 0.01 

        # Número de iteraciones
        iterations = 2000 #No. of iterations

        # Seed para inicializar w
        np.random.seed(123)
        w0 = np.random.rand(2)
        
        training_y = np.array([208500, 181500, 223500, 
                                140000, 250000])
        training_x = np.array([[ 1.        ,  0.37020659],
                               [ 1.        , -0.48234664],
                               [ 1.        ,  0.51483616],
                               [ 1.        ,  0.38352774],
                               [ 1.        ,  1.29888065]])
                            
        weights, loss = gradient_descent(training_x, training_y, w0, iterations, eta)
        
        print(weights[-1])  #--> np.array([183845.82320222  40415.66453324])
    """
    loss_history = []
    
    for _ in range(iterations):
        prediction = np.dot(x, w)
        error = prediction - y
        
        loss = 0.5 * np.sum(error ** 2)
        loss_history.append(loss)
        gradient = np.dot(x.T, error)
        w -= eta * gradient
        
    return w, loss_history


# Una vez construida nuestra función para el Gradient Descent podemos usarla para encontrar los valores optimos de $w$. **Prueba a modificar el learning rate para ver la convergencia del Gradient Descent.**

# In[102]:


import numpy as np

# Learning rate
eta = 0.001 

# Número de iteraciones
iterations = 1000 #No. of iterations

# Seed para inicializar w
np.random.seed(123)
w0 = np.random.rand(2)

weights, loss = gradient_descent(x, y, w0, iterations, eta)

print(weights[-1])


# In[103]:


type(x)


# Hemos creado la siguiente función para ver como Gradient Descent encuentra el resultado final - **Tarda un poco**

# In[104]:


import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definir figure
fig = plt.figure()
ax = plt.axes()
plt.title('Sale Price vs Living Area')
plt.xlabel('Living Area in square feet (normalised)')
plt.ylabel('Sale Price ($)')
plt.scatter(x[:,1], y, color='red')
line, = ax.plot([], [], lw=2)
annotation = ax.text(-1, 700000, '')
annotation.set_animated(True)
plt.close()

# Generar animacion de los datos
def init():
    line.set_data([], [])
    annotation.set_text('')
    return line, annotation

# Función para la animación
def animate(i):
    x = np.linspace(-5, 20, 1000)
    y = weights[i][1]*x + weights[i][0]
    line.set_data(x, y)
    annotation.set_text('loss = %.2f e10' % (loss[i]/10000000000))
    return line, annotation

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=300, interval=0, blit=True)

anim.save('animation.gif', writer='imagemagick', fps = 30)

# Visualizar la animación
import io
import base64
from IPython.display import HTML

filename = 'animation.gif'

video = io.open(filename, 'r+b').read()
encoded = base64.b64encode(video)
HTML(data='''<img src="data:image/gif;base64,{0}" type="gif" />'''.format(encoded.decode('ascii')))


# ## (Opcional) - Calculando similitud entre páginas web
# 
# Este ejercicio pondrá a prueba tu capacidad para encontrar la similitud entre vectores usando cosine similarity.
# 
# **Objetivos**:
# - Usar `Python` + `BeautifulSoup` para "scrapear" páginas webs.
# - Asegurar los fundamentos matemáticos detrás del cosine similarity.
# 
# **Problema**: Dadas N páginas web, extraer el texto de ellas y determinar la similitud.
# 
# ### Repaso
# 
# Como recordarás, podemos medir la similitud entre vectores usando la siguiente ecuación:<br>
# 
# <center>$\overrightarrow{u} \cdot \overrightarrow{v} = |\overrightarrow{u}||\overrightarrow{v}| \cos \theta $</center>
# 
# Que podemos reescribir de la siguiente forma:<br>
# 
# <center>$\cos \theta = \frac{\overrightarrow{u} \cdot \overrightarrow{v}}{|\overrightarrow{u}||\overrightarrow{v}|}$</center>
# 
# La **similitud** va a venir dada por el ángulo $\theta$, que nos indicará lo siguiente:
# 
# <img src="./Images/cosine_sim.png" width=70%/>
# 
# ### Web scraping
# 
# La técnica llamada `web scraping` es la utilizada normalmente para extraer contenido de páginas webs y posteriormente procesarlos. Por ejemplo, si quisieramos construir una base de datos para entrenar un modelo con imágenes de ropa para hombres, podríamos intentar "scrapear" dicha sección de la página web del El Corte Inglés para conseguir las imágenes (no es tan fácil como suena).

# In[ ]:


# Estas librerias deben ser instaladas para hacer este ejercicio
get_ipython().system('pip install beautifulsoup4')
get_ipython().system('pip install lxml')


# In[ ]:


import re
import lxml
from bs4 import BeautifulSoup
import urllib
import urllib.request

url = "https://es.wikipedia.org/wiki/Canis_lupus_familiaris"

def parse_from_url(url):
    """
    Función para extraer el contenido (raw text) de una página web
    """
    
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser" )
    for script in soup(["script", "style"]):
        script.extract()
        
    text = soup.get_text()
    
    # Eliminar saltos de linea
    text = re.sub('\s+', ' ', text)
    return text

parse_from_url(url)[:1000]


# In[ ]:


### TODO: Escribe una función que reciba una lista de urls
### Aplica web scraping a cada una de ellas para extraer el contenido
### Y devuelva un diccionario con el contenido por cada url

### HINT: Usa la función anterior
### NOTE: Suele tardar un poco en extraer el contenido de las paginas web
### TU RESPUESTA ABAJO

def get_content(url_ls):
    """Extrae el contenido de una lista de urls
    
    Argumentos:
        url_ls -- Lista con urls
        
    Ejemplo:
        url_ls = ['https://es.wikipedia.org/wiki/Canis_lupus_familiaris', 
        'https://es.wikipedia.org/wiki/Canis_lupus',
        'https://es.wikipedia.org/wiki/Felis_silvestris_catus']
        
        url2content = get_content(url_ls)  
    
    Requerimientos:
        Esta función depende de 'parse_from_url()'
    """


# ### Preprocesado
# 
# Como es lógico, no podemos resolver esta ecuación $\cos \theta = \frac{\overrightarrow{u} \cdot \overrightarrow{v}}{|\overrightarrow{u}||\overrightarrow{v}|}$ usando texto sin más, debemos convertir cada página web a un vector.

# In[ ]:


### TODO: Escribe una función que reciba texto
### Y devuelva una lista con el texto separado por espacios
### Además del set de la lista
### "hola que que tal" - ["hola", "que", "que", "tal"], {"hola", "que", "tal"}
### TU RESPUESTA ABAJO

def tokenizer(text):
    """Divide el texto en palabras
    
    Argumentos:
        text -- String
        
    Ejemplo:
        url_ls = "Hola me llamo llamo Alex y estamos aprendiendo Algebra y estamos bien"
        
        tokens_txt, set_txt = tokenizer(url_ls)  
    
    Requerimientos:
        No uses ningún tokenizer ya implementado (nltk, spacy, ...)
    """


# El siguiente paso es crear un conjunto con las palabras de ambas páginas web (unión), por ejemplo:
# 
# - Los perros son maravillosos...
# - Los maravillosos años 80...
# 
# Por tanto, el conjunto para estas dos frases sería `{"los", "perros", "son", "maravillosos", "años", "80"}`. Debemos realizar esto para todas las combinaciones posibles, es decir:
# 
# - web_1
# - web_2
# - web_3
# 
# En este caso, las combinaciones serían (no importa el orden) `[web_1, web_2]`, `[web_1, web_3]`, `[web_2, web_3]`

# In[ ]:


### TODO: Escribe una función que recibe una lista de N páginas web
### Y calcula todas las combinaciones posibles entre ellas, no importa el orden
### [web_1, web_2, web_3, ...]
### Devuelve una lista de tuples con las combinaciones [(web_1, web_2), (web_1, web_3), ...]

# HINT: Puedes implementar esta función como quieras pero la librería itertools 
#       proporciona una función llamada `combinations` para realizar esta tarea.

### TU RESPUESTA ABAJO
import itertools
    
def combinations(url_ls):
    """Calcula todas las combinaciones posibles entre los elementos de una lista
    
    Argumentos:
        url_ls -- Lista de urls
        
    Ejemplo:
        url_ls = ['https://es.wikipedia.org/wiki/Canis_lupus_familiaris', 
        'https://es.wikipedia.org/wiki/Canis_lupus',
        'https://es.wikipedia.org/wiki/Felis_silvestris_catus']
        
        permutation = combinations(url_ls)  
    
    Requerimientos:
        Puedes implementar esta función como quieras pero la librería itertools 
        proporciona una función llamada `combinations` para realizar esta tarea.
    """


# In[ ]:


### TODO: Escribe una función que recibe una lista con tuples
### [({'que', 'hola'}, {'que', 'es', 'guay'}), ({'que', 'hola'}, {'madrid', 'la', 'es'})]
### Y devuelve una lista con la union de los conjuntos
### [({'que', 'hola', 'es', 'guay'}), ({'que', 'hola', 'madrid', 'la', 'es'})]
### TU RESPUESTA ABAJO

def union(comb_ls):
    """Calcula la unión por cada tuple de una lista 
    
    Argumentos:
        comb_ls -- Lista de tuples
        
    Ejemplo:
        comb_ls = [({'que', 'hola'}, {'que', 'es', 'guay'}), ({'que', 'hola'}, {'madrid', 'la', 'es'})]
        
        union_ls = union(comb_ls)  # -> [{'es', 'que', 'hola', 'guay'}, {'es', 'que', 'hola', 'madrid', 'la'}]
    """


# Una vez que tenemos una lista de conjuntos por cada par de páginas web, podemos convertir el texto de la página web a un vector.

# In[ ]:


def set2vector(tokens_web1, tokens_web_2, set_web1, set_web2):
    """
    Función para convertir un conjunto a vector
    
    Argumentos:
        tokens_web1 -- Contenido tokenizado de página web 1
        tokens_web_2 -- Contenido tokenizado de página web 2
        set_web1 -- Conjunto de palabras de la página web 1
        set_web2 -- Conjunto de palabras de la página web 2
        
    Ejemplo:
        tokens_web1 = ["hola", "que", "tal", "soy", "Alex"]
        tokens_web_2 = ["hola", "me", "llamo"]
        set_web1 = {"hola", "que", "tal"}
        set_web2 = {"hola", "me", "llamo"}
        union_ls = set2vector(tokens_web1, tokens_web_2, set_web1, set_web2)  
        
    Requerimientos:
        Depende de la función `union()`
    """
    
    # Unimos los conjuntos
    join_set = union([(set_web1, set_web2)])[0]
    
    web1_array = []
    web2_array = [] 

    for word in join_set:
        if word in tokens_web1:
            web1_array.append(1)
        else:
            web1_array.append(0)
        if word in tokens_web_2:
            web2_array.append(1)
        else:
            web2_array.append(0)

    return web1_array, web2_array

tokens_web1 = ["hola", "que", "tal", "soy", "Alex"]
tokens_web_2 = ["hola", "me", "llamo"]
set_web1 = {"hola", "que", "tal", "soy", "Alex"}
set_web2 = {"hola", "me", "llamo"}
web1_array, web2_array = set2vector(tokens_web1, tokens_web_2, set_web1, set_web2)  


# In[ ]:


print(web1_array, web2_array)


# ### Cosine Similarity
# 
# Por último, ya podemos implementar la ecuación: $\cos \theta = \frac{\overrightarrow{u} \cdot \overrightarrow{v}}{|\overrightarrow{u}||\overrightarrow{v}|}$

# In[ ]:


### TODO: Escribe una función que recibe dos vectores, u y v
### Y devuelva la similaridad entre ambos vectores
###
### Paso 1: Si u y v son listas -> Convertirlo a arrays
###
### Paso 2: Calcula la similaridad entre ambos vectores
### TU RESPUESTA ABAJO

import numpy as np

def cosine_similarity(u, v):
    """Calcula la similaridad entre dos vectores
    
    Argumentos:
        u -- Vector 1
        v -- Vector 2
        
    Ejemplo:
        u = np.array([1, 2, 3])
        v = np.array([3, 2, 1])
        
        similarity = cosine_similarity(u, v)  # -> 0.71428
    """


# In[ ]:


def websites_sim(url_ls):
    """Función para calcular la similaridad entre páginas web
    
    Argumentos:
        url_ls -- Listas de páginas web
        
    Ejemplo:
        url_ls = ['https://es.wikipedia.org/wiki/Canis_lupus_familiaris', 
        'https://es.wikipedia.org/wiki/Canis_lupus',
        'https://es.wikipedia.org/wiki/Felis_silvestris_catus']
        
        similarity_ls = websites_sim(url_ls)  
    """
    
    url2content = get_content(url_ls)
    
    # Creamos un diccionario donde cada url tendrá su contenido tokenizado y su conjunto
    url_dict = {}
    for url, content in url2content.items():
        toks, sets = tokenizer(content)
        url_dict[url] = {'tokens': toks,
                        'unique_tokens': sets}
    
    # Calculamos todas las combinaciones posibles de las direcciones de las páginas web
    comb_ls = combinations(url_ls)

    # Usando comb_ls y la función `set2vector()` convertimos cada página web a vectores
    print("Similaridad: ")
    for el in comb_ls:
        # Obtenemos los tokens y el conjunto para cada página web
        token_1 = url_dict[el[0]]['tokens']
        token_2 = url_dict[el[1]]['tokens']
        set_1 = url_dict[el[0]]['unique_tokens']
        set_2 = url_dict[el[1]]['unique_tokens']
        array_web1, array_web2 = set2vector(token_1, token_2, set_1, set_2)
        similarity = cosine_similarity(array_web1, array_web2)
        
        print("{} vs {} - {}".format(el[0], el[1], round(similarity, 3)))

                      
url_ls = ['https://es.wikipedia.org/wiki/Canis_lupus_familiaris', 
'https://es.wikipedia.org/wiki/Canis_lupus',
'https://es.wikipedia.org/wiki/Felis_silvestris_catus']

similarity_ls = websites_sim(url_ls) 


# In[ ]:




