# Teste em Python para Desenvolvedor Python Júnior

Um simples teste criar um programa capaz de resolver algumas questões matemáticas e de lógica.

## 💻 Começando

Esta API fornece endpoints para calcular a soma de números pares, verificar palíndromos e encontrar o maior número em uma lista.

### 📋 Pré-requisitos
* Python 3.7+
* FastAPI
* uvicorn
* Git

### 🔧 Instalação

1. **Clone o repositório:**
   Use o comando `git` para clonar o repositório onde está o projeto:
~~~bash
git clone https://github.com/Nyuruy/Test-Python.git
~~~

2. **Navegue até o diretório do projeto:**
   Entre no diretório onde está o repositório clonado:
~~~bash
cd Test-Python
~~~

3. **Instale as dependências:** Instale as dependências necessárias usando `pip`:
~~~bash
pip install fastapi uvicorn
~~~

## ⚙️ Executando a API

1. **Abra o CMD:** Vá até a pasta onde seu arquivo `python-questoes.py` está localizado. Para isso, use o comando `cd` no CMD. Por exemplo, se seu arquivo está em `C:\Users\SeuUsuário\Documents\Test-Python`, digite: 
~~~Bash
cd C:\Users\SeuUsuário\Documents\Test-Python
~~~

2. **Execute o comando:** Digite o comando abaixo no CMD:
~~~Python
python -m uvicorn python-questoes:app --reload
~~~

3. **Acesse a API:** O servidor irá iniciar e você poderá acessar sua API no endereço `http://127.0.0.1:8000/`. Você pode testar os endpoints, como `/hello`, `/soma_pares`, `/eh_palindromo`, e `/maior_numero`, adicionando parâmetros na URL.

**Exemplo:**
~~~Bash
C:\Users\SeuUsuário\Documents\Test-Python> python -m uvicorn python-questoes:app --reload
←[32mINFO←[0m:     Will watch for changes in these directories: ['C:\\Users\\SeuUsuário\\Documents\\Test-Python']
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://127.0.0.1:8000←[0m (Press CTRL+C to quit)
←[32mINFO←[0m:     Started reloader process [←[36m←[1m61608←[0m] using ←[36m←[1mWatchFiles←[0m
←[32mINFO←[0m:     Started server process [←[36m64328←[0m]
←[32mINFO←[0m:     Waiting for application startup.
←[32mINFO←[0m:     Application startup complete.
~~~

### 🔨 Endpoints

---

#### 👋 `/hello`
Retorna a mensagem "Hello, World!".

**Exemplo:**
~~~http
http://127.0.0.1:8000/hello
~~~

**Resposta:**
~~~Json
{
    "message": "Hello, World!"
}
~~~

---

#### ➕ `/soma_pares`
Calcula a soma dos números pares em uma lista.

**Parâmetros:**
* ´numeros´: Lista de números inteiros separados por vírgula (ex: `1,2,3,4,5`)

**Exemplo:**
~~~http
http://127.0.0.1:8000/soma_pares?numeros=1&numeros=2&numeros=3&numeros=4&numeros=5
~~~

**Resposta:**
~~~Json
{
    "soma": 6
}
~~~

---

#### ⬅️ `/eh_palindromo`
Verifica se uma string é um palíndromo

**Parâmetros:**
* `texto`:String a ser verificada (ex: `arara`).

**Exemplo:**
~~~http
http://127.0.0.1:8000/eh_palindromo?texto=arara
~~~

**Resposta:**
~~~Json
{
    "palindromo": true
}
~~~

---

#### 🔝 `/maior_numero`
Encontra o maior número em uma lista.

**Parâmetro:**
* `numeros`: Lista de números inteiros separados por vírgula (ex: `1,2,3,4,5`).

**Exemplo:**
~~~http
http://127.0.0.1:8000/maior_numero?numeros=1&numeros=2&numeros=3&numeros=4&numeros=5
~~~

**Resposta:**
~~~Json
{
    "maior número":5
}
~~~


## 🛠️ Construído com

* [FastAPI](https://fastapi.tiangolo.com) - Framework Python para construir APIs RESTful.
* [uvicorn](https://www.uvicorn.org) - Servidor ASGI para rodar aplicações FastAPI.
