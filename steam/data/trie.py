# Para fazer o parsing do arquivo json
import json

class TrieNode():
    """
        Classe: Formato do nodo que faz parte da TRIE

        Param: TrieNode(char, id)
            char:char - letra que está contida no nodo
            id:int - id da palavra que será inserida (ao longo de vários nodos)
    """    
    def __init__(self, char: str, id):
        self.char = char
        self.id = id
        self.children = []
        self.word_finished = False
        self.counter = 1
    
class Trie(object):

    def __init__(self):
        self.root = TrieNode('*', None)

    def _initialize_trie(self):
        """
            Inicializa a TRIE com a raiz TrieNode('*', None)
        """
        return TrieNode('*',None)

    def add(self, word: str, id):
        """
            Método de Trie: adiciona uma palavra na TRIE. 

            Param: add(word, id)
                word:str - palavra que será inserida
                id:int - id da palavra
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
                    child.counter += 1
                    # E vamos para o nodo filho onde econtramos o caractere de 'word'
                    node = child
                    found_in_child = True
                    break
            # Se não achamos o caractere de 'word' temos que adicioná-lo
            if not found_in_child:
                new_node = TrieNode(char,id)
                node.children.append(new_node)
                node = new_node

        # Quando terminarmos a palavra, marcamos o seu final
        node.word_finished = True

    def find_prefix(self, prefix: str):
        """
            Método de Trie: checa se o prefixo existe em alguma das palavras. 
            Se sim, retorna quantas palavras tem o mesmo prefixo.

            Param: find_prefix(prefix)
                prefix:str - prefixo que será buscado na TRIE
        """
        prefix = self._standardize_string(prefix)
        node = self.root
        # Se a raiz não tiver filhos, retorna falso
        if not self.root.children:
            return [None]
        for char in prefix:
            char_not_found = True
            # Procura em todos os filhos do nodo atual
            for child in node.children:
                if child.char == char:
                    # Achamos o caractere que estávamos procurando
                    char_not_found = False
                    node = child
                    break
        
            if char_not_found:
                return [None]

        # Se o prefixo corresponde a somente uma palavra, retornamos somente um id
        # Senão, vamos procurar por todos os ids que estão relacioandos ao prefixo
        if node.word_finished:
            return [int(node.id)]
        else:    
            ids_found = []
            return self._find_ids(node, ids_found)

    def _find_ids(self, node: TrieNode, ids_found):
        """
            Método de Trie: encontra todos os ids relacionados a um prefixo

            Param: _find_ids(node, ids_found)
                node:TrieNode - nodo do qual iremos buscar todos os ids abaixo, 
                é o último caractere do prefixo
                ids_found:array[int] - array com todos os ids encontrados a partir de node
        """
        for node in node.children:
            if node.word_finished:
                ids_found.append(int(node.id))
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

    def add_from_file(self, filename):
        """
            Método de Trie: adiciona à vários registros retirados de um arquivo

            Param: add_from_file(filename):
                filename:str - string que contém o nome do arquivo. 
                O arquivo deve ser um JSON no seguinte formato
                [
                    <objeto_1>,
                    <objeto_2>,
                    ...
                    <objeto_n>
                ]
        """
        arq = open(filename).readlines()
        arq = arq[1:-1]

        for i,entry in enumerate(arq):
            # O último objeto do arquivo.json não tem vírgula no final da linha
            if i != len(arq)-1:
                entry = entry[0:-2]

            obj = json.loads(entry)
            # Formatando o nome para inserí-lo na TRIE
            name = self._standardize_string(obj["name"])
            id = int(obj["id"])
            self.add(name, id)

# TODO retornar lista com todas as palavras com prefixos correspondentes, não somente o primeiro resultado

trie = Trie()
trie.add_from_file('arquivo.json')
trie.add('GTA',20)

# Procurando pelos prefixos
print(trie.find_prefix('gt'))
print(trie.find_prefix('God'))
print(trie.find_prefix('godofwar20'))
print(trie.find_prefix('resi'))
print(trie.find_prefix('Resi'))
print(trie.find_prefix('Gran Turismo'))