"""
Vowel Counter: Count the number of vowels in a given string.
"""
sentence = "The quick brown fox jumps over the lazy dog"
vowels = "aeiou"
vowel_count = 0

for char in sentence:
    if char.lower() in vowels:
        vowel_count += 1

print(f"The number of vowels is: {vowel_count}")
