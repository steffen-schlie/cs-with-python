# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    return input_text.split(' ')


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    if type(input_iterable) == str:
        letter_frequencies = {}
        for elem in set(list(input_iterable)):
            count = 0
            for letter in input_iterable:
                if letter == elem:
                    count += 1
            letter_frequencies[elem] = count
        return letter_frequencies
    else:
        word_frequencies = {}
        for elem in set(input_iterable):
            count = 0
            for word in input_iterable:
                if word == elem:
                    count += 1
            word_frequencies[elem] = count
        return word_frequencies
            


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    return get_frequencies(word)


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    # get lists of words from both dictionaries
    words_dict1 = list(freq_dict1.keys())
    words_dict2 = list(freq_dict2.keys())

    # create list of unique words
    unique_words = list(set(words_dict1+words_dict2))

    # loop through list of unqiue words, get frequencies from dicts
    # and set frequ to zero if not found in dict
    # keep track of total sum of delta and sigma scores
    delta_score = 0
    sigma_score = 0
    for word in unique_words:
        if word in words_dict1 and word in words_dict2:
            delta_score += abs(freq_dict1[word]-freq_dict2[word])
            sigma_score += freq_dict1[word]+freq_dict2[word]
        elif word in words_dict1 and word not in words_dict2:
            delta_score += freq_dict1[word]
            sigma_score += freq_dict1[word]
        else:
            delta_score += freq_dict2[word]
            sigma_score += freq_dict2[word]
    return round(1-delta_score/sigma_score, 2)


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    # get lists of words from both dictionaries
    words_dict1 = list(freq_dict1.keys())
    words_dict2 = list(freq_dict2.keys())

    # create list of unique words
    unique_words = list(set(words_dict1+words_dict2))

    current_highest = []
    current_max_count = 0

    for word in unique_words:
        if word in words_dict1 and word in words_dict2:
            if freq_dict1[word] + freq_dict2[word] > current_max_count:
                current_highest.clear()
                current_highest.append(word)
                current_max_count = freq_dict1[word] + freq_dict2[word]
            elif freq_dict1[word] + freq_dict2[word] == current_max_count:
                current_highest.append(word)
        elif word in words_dict1 and word not in words_dict2:
            if freq_dict1[word] > current_max_count:
                current_highest.clear()
                current_highest.append(word)
                current_max_count = freq_dict1[word]
            elif freq_dict1[word] == current_max_count:
                current_highest.append(word)
        else:
            if freq_dict2[word] > current_max_count:
                current_highest.clear()
                current_highest.append(word)
                current_max_count = freq_dict2[word]
            elif freq_dict2[word] == current_max_count:
                current_highest.append(word)
    return current_highest

            


### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    text_file = load_file(file_path)
    words_list = text_to_list(text_file)
    total_nr_words = len(words_list)

    # get frequencies of word
    freq_dict = get_frequencies(words_list)
    tf_dict = {}
    for word in freq_dict.keys():
        tf_dict[word] = freq_dict[word] / total_nr_words
    return tf_dict

def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    total_nr_files = len(file_paths)

    # now for every file we need the frequency dictionary
    list_of_words_lists = []
    total_words_list = []
    for i in range(len(file_paths)):
        loaded_text_file = load_file(file_paths[i])
        words_in_text = text_to_list(loaded_text_file)
        list_of_words_lists.append(words_in_text)
        total_words_list += words_in_text

    # merge the lists of all files to one list containing of all words that occur somewhere
    unique_words_list = list(set(total_words_list))

    # iterate through list of unqiue words and create dictionary with idf scores
    idf_dict = {}
    for word in unique_words_list:
        count = 0
        for elem in list_of_words_lists:
            if word in elem:
                count += 1
        idf_dict[word] = math.log10(total_nr_files / count)
    return idf_dict



def get_tfidf(tf_file_path, idf_file_paths):
    """
    Args:
        tf_file_path: name of file in the form of a string (used to calculate TF)
        idf_file_paths: list of names of files, where each file name is a string
        (used to calculate IDF)
    Returns:
        a sorted list of tuples (in increasing TF-IDF score), where each tuple is
        of the form (word, TF-IDF). In case of words with the same TF-IDF, the
        words should be sorted in increasing alphabetical order.

    * TF-IDF(i) = TF(i) * IDF(i)
    """
    score_list = []
    tf_scores = get_tf(tf_file_path)
    idf_scores = get_idf(idf_file_paths)

    for word in tf_scores.keys():
        score_list.append((word, tf_scores[word]*idf_scores[word]))
    return score_list


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    test_directory = "problem-sets/ps3/tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    print(world)      # should print ['hello', 'world', 'hello']
    print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    test_directory = "problem-sets/ps3/tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    freq1 = get_letter_frequencies('hello')
    freq2 = get_letter_frequencies('that')
    print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    test_directory = "problem-sets/ps3/tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    word1_freq = get_letter_frequencies('toes')
    word2_freq = get_letter_frequencies('that')
    word3_freq = get_frequencies('nah')
    word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    print(word_similarity1)       # should print 1.0
    print(word_similarity2)       # should print 0.25
    print(word_similarity3)       # should print 0.0
    print(word_similarity4)       # should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    tf_text_file = 'problem-sets/ps3/tests/student_tests/hello_world.txt'
    idf_text_files = ['problem-sets/ps3/tests/student_tests/hello_world.txt', 'problem-sets/ps3/tests/student_tests/hello_friends.txt']
    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)
    tf_idf = get_tfidf(tf_text_file, idf_text_files)
    print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]