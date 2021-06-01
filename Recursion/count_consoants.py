vowels = "aeiou"

def iterative_count_consonants(input_str):
    consonant_count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowels and input_str[i].isalpha():
            consonant_count += 1
    return consonant_count

def recursive_count_consonants(input_str):
    # Base Case
    if input_str == "":
        return 0

    # Recursion
    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])
    
    

s = " Hey Jawad Saleem"
print("Iterative",iterative_count_consonants(s))

print("Recursive: ",recursive_count_consonants(s))