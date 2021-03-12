#计算文本文件单词数的脚本

filename = input('please input the path of the file(including the file identity):')

try:
    with open(filename,encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry,the file {filename} does not exist.")
else:
    #计算单词数
    words = contents.split()
    # print(words)#--->测试
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
