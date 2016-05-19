# udacity-优达学城
-----
#统计Python中的字数
										                            
##问题：

>在 Python 中实施函数“count_words()”，该函数将字符串“s”和数字“n”用作输入，并返回“s”中“n”个出现频率最高的单词。返回值应该是一个元组列表 - 出现频率最高的“n”个单词及其相应的出现次数“[(, ), (, ), ...]”，按出现次数的降序排列。
您可以假设所有输入都是小写形式，并且不含标点符号或其他字符（只包含字母和单个分隔空格）。如果出现次数相同，则按字母顺序排列出现次数相同的单词。

例如：
print count_words("betty boughta bit of butter but the butter was bitter",3)

Output:

[('butter', 2), ('a', 1), ('betty', 1)]

##解题思路：
>- 由于s是个字符串，所以应该先把字符串split变成一个list，并且应该按照首字母利用sorted排好序！！！！！（这步非常重要，这步解决了如果出现次数相同，则按字母顺序排列出现次数相同的单词）。
>- 考虑到输出的时候要同时输出word和出现的次数，所以要用dictionary，但是单单dictionary是不够的，要用OrderedDict才可以，这样才能保证生成的dictionary是按照之前排好的顺序。
>- 利用for将words和出现的次数填入dictionary中，此时dictionary的顺序是按照key中的word的首字母顺序排序的。
>- 接着要做的就是将dictionary按照value排序（第一排序条件是value，第二排序条件是key中word的首字母）
>- output的格式是[('butter', 2), ('a', 1), ('betty', 1)]，所以新建一个top_n的list即可，并且用for以及append根据传入的n填充list即可。


                                                                                         毛礼建
                                                                                   2016年5月19号
