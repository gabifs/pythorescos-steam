# Para fazer o parsing do arquivo json
import json

class TrieNode():
    """
        Classe: Formato do nodo que faz parte da TRIE

        Param: TrieNode(char, value)
            char:char - letra que está contida no nodo
            value:any - value qualquer valor a ser inserido na trie
    """
    def __init__(self, char: str, value):
        self.char = char
        self.value = value
        self.children = []
        self.word_finished = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode('*', None)

    def _initialize_trie(self):
        """
            Inicializa a TRIE com a raiz TrieNode('*', None)
        """
        return TrieNode('*',None)

    def __setitem__(self, word: str, value):
        """
            Método de Trie: adiciona uma palavra na TRIE.

            Param: add(word, value)
                word:str - palavra que será inserida
                value:any - qualquer valor
        """
        word = self._standardize_string(word)
        node = self.root
        for char in word:
            found_in_child = False
            # Procura pelo caractere nos filhos do nodo atual
            for child in node.children:
                if child.char == char:
                    # Encontramos o caractere, incrementamos o contador pois
                    # agora temos mais uma palavra que tem o mesmo prefixo
                    # E vamos para o nodo filho onde econtramos o caractere de 'word'
                    node = child
                    found_in_child = True
                    break
            # Se não achamos o caractere de 'word' temos que adicioná-lo
            if not found_in_child:
                new_node = TrieNode(char,None)
                node.children.append(new_node)
                node = new_node

        # Quando terminarmos a palavra, marcamos o seu final
        node.value = value
        node.word_finished = True

    def __getitem__(self, prefix: str):
        """
            Método de Trie: checa se o prefixo existe em alguma das palavras.
            Se sim, retorna quantas palavras tem o mesmo prefixo.

            Param: find_prefix(prefix)
                prefix:str - prefixo que será buscado na TRIE
        """
        prefix = self._standardize_string(prefix)
        node = self.root

        if not self.root.children:
            return None
        for char in prefix:
            char_not_found = True

            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break

            if char_not_found:
                return None

        if node.word_finished:
            return node.value

    def _find_ids(self, node: TrieNode, ids_found=[]):
        """
            Método de Trie: encontra todos os ids relacionados a um prefixo

            Param: _find_ids(node, ids_found)
                node:TrieNode - nodo do qual iremos buscar todos os ids abaixo,
                é o último caractere do prefixo
                ids_found:array[int] - array com todos os ids encontrados a partir de node
        """
        for node in node.children:
            if node.word_finished:
                ids_found.append(node.value)
            else:
                self._find_ids(node, ids_found)

        return ids_found

    def _standardize_string(self, str):
        """
            Método de Trie: preprada o prefixo que será usado na pesquisa

            Param: _standardize_string(str)
                str:str - prefixo recebido
        """
        return str.lower().strip().replace(" ","")

if __name__ == "__main__":
    trie = Trie()
    trie['GTA'] =20
    trie['Assassins'] =[12, "add"]
    trie['GTA'] =32
    trie['GTC'] ="23"
    trie['G'] =3

    print(trie['GTA'])
    print(trie['GT'])
    print(trie['Assassins'])
    print(trie['G'])

    # for n in range(80000):
    #     trie[str(n)] = n
