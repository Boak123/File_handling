def most_frequent_word(filename):
    with open(filename, 'r') as file:
        file_contents = file.read().split()
        word_count = {}
        for w in file_contents:
            if w in word_count:
                word_count[w] += 1
            else:
                word_count[w] = 1

        max_word = None
        max_count = 0
        for w, count in word_count.items():
            if count > max_count:
                max_word = w
                max_count = count

    return max_word, max_count

