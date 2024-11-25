David Urdaneta - Social Oplesk - Programa Fullstack - Grupo 9
---

# Solución de Hacks #7

## Tecnologías utilizadas
[![My Skills](https://skillicons.dev/icons?i=py,flask)](https://skillicons.dev)


## Tabla de contenidos
- [Instrucciones de Instalación](#instrucciones-de-instalación)
- [Pruebas](#pruebas)
- [Descripción de los Hacks](#descripción-de-los-hacks)
- [Adicional: Problemas para cerrar el servidor de Flask en segundo plano](#adicional-problemas-para-cerrar-el-servidor-de-flask-en-segundo-plano)

---

## Instrucciones de Instalación

1. **Clonar el Repositorio**
   
   ```bash
   git clone https://github.com/davidjuo96/hack_07_backend_python_01
   ```

2. **Crear un Entorno Virtual (aquí)**  
   Crea un entorno virtual para instalar las dependencias de Python de forma aislada:

   ```bash
   python -m venv venv
   ```

3. **Activar el Entorno Virtual (aquí)**  
   Activa el entorno virtual para que puedas instalar dependencias y ejecutar el proyecto dentro de este entorno. En Windows:

   ```bash
   source venv/Scripts/activate
   ```

   Si estás usando **Linux** o **macOS**, usa:

   ```bash
   source venv/bin/activate
   ```

4. **Cambiar al Directorio del Proyecto (aquí)**  
   Navega al directorio del proyecto clonado:

   ```bash
   cd hack_07_backend_python_01/
   ```

5. **Instalar Requerimientos**  
   Instala las dependencias necesarias para el proyecto desde el archivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

---

## Pruebas

Para verificar cada hack, se utilizan pruebas con `pytest`:

- **Ejecutar el servidor Flask en segundo plano:**  
  Inicia el servidor en modo debug y libera la terminal para ejecutar otros comandos:
  ```bash
  flask run --debug &
  ```

- **Ejecutar pruebas globales:**  
  Corre todos los tests definidos con `pytest`:
  ```bash
  pytest -v
  ```

- **Ejecutar pruebas específicas:**  
  Ejecuta pruebas específicas para cada hack. Por ejemplo, para el primer hack:
  ```bash
  pytest -v test_server.py::test_hack_1
  ```

---

## Descripción de los Hacks
## 🏆 H-1 

```sh
CREATE AN ENDPOINT THAT RESPONDS IF THE REQUEST IS OF TYPE "GET"

ENDPOINT:("/users")
METHOD: "GET"
TYPE: JSON

output => {'payload':'success'}
```
<br/>


## 🏆 H-2
```sh
CREATE AN ENDPOINT THAT RESPONDS IF THE REQUEST IS OF TYPE "POST"

ENDPOINT:("/user")
METHOD: "POST"
TYPE: JSON

output => {'payload':'success'}
```
<br/>

## 🏆 H-3
```sh
CREATE AN ENDPOINT THAT RESPONDS IF THE REQUEST IS OF TYPE "DELETE"

ENDPOINT:("/user")
METHOD: "DELETE"
TYPE: JSON

output => {'payload':'success'}
```
<br/>

## 🏆 H-4
```sh
CREATE AN ENDPOINT THAT RESPONDS IF THE REQUEST IS OF TYPE "PUT"

ENDPOINT:("/user")
METHOD: "PUT"
TYPE: JSON

output => {'payload':'success'}

```
<br/>

## 🏆 H-5
```sh
CREATE AN ENDPOINT THAT RESPONDS IF THE REQUEST IS OF TYPE "GET"

ENDPOINT:("/api/v1/users")
METHOD: "GET"
TYPE: JSON

output => {'payload':[]}
```
<br/>


## 🏆 H-6
```sh
CREATE AN ENDPOINT THAT RESPONDS IF THE REQUEST IS OF TYPE "POST"

ENDPOINT:("/api/v1/user")
METHOD: "POST"
TYPE: JSON
INPUT: http://localhost:5000/api/v1/user?email=foo@foo.foo&name=fooziman

output =>  {
        'payload': {
            'email':email,
            'name':name,
        }
    }
```
<br/>

## 🏆 H-7
```sh
CREATE AN ENDPOINT THAT RESPONDS IF THE REQUEST IS OF TYPE "POST"

ENDPOINT:("/api/v1/user/add")
METHOD: "POST"
TYPE: JSON
INPUT: "request.form.get('key')"

output => {
        'payload': {
            'email':email,
            'name':name,
            'id':id,
        }
    }
```
<br/>

## 🏆 H-8
```sh
CREATE AN ENDPOINT THAT RESPONDS IF THE REQUEST IS OF TYPE "POST"

ENDPOINT:("/api/v1/user/create")
METHOD: "POST"
TYPE: JSON
INPUT: "request.get_json()"

output => {
        'payload': {
            'email':email,
            'name':name,
            'id':id,
        }
    }
```
<br/>
<br/>

## Adicional: Problemas para cerrar el servidor de Flask en segundo plano

Aquí tienes las opciones más comunes para detener, sin complicaciones, el servidor que ejecutaste en segundo plano con `flask run --debug &`.

---

### 1. **Usar el comando `jobs` para listar los procesos en segundo plano**
Al ejecutar el servidor con `&`, Flask se ejecuta como un **job** en segundo plano. Para detenerlo:

1. Lista los procesos en segundo plano con:
   ```bash
   jobs
   ```

   Esto mostrará una lista como esta:
   ```
   [1]+  Running   flask run --debug &
   ```

2. Detén el servidor utilizando el comando `kill` o `fg`:
   - Usa `fg` para traer el proceso al primer plano:
     ```bash
     fg %1
     ```
     (donde `1` es el número del job mostrado por `jobs`) y luego presiona `Ctrl + C` para detener el servidor.

   - O directamente termina el proceso con:
     ```bash
     kill %1
     ```

---

### 2. **Usar `ps` para encontrar el PID del proceso Flask**
Otra opción es buscar el **PID** (Process ID) del servidor Flask y detenerlo manualmente.

1. Encuentra el proceso Flask con:
   ```bash
   ps aux | grep flask
   ```

   Ejemplo de salida:
   ```
   user      12345  0.0  0.1  123456  7890 pts/0    S    10:00   0:00 flask run --debug
   ```

   Aquí, `12345` es el **PID** del proceso.

2. Detén el servidor Flask con:
   ```bash
   kill 12345
   ```

---

### 3. **Usar `pkill` para terminar directamente procesos Flask**
Si quieres evitar buscar el PID, puedes usar `pkill` para detener cualquier proceso Flask:

```bash
pkill -f "flask run"
```

Esto terminará todos los procesos relacionados con Flask.

---

### 4. **Atajo para detener Flask en el background**
Si sabes que Flask es el último comando ejecutado en segundo plano, puedes usar:

```bash
kill %%
```

El `%%` se refiere al último proceso en segundo plano ejecutado con `&`.

---

Con estos métodos puedes controlar fácilmente tu servidor Flask cuando está en segundo plano.
