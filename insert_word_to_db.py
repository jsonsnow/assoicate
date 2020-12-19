# _*_coding:utf-8_*_
import sqlite3
import parse_city

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
     
    def get_insert_sql(self, word, count):
        return "insert into assoicate (word, count) values('%s','%s')" % (word, count)

    def insert_associate_word(self, words):
        self.connect()
        for word_map in words:
            word = word_map[0]
            count = word_map[1]
            insert_sql = self.get_insert_sql(word, count)
            print(insert_sql)
            self.cursor.execute(insert_sql)
        self.conn.commit()
        self.close()


if __name__ == "__main__":
    db = db_manager()
    # words = parse_city.parase_city_word()
    # db.insert_associate_word(words)
    wsxc_words = parse_city.parase_wsxc_word()
    db.insert_associate_word(wsxc_words)
    # wsxc_words = parse_city.parse_food_word()
    # db.insert_associate_word(wsxc_words)
