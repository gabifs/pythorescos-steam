class HashTable:
    def __init__(self, size):
        self._size = size
        self._dicionario = [-1] * size
        self._conteudo   = [None] * size
        self._used       = [False] * size

    def _hash(self, obj):
        string = str(obj)
        result = 0
        for letter, position in zip(string, range(1, len(string)+1)):
            result += position * ord(letter)
        return result % self._size

    def __setitem__(self, chave, dado):
        posicao = posicao_inicial = self._hash(chave)

        if self._dicionario[posicao] == -1:            # se estiver vazio
            self._dicionario[posicao] = chave          # coloca a chave
            self._conteudo[posicao] = dado                      # associa dado
            self._used[posicao] = True
            return posicao
        else:                                         # se estiver ocupado, tenta achar lugar usando linear probing
            first_pass = True
            while posicao != posicao_inicial or first_pass:
                first_pass = False
                posicao += 1
                if self._dicionario[posicao] == -1:
                    self._dicionario[posicao] = chave
                    self._conteudo[posicao] = dado
                    self._used[posicao] = True
                    return posicao

        if posicao == posicao_inicial:                  # se posicao igual à inicial é porque fez a volta e não achou
            return -1                                  # informa que deu problema (está cheio)
        else:
            return posicao                             # retorna posição onde colocou o dado

    def __getitem__(self, chave):
        posicao_inicial = posicao = self._hash(chave)
        first_pass = True

        # busca elemento usando linear probing:
        while self._dicionario[posicao] != chave and self._used and (posicao_inicial != posicao or first_pass):
            first_pass = False
            posicao += 1

        if self._dicionario[posicao] == chave:
            return self._conteudo[posicao]
        else:
            return None # se chegou aqui é porque não existe a chave

    def __len__(self):
        return self._size

    def pop(self, chave):
        posicao_inicial = posicao = self._hash(chave)
        first_pass = True

        # busca elemento usando linear probing:
        while self._dicionario[posicao] != chave and self._used and (posicao_inicial != posicao or first_pass):
            first_pass = False
            posicao += 1

        if self._dicionario[posicao] == chave:
            self._dicionario[posicao] = -1
            self._conteudo[posicao] = None
            return posicao
        else:
            return None # se chegou aqui é porque não existe a chave
        return -1

    def keys(self):
        return [key for key in self._dicionario if key != -1]

    def values(self):
        return [value for value in self._conteudo if value != None]

    def print(self):
        for indice in range(0, self._size):
            print(f"({indice:03d})[{self._dicionario[indice]}] = {str(self._conteudo[indice]):15s} ({self._used[indice]})")

if __name__ == "__main__":
    table = HashTable(23)
    table[[2,3]] = 8
    table["foo"] = "bar"

    print(table.values())
