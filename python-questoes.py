#   Impotação da Biblioteca
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()           

def soma_pares(lista):
    #   Soma os números pares em uma lista.
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c       
    return soma

def eh_palindromo(s):
    #   Verifica se uma string é um palíndromo.
    s = s.lower()
    s_invert = s[::-1]
    return s == s_invert

def maior_numero(lista):
    #   Encontra o maior número em uma lista.
    maior = lista[0]
    for c in lista:
        if c > maior:
            maior = c
            
    return maior

@app.get("/hello")
def read_hello():
    '''
    Endpoint para retornar a mensagem "Hello, World!"
    
    Exemplo de uso:
    /hello
    
    Resposta:
    {
        "message": "Hello, World!"
    }
    '''
    return {"message": "Hello, World!"}

@app.get("/soma_pares")
def read_soma_pares(numeros: list[int] = Query(...)):
    """
    Endpoint soma números pares de uma lista passada como query parameters.
    
    Parâmetros:
    - numeros (list[int]): Lista de inteiros passada como query parameters.

    Exemplo de uso:
    /soma_pares?numeros=1&numeros=2&numeros=3&numeros=4&numeros=5
    
    Resposta:
    {
        "soma": 6  # Soma dos números pares (2 + 4)
    }
    """
    if not numeros:
        raise HTTPException(status_code=400, detail="A lista de números não pode estar vazia")
    if not all(isinstance(num, int) for num in numeros):
        raise HTTPException(status_code=400, detail="Todos os valores na lista devem ser inteiros")
    
    return {"soma": soma_pares(numeros)}

@app.get("/eh_palindromo")
def read_eh_palindromo(texto: str):
    '''
    Endpoint para verificar se a string é um palíndromo.
    
    Parâmetros:
    - texto (str): Uma string com o possível palíndromo passada como query.
    
    Exemplo de uso:
    /eh_palindromo?texto=arara
    
    Resposta:
    {
        "palindromo": true  # ararA
    }
    '''
    return {"palindromo": eh_palindromo(texto)}

@app.get("/maior_numero")
def read_maior_numero(numeros: list[int] = Query(...)):
    '''
    Endpoint para encontrar o maior número em uma lista.
    
    Parâmetros:
    - numeros (list[int]): Lista de inteiros passada como query parameters.

    Exemplo de uso:
    /maior_numero?numeros=1&numeros=2&numeros=3&numeros=4&numeros=5
    
    Resposta:
    {
        "maior número": 5  # Maior dos números pasados (5 > 4 > 3 > 2 > 1)
    }
    '''
    if not numeros:
        raise HTTPException(status_code=422, detail="A Lista de números não pode estar vazia.")
    if len(numeros) < 2:
        raise HTTPException(status_code=422, detail="A Lista deve conter ao menos 2 números")
    return {"maior número": maior_numero(numeros)}

class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
         self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def top(self):
        if not self.items:
            return None
        return self.items[-1]
    
class Fila:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)
    
    
'''
    | Testes para verificar se todas as funções estão funcionando como deviam |
'''
#   Soma de Pares
assert soma_pares([1, 2, 3, 4, 5, 6]) == 12
assert soma_pares([10, 20, 30]) == 60
assert soma_pares([1, 3, 5]) == 0

#   Verificação de Palíndromos 
assert eh_palindromo("radar") == True
assert eh_palindromo("python") == False
assert eh_palindromo("arara") == True

#   Verificação de maior número
assert maior_numero([1, 2, 3, 4, 5, 6]) == 6
assert maior_numero([10, 20, 30]) == 30
assert maior_numero([-1, -3, -2, -5]) == -1

#   Verificação de stack
pilha = Pilha()
pilha.push(1)
pilha.push(2)
assert pilha.top() == 2
assert pilha.pop() == 2
assert pilha.top() == 1

#   Verificação de stack fila
fila = Fila()
fila.enqueue(1)
fila.enqueue(2)
assert fila.dequeue() == 1
assert fila.dequeue() == 2

#   Iniciando o servidor com uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
