def count_words(str):
    only_alpha = ""
    for char in str:
        if char.isalpha() or char==' ':
            only_alpha += char
    words = only_alpha.split()
    print ({word:len(word) for word in words})