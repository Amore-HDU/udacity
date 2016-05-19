# udacity-优达学城

统计Python中的字数

问题

在 Python 中实施函数“count_words()”，该函数将字符串“s”和数字“n”用作输入，并返回“s”中“n”个出现频率最高的单词。返回值应该是一个元组列表 - 出现频率最高的“n”个单词及其相应的出现次数“[(, ), (, ), ...]”，按出现次数的降序排列。
您可以假设所有输入都是小写形式，并且不含标点符号或其他字符（只包含字母和单个分隔空格）。如果出现次数相同，则按字母顺序排列出现次数相同的单词。

例如：
print count_words("betty boughta bit of butter but the butter was bitter",3)

Output:

[('butter', 2), ('a', 1), ('betty', 1)]