
# Contador de palabras: crear un script que lea el nombre de un archivo de texto y retorne 
# las 10 palabras más repetidas. 
# Debería usar listas, diccionarios, ciclos, funciones, try/except.
import re, string
from collections import Counter

def remove_punctuation ( text ):
  return re.sub('[%s]' % re.escape(string.punctuation), '', text)

file = input('Ingrese el nombre del archivo que desea abrir(file.txt): ')
numWords = input('Ingrese el número de palabras repetidas que desea obtener: ')
words = list()

try:
  file = open(file)
  numWords = int(numWords)
except (ValueError, FileNotFoundError) as error:
  print(error)
  exit()

for line in file:
  line = line.strip()
  newText = remove_punctuation(line)
  newText = newText.split(" ")
  for word in newText:
    if word != '' and word.isnumeric() == False:
      words.append(word)

mCommons = Counter(words).most_common(numWords)

i = 0
for c_word in mCommons:
  i+=1
  print((i),'.-palabra: ',c_word[0],'\n Veces en el texto: ', c_word[1])


