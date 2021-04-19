# -*- coding:utf-8 -*-

import itertools

words_num = "1234567890"
words_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
words_letter2 = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
words_letter3 = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,./;'[]\<>?:\"{}|`~!@#$%^&*()_+-="

# 没有好的字典，只有自己生成了，但是实在是太大了，效率好低

def createWifiPwd():
    r = itertools.product(words_letter2, repeat=8)
    fo = open("pwd.txt", "w")
    for i in r:
        fo.write("".join(i))
        fo.write("".join("\n"))
    fo.close()


def main():
    createWifiPwd()


if __name__ == '__main__':
    main()