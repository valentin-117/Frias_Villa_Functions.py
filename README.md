# Frias_Villa_Functions.py

#Practicando funciones
1- En Python una funcion es definida usando la palabra def como palabra clave 
![image](https://github.com/user-attachments/assets/fc28f9a0-b086-438c-829b-40b843339f6d)
![image](https://github.com/user-attachments/assets/0ae39ad4-d7b4-44bd-ba7a-31fefe900f52)

2- Para llamar a una funcion, use la funcion nombrada y seguida de parentesis:
![image](https://github.com/user-attachments/assets/46b1abea-0112-4d3b-bdcc-39b3f6f5e591)
![image](https://github.com/user-attachments/assets/77722230-b390-4d62-8ae3-2e32ed4f925d)

3- El siguiente ejemplo tiene una función con un argumento (fname). Cuando se llama a la función, pasamos un nombre, que se usa dentro de la función para imprimir el nombre completo:
![image](https://github.com/user-attachments/assets/97e80495-251b-458e-a8b6-b964abd04ba7)
![image](https://github.com/user-attachments/assets/366f4519-d747-43f3-bbda-7461d5f72e54)

4- De forma predeterminada, se debe llamar a una función con la cantidad correcta de argumentos. Lo que significa que si su función espera 2 argumentos, debe llamar a la función con 2 argumentos, ni más ni menos.
![image](https://github.com/user-attachments/assets/3b1593e6-c0be-4a89-9ff7-b16e1c614f1c)
![image](https://github.com/user-attachments/assets/ded3c7c0-5c8b-4213-8b85-2128d71950d6)

5- Esta función espera 2 argumentos, pero solo obtiene 1:
![image](https://github.com/user-attachments/assets/3172068e-c4d6-410a-be41-17c6cce27f3e)
![image](https://github.com/user-attachments/assets/40fe4d5e-7849-469a-9c4b-2f44358b31b9)

6- Si no sabe cuántos argumentos se pasarán a su función, agregue un * antes del nombre del parámetro en la definición de la función.
De esta manera, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia:
Si se desconoce el número de argumentos, agregue un * antes del nombre del parámetro:
![image](https://github.com/user-attachments/assets/7b14d732-6511-4ef1-8fe1-b2e4c03ed820)
![image](https://github.com/user-attachments/assets/779f32fc-c980-44c5-af4e-a4093555f776)

7- También puede enviar argumentos con la sintaxis clave = valor.
![image](https://github.com/user-attachments/assets/5b5725af-b40d-43aa-86b1-c6a907b57a48)
![image](https://github.com/user-attachments/assets/fbd422af-bd75-43c2-8a30-5aff548527a5)

8- Argumentos arbitrarios de palabras clave, **kwargs
Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue dos asteriscos: ** antes del nombre del parámetro en la definición de la función.
De esta manera, la función recibirá un diccionario de argumentos y podrá acceder a los elementos en consecuencia:
Si se desconoce el número de argumentos de palabras clave, agregue un doble ** antes del nombre del parámetro:

![image](https://github.com/user-attachments/assets/1cbef04d-30f4-4521-b201-3b7ccee8ca40)
![image](https://github.com/user-attachments/assets/af50dda6-d1a0-4f94-be5f-2c3645340d53)

9- Valor de parámetro predeterminado
El siguiente ejemplo muestra cómo utilizar un valor de parámetro predeterminado.
![image](https://github.com/user-attachments/assets/bd3fff1c-0db4-42c7-a2c7-bf94aab725a6)
![image](https://github.com/user-attachments/assets/a09bbf7b-d166-4715-a1a6-2796e09f6f9d)

10- Pasar una lista como argumento
Puede enviar cualquier tipo de argumento de datos a una función (cadena, número, lista, diccionario, etc.) y será tratado como el mismo tipo de datos dentro de la función.
![image](https://github.com/user-attachments/assets/faa93d79-1cbf-4ab2-bdff-4d21b20f1722)
![image](https://github.com/user-attachments/assets/fe270546-7748-4978-8299-cdd910393584)

11-Regresa Valores
Para permitir que una función devuelva un valor, utilice la declaración de retorno:
def my_function(x):
  
![image](https://github.com/user-attachments/assets/0cca75ab-1f6c-46d1-9bb6-7a333e5b9be3)
![image](https://github.com/user-attachments/assets/fdb2095e-bd8d-44a0-83a0-fc439f2c15d7)

12- La declaración del pass
Las definiciones de función no pueden estar vacías, pero si por alguna razón tiene una definición de función sin contenido, ingrese la instrucción pass para evitar recibir un error.
![image](https://github.com/user-attachments/assets/38cd7ccc-d490-46f8-8dda-80efe221200b)
![image](https://github.com/user-attachments/assets/8a4bf14c-d452-45a6-b2fe-cfe351a6ffea)


13- Argumentos sólo posicionales 
Puede especificar que una función pueda tener SÓLO argumentos posicionales o SÓLO argumentos de palabras clave.

Para especificar que una función solo puede tener argumentos posicionales, agregue , / después de los argumentos:

Ícono de validado por la comunidad

![image](https://github.com/user-attachments/assets/94f92a00-27f1-4ff9-bf7a-2fdaf15a9019)
![image](https://github.com/user-attachments/assets/eeb8928e-4298-49cd-bd3c-ac1f17aedea6)

14
Sin , / en realidad se le permite usar argumentos de palabras clave incluso si la función espera argumentos posicionales:
![image](https://github.com/user-attachments/assets/1f121844-9598-4282-987d-02c5c3a781d7)
![image](https://github.com/user-attachments/assets/ffc73b18-d65a-4650-8626-09e8c018bb9b)


15
Pero al agregar , / obtendrá un error si intenta enviar un argumento de palabra clave:
def my_function(x, /):
  print(x)

my_function(x = 3)
![image](https://github.com/user-attachments/assets/5fbd3352-746a-412d-a561-67e7e67cee8b)
![image](https://github.com/user-attachments/assets/faf504ae-9c99-4c85-8fad-7d42a7a0d3c2)

16
Argumentos de solo palabras clave
Para especificar que una función solo puede tener argumentos de palabras clave, agregue *, antes de los argumentos:
def my_function(*, x):
  print(x)
  ![image](https://github.com/user-attachments/assets/94f0d184-ea36-413b-b877-b122fce51c70)
  ![image](https://github.com/user-attachments/assets/ae73eb53-ec29-4485-840d-f52464aa6813)


17
Sin el *, se le permite utilizar argumentos posicionales incluso si la función espera argumentos de palabras clave:
![image](https://github.com/user-attachments/assets/e0a62de9-1a97-458e-8dce-d1154333f344)
![image](https://github.com/user-attachments/assets/86cbbfe1-2ac5-4c03-af5a-a644b89f0e9b)


18
Pero al agregar *, / obtendrás un error si intentas enviar un argumento posicional:
def my_function(*, x):
![image](https://github.com/user-attachments/assets/6303ba7d-51ee-4b07-9ef6-feb5c4a64ca6)
![image](https://github.com/user-attachments/assets/0d88c35a-276f-4a1e-84fa-99eab1b67f5f)


19
Combine solo posicional y solo palabras clave
Puede combinar los dos tipos de argumentos en la misma función.

Cualquier argumento antes de / es solo posicional y cualquier argumento después de * es solo de palabra clave.
def my_function(a, b, /, *, c, d):
![image](https://github.com/user-attachments/assets/078c73ca-334d-4ed6-ae18-5745869089ce)
![image](https://github.com/user-attachments/assets/782eed27-7e9c-421d-9249-64722efeda20)








