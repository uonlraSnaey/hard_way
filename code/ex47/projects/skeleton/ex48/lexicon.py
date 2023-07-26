# lexicon.py

def scan(sentence):
    pass

def scan(sentence):
    # 分割句子成单词
    words = sentence.split()
    # 创建结果列表
    result = []
    # 遍历单词，识别类型并添加到结果列表中
    for word in words:
        # 这里的伪代码示例只包括方向词汇的识别，其它类型需要类似的逻辑
        if word == "north":
            result.append(('direction', 'north'))
    return result

# lexicon.py

def scan(sentence):
    # 分割句子成单词
    words = sentence.split()
    # 创建结果列表
    result = []
    # 遍历单词，识别类型并添加到结果列表中
    for word in words:
        if word == "north":
            result.append(('direction', 'north'))
        elif word == "south":
            result.append(('direction', 'south'))
        elif word == "east":
            result.append(('direction', 'east'))
        elif word == "west":
            result.append(('direction', 'west'))
        else:
            # 无法识别的单词作为错误处理
            result.append(('error', word))
    return result
