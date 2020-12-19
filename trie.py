# -*- coding:utf-8 -*-

class Trie(object):

    def __init__(self):
        self.root = {}
        self.end = -1

    def insert(self, word):
        cur_node = self.root
        for c in word:
            if not c in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node[self.end] = True

    def search(self, word):
        cur_node = self.root
        for c in word:
            if not c in cur_node:
                return False
            cur_node = cur_node[c]
        if not self.end in cur_node:
            return False
        return True

    def start_with(self, prefix):
        cur_node = self.root
        for c in prefix:
            if not c in cur_node:
                return False
            cur_node = cur_node[c]
        return True

    def get_start(self, prefix):
        def get_key(pre, pre_node):
            result = []
            if pre_node.get(self.end):
                result.append(pre)
            for key in pre_node.keys():
                if key != self.end:
                    result.extend(get_key(pre+key, pre_node.get(key)))
            return result
    
        if not self.start_with(prefix):
            return []
        else:
            node = self.root
            for p in prefix:
                node = node.get(p)
            else:
                return get_key(prefix, node)

if __name__ == "__main__":
    trie = Trie()
    trie.insert("Python")
    trie.insert("Python 算法")
    trie.insert("Python web")
    trie.insert("Python web 开发")
    trie.insert("Python web 开发 视频教程")
    trie.insert("Python 算法 源码")
    trie.insert("Perl 算法 源码")
    print(trie.search("Perl"))
    print(trie.search("Perl 算法 源码"))
    print((trie.get_start('P')))
    print((trie.get_start('Python web')))
    print((trie.get_start('Python 算')))
    print((trie.get_start('P')))
    print((trie.get_start('Python web')))
    print((trie.get_start('Python 算')))