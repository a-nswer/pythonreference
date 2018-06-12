dictionary = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
print(dictionary)

dictionary[7] = 'g'
print(dictionary, "<- new value added at 7")

del dictionary[7]
print(dictionary, "<- value at 7 deleted")

# loop through the above dictionary
for x, y in dictionary.items():
    print(x, y)


# don't mind this, just making an alphabet list (with a list comprehension)
alphabet = [chr(c).upper() for c in range(ord('a'), ord('z')+1)]

# dict comprehensions!
alphabetdict = {x+1: alphabet[x] for x in range(len(alphabet))}
print("\nAlphabet Dictionary", alphabetdict, sep="\n")

print("\nAlphabet Dictionary values", list(alphabetdict.values()), sep="\n")
print("\nAlphabet Dictionary keys", list(alphabetdict.keys()), sep="\n")
