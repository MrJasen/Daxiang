filename = 'alice.txt'
try:
    with open(filename,encoding='utf-8') as file_objcet:
        contens=file_objcet.read()
except FileNotFoundError:
    msg = 'no found file'
    print(msg)
else:
    #开始计算有多少个单词
    words=contens.split()
    num_words=len(words)
    print(num_words)