fw = open('sample.txt', 'w')
fw.write('test123\nlol123')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

