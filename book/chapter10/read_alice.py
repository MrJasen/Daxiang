#改变集成于方法，统计单词用，传入个书名即可
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as file_objcet:
            contens = file_objcet.read()
    except FileNotFoundError:
        msg = 'no found file'
        print(msg)
    else:
        # 开始计算有多少个单词，以空格为分隔符拆分多个部分，将这些部分存储到列表
        words = contens.split()
        num_words = len(words)
        print(num_words)
count_words('alice.txt')