# _*_coding:utf-8_*_
import sqlite3
import parse_city
import os

class db_manager(object):
    
    def __init__(self, db_path="input_word.db"):
        super().__init__()
        self.db_path = db_path

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()
     
    def get_insert_sql(self, word, count, prename):
        return "insert into assoicate (word, count, prename) values('%s', '%s', '%s')" % (word, count, prename)

    def create_associate_db(self, word_maps):
        conn = sqlite3.connect("input_word.db")
        cursor = conn.cursor()
        create_sql = '''create table IF NOT EXISTS assoicate(id INTEGER PRIMARY KEY,
        word TEXT NOT NULL,
        count INT,
        prename VARCHAR(1)
        )
        '''
        cursor.execute(create_sql)
        for word_map in word_maps:
            word = word_map[0]
            count = word_map[2]
            preword = word[0]
            insert_sql = self.get_insert_sql(word, count, preword)
            # print(insert_sql)
            if count.isdigit() and int(count) > 500:
                cursor.execute(insert_sql)

        cursor.execute('CREATE INDEX index_name ON assoicate(prename)')
        cursor.execute('CREATE INDEX index_count ON assoicate(count)')
        cursor.close()
        conn.commit()
        conn.close()

    def insert_associate_word(self, words):
        self.connect()
        for word_map in words:
            word = word_map[0]
            count = word_map[1]
            insert_sql = self.get_insert_sql(word, count, word[0])
            print(insert_sql)
            self.cursor.execute(insert_sql)
        self.conn.commit()
        self.close()

class associate_manager(object):
    def __init__(self, word_path="s_word.txt", db_path='input_word.db'):
        super().__init__()
        self.word_path = word_path
        self.db_path = db_path
    
    def read_words(self):
        inputs = open(self.word_path, 'r', encoding='utf-8')
        word_list = []
        for line in inputs:
            values = line.strip('\n').split('	')
            if len(values) > 1:
                word_list.append(values)
        return word_list

    def rm_db_file(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        else:
            print('no such file:%s'%self.db_path)


    def create_associate_db(self):
        self.rm_db_file()
        db = db_manager()
        words = self.read_words()
        db.create_associate_db(words)

    def insert_wsxc_word_to_file(self):
        city_words = parse_city.parase_wsxc_word()
        with open(self.word_path, 'a+', encoding='utf-8') as f:
            for city in city_words:
                city.insert(1, 'insert')
                print(city)
                value = '	'.join(city)
                f.write(value + '\n')

    def insert_city_word_to_file(self):
        city_words = parse_city.parase_city_word()
        with open(self.word_path, 'a+', encoding='utf-8') as f:
            for city in city_words:
                city.insert(1, 'insert')
                print(city)
                value = '	'.join(city)
                f.write(value + '\n')



# 追加文本到s_word.txt
# 追加的格式是  word	'insert'	count
#追加完成后如果需要创建数据库，调用create_associate_db，将通过s_word.txt创建数据库
if __name__ == "__main__":
    # db = db_manager()
    assoicate = associate_manager()
    assoicate.create_associate_db()
    # assoicate.insert_city_word_to_file()

    # words = parse_city.parase_city_word()
    # db.insert_associate_word(words)
    # wsxc_words = parse_city.parase_wsxc_word()
    # db.insert_associate_word(wsxc_words)
    # wsxc_words = parse_city.parse_food_word()
    # db.insert_associate_word(wsxc_words)
