print("This program provides word analytics on a provided text file.")
print("")

#Read the entire text as a string.

def readBook():
  f = open("dracula-short.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

draculaText = readBook()


#split the string into words and assign to a variable

words = draculaText.split()


#Find all of the individual words in the book and key the words into a dictionary called counter, and assign the words a
#base value of 1 if the word has never been seen before, otherwise increase the value by 1.

counter = {}
for word in words:
  word = word.lower()
  if word not in counter:
    counter[word] = 1
  else:
      counter[word] += 1




#Find the single word that shows up the most by iterating through dictionary with the
#counter.items() method, and hold the word with the largest value (a/k/a occurences)
#in the  MostCommonWord variable. Once the program meets a key with a value > largest;
#set that value as the next benchmark in largest, and assign the key as the mostCommonWord.

largest = 0
mostCommonWord = ""
counterTuple = counter.items()
for key, value in counterTuple:
  if value > largest:
    largest = value
    mostCommonWord = key

print("The most common word is", "'" + mostCommonWord.upper() + "'",  "at", largest, "occurences.")
print("")



#Find the words that are most common and print out their value.


print("The most common words (words with 50 or more occurances) are: ")
print("")
for key, value in counterTuple:
  if value >= 50:
    print("The word", "'" + key.upper() + "'", "appears", value, "times.")
print("")



#Count the number of words that are exactly four letters

fourLetterCount = []
for word in words:
  if len(word) == 4:
    fourLetterCount.append(word)
print("There were", len(fourLetterCount), "words that were four letters long.")
print("")



#Count the number of unique words by counting the length of the dictionary. Since a dictionary must
#have unique keys, the length of the dictionary is the number of unique words

print("There were", len(counter), "unique words.")
print("")


#The number of unique 4 letter words were:


fourLetterUnique = []
for word in words:
  if word not in fourLetterUnique:
    if len(word) == 4:
      fourLetterUnique.append(word)
print("There were", len(fourLetterUnique),  "unique words containing four letters.")
print("")
