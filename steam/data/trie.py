from typing import Tuple
import json

class TrieNode(object):
    
    def __init__(self, char: str, id):
        self.char = char
        self.id = id
        self.children = []
        self.word_finished = False
        self.counter = 1
    

def add(root, word: str, id):
  """Adicionando uma palavra da Trie"""
  node = root
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


def find_prefix(root, prefix: str) -> Tuple[bool, int, int]:
    """
    1. Checa se o prefixo existe em alguma das palavras
    2. Se sim, retorna quantas palavras tem o mesmo prefixo
    """
    node = root
    # Se a raiz não tiver filhos, retorna falso
    if not root.children:
        return False, 0
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
            return False, 0
    # Se chegamos aqui, então encontramos o prefixo. O retorno indica 
    # se que o encontramos e quantas palavras tem esse prefixo
    return True, node.counter, int(node.id)

root = TrieNode('*',None)
arq = open("arquivo.json").readlines()
arq = arq[1:-1]

for i,entry in enumerate(arq):
    # O último objeto do arquivo.json não tem vírgula no final da linha
    if i != len(arq)-1:
        entry = entry[0:-2]

    obj = json.loads(entry)
    # Formatando o nome para inserí-lo na TRIE
    name = obj["name"].lower().strip().replace(" ","")
    add(root, name, obj["id"])

# Procurando pelos prefixos
print(find_prefix(root, 'God'))
print(find_prefix(root, 'godofwar20'))
print(find_prefix(root, 'resi'))
print(find_prefix(root, 'Resi'))
print(find_prefix(root, 'gr'))