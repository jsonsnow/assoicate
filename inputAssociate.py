# _*_coding:utf-8_*_
import jieba
import re
import sqlite3
import datetime

def read_words():
    inputs = open('s_word.txt', 'r', encoding='utf-8')
    wordList = []
    for line in inputs:
       values = line.strip('\n').split('	')
       if len(values) > 1:
           wordList.append(values)
    return wordList

def get_insert_sql(word, count, preword):
    return "insert into assoicate (word, count, prename) values('%s','%s','%s')" % (word, count, preword)

def get_select_sql(word):
    sql = "select * from assoicate where word like '%{name}_%' and count > 100 order by count desc".format(name=word)
    print(sql)
    return sql

def create_associatedb():
    conn = sqlite3.connect("input_word.db")
    cursor = conn.cursor()
    create_sql = '''create table IF NOT EXISTS assoicate(id INTEGER PRIMARY KEY,
    word TEXT NOT NULL,
    count INT,
    prename VARCHAR(1)
    )
    '''
    cursor.execute(create_sql)
    for word_map in read_words():
        word = word_map[0]
        count = word_map[2]
        preword = word[0]
        # print(preword)
        insert_sql = get_insert_sql(word, count, preword)
        # print(insert_sql)
        if count.isdigit() and int(count) > 500:
            cursor.execute(insert_sql)
        # if int(count) >= 1:


    cursor.execute('CREATE INDEX index_name ON assoicate(prename)')
    cursor.execute('CREATE INDEX index_count ON assoicate(count)')
    cursor.close()
    conn.commit()
    conn.close()

# def insert_app_word():
#     conn = sqlite3.connect('input_word.db')
#     cursor = conn.cursor()
#     create_sql = '''create table IF NOT EXISTS assoicate(id INTEGER PRIMARY KEY,
#     word TEXT NOT NULL UNIQUE,
#     count INT
#     )
#     '''
#     cursor.execute(create_sql)
#     for word_map in read_words():
#         word = word_map[0]
#         count = word_map[2]
#         insert_sql = get_insert_sql(word, count)
#         # print(insert_sql)

#         cursor.execute(insert_sql)
#         # if int(count) >= 1:


#     # cursor.execute('CREATE INDEX index_word ON assoicate(word)')
#     cursor.execute('CREATE INDEX index_count ON assoicate(count)')
#     cursor.close()
#     conn.commit()
#     conn.close()

def get_jieba_split_word(word):
    input_words = jieba.cut(word)
    words = []
    for word in input_words:
        words.append(word)
    return words

def get_input_last_word(word):
    words = get_jieba_split_word(word)
    return words[-1]

def get_a_assoicate(associate, words):
    # print(words)
    for index, word in enumerate(words):
        # print("for associate %s in word %s" % (associate, word))
        regex = r"%s(.*)" % associate
        # print(regex)
        search_obj = re.search(regex, word)
        if search_obj:
            res = (search_obj.group(1))
            if res == "":
                return words[index + 1]
            return res
        else:
            print(word)

def get_assoicate_list(word):
    starttime = datetime.datetime.now()
    for_associate = get_input_last_word(word)
    print(for_associate)
    conn = sqlite3.connect('input_word.db')
    cursor = conn.cursor()
    cursor.execute(get_select_sql(for_associate))
    values = cursor.fetchall()
    res = []
    for row in values:
        assoicate_word = row[1]
        jieba_words = get_jieba_split_word(assoicate_word)
        value = get_a_assoicate(for_associate, jieba_words)
        if value:
            res.append(value)
    cursor.close()
    conn.close()
    print(res)
    endtime = datetime.datetime.now()
    print((endtime - starttime).microseconds/1000)
    return res

def get_assoicate():
    word = input('输入词汇：')
    while len(get_assoicate_list(word)):
        othter = input('选择词汇：')
        word = othter


if __name__ == '__main__':
    create_associatedb()
    # starttime = datetime.datetime.now()
    # get_assoicate()
    # endtime = datetime.datetime.now()
    # print((endtime - starttime).seconds)
