def single_root_words(root_word, *other_words): # обязат. слово в root_word, неогр. послед-ть в *other_words
    same_words = [] # пустой список для пополнения

    for word in other_words:
        if root_word.lower() in word.lower(): #  содержит ли слово word подстроку root_word (без учета регистра)
            same_words.append(word) # если да - добавить в список
        elif word.lower() in root_word.lower(): #  содержит ли root_word слово word (без учета регистра)
            same_words.append(word) # если да - добавить в список
    return same_words # после завершения цикла возврат списока same_words

# Вызовы функции и вывод результатов
result1 = single_root_words('Умозаключение', 'Ум', 'зАкЛюЧеНиЕ', 'клюЧ', 'учение')
result2 = single_root_words('SaD', 'sadnesS', 'SaDdEn', 'SADDLE', 'sacred', 'saddle horse')
print(result1)
print(result2)