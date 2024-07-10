def popular_words (text, words):
    text2=text.split(" ")
    result = {}
    for i in range (len(words)):
        result[words[i]] = 0
    for i in range(len(text2)):
        for j in range(len(words)):
            if text2[i].lower() == words[j].lower():
                result[words[j]] += 1
                break
    return result