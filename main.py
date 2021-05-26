from morse_code import translator

initial_phrase = input("Introduce the phrase to convert:\n")

words = initial_phrase.upper().split(' ')

morse_code_result = []

# Loop for every word I have in the phrase
for word in words:
    morse_word = [translator[letter] if letter in translator else letter for letter in word ]
    morse_code_result.append(morse_word)

print(morse_code_result)