import shelve

shelfFile = shelve.open('mydata')
#cats = ['Zophie', 'Pooka', 'Simon']
#shelfFile['cats'] = cats
#shelfFile.close()
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()
