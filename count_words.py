"""Count words."""
from string import *
import collections
def count_words(s, n):
    words = sorted(split(s))
    length = len(words)
    d  = collections.OrderedDict()
    top_n = []
    for word in words:
        d[word] = words.count(word)
    dic = sorted(d.iteritems(),key = lambda c: c[1],reverse = True)
    for i in range(n):
        top_n.append(dic[i])
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
