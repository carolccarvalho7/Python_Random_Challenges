# ###############################################################################################
# RANDOM CHALLENGE
#
# Write a function named capital_indexes. 
# The function takes a single parameter, which is a string. 
# Your function should return a list of all the indexes in the string that have capital letters.
#
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
################################################################################################

# My Solution Number 1:
def capital_indexes(word):
    list_of_words_uppercase = []
    for count, letter in enumerate(word):
        if letter.isupper() == True:
            list_of_words_uppercase.append(count)
    return(list_of_words_uppercase)

upper_index = capital_indexes("CaRoLiNa")
print("Letras em maiúsculo nas posições:", upper_index)


# My Solution Number 2:
def capital_indexes_2(word):
    return[i for i in range(len(word)) if word[i].isupper() == True]

upper_index2 = capital_indexes_2("CaRoLiNa")
print("Letras em maiúsculo nas posições:", upper_index2)