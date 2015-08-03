f = open("xxx.java", encoding='utf-8')
# 如果以wb开一个文件，py3+在write的时候要转bytes，encode
result = open("result.txt", "w")
line = f.readline()
while line:
    line = line.strip()
    if line.startswith('private'):
        properties = line.split(' ')
        theOne = properties[2].replace(';', '')
        for i in theOne:
            if i.isupper():
                theOne = theOne.replace(i, '_'+i.swapcase())

        print('@JsonProperty("'+theOne+'")')
        result.write('@JsonProperty("'+theOne+'")\n')
    line = f.readline()

f.close()
result.close()
