# Teste em Python para Desenvolvedor Python Júnior

Um simples teste criar um programa capaz de resolver algumas questões matemáticas e de lógica.

## 💻 Começando

Esta API fornece endpoints para calcular a soma de números pares, verificar palíndromos e encontrar o maior número em uma lista.

### 📋 Pré-requisitos
* Python 3.7+
* FastAPI
* uvicorn
* Curl (opcional, todos os comandos funcionan no navegador)
* Git

### 🔧 Instalação

Clone esse repositório com a ferramenta GIT:

```
git clone https://github.com/Nyuruy/Test-Python/blob/main/python-questoes.py
```

## ⚙️ Executando a API

1. **Abra o CMD:** Vá até a pasta onde seu arquivo `python-questoes.py` está localizado. Para isso, use o comando `cd` mo CMD. Por exemplo, se seu arquivo está em `C:\Users\SeuUsuário\Documents\python-questoes`, digite: 
~~~Bash
cd C:\Users\SeuUsuário\Documents\python-questoes
~~~

2. **Execute o comando:** Digite o comando abaixo no CMD:
~~~Bash
uvicorn python-questoes:app --reload
~~~

3. **Acesse a API:** O servidor irá iniciar e você poderá acessar sua API no endereço `https://127.0.0.1:8000/`. Você pode testar os endpoints, como `/hello`, `/soma_pares`, `/eh_palindromo`, e `/maior_numero`, adicionando parâmetros na URL.

**Exemplo:**
~~~Bash
C:\Users\SeuUsuário\Documents\python-questoes> uvicorn python-questoes:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using statreload
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
~~~

### 🔨 Endpoints

---

#### 👋 `/hello`
Retorna a mensagem "Hello, World!".

**Exemplo Via CMD:**
~~~Bash
curl https://127.0.0.1:8000/hello
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

**Exemplo Via CMD:**
~~~Bash
curl https://127.0.0.1:8000/maior_numero?numeros=1&numeros=2&numeros=3&numeros=4&numeros=5
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

**Exemplo Via CMD:**
~~~Bash
curl https://127.0.0.1:8000/eh_palindromo?texto=arara
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

**Exemplo Via CMD:**
~~~Bash
curl https://127.0.0.1:8000/maior_numero?numeros=1&numeros=2&numeros=3&numeros=4&numeros=5
~~~

**Resposta:**
~~~Json
{
    "maior número": 5
}
~~~


## 🛠️ Construído com

* [FastAPI](https://fastapi.tiangolo.com) - Framework Python para construir APIs RESTful.
* [uvicorn](https://www.uvicorn.org) - Servidor ASGI para rodar aplicações FastAPI.
