import random
import math

# Firi tou ngingī
onset = ['p', 'pʰ', 'ɓ', 't', 'tʰ', 'ᶑ', 'k', 'kʰ', 'q', 'qʰ', 'm', 'n', 'ɲ', 'ɳ', 'ŋ', 'ɸ', 'β', 'ɕ', 'ʑ', 'ʂ', 'ʐ', 'x', 't͡sʰ', 't͡ɕ', 't͡ɕʰ', 'ʈ͡ʂ', 'ʈ͡ʂʰ', 'r', 'ɾ', 'l', 'j', '*β̞', 'ɥ', 'ɰ']  # Fakatu'u Āraingingī
median = ['m', 'n', 'ɲ', 'ɳ', 'ŋ', 'ɾ', 'j', 'w', 'ɥ', 'ɰ']                     # Uaroto Āraingingī
vowel = ['...']                 # Fa'aingingī
coda = ['p̚', 't̚', 'ʈ̚', 'k̚', 'q̚', 'm', 'n', 'ɲ', 'ɳ', 'ŋ', 'ɻ', '', 'j', 'β̞']                 # Muri Āraingingī
tone = ['high', 'low', 'rising', 'falling']       # Papapa
extra1 = ['x1', 'x2']                             # Fafaru 1
extra2 = ['y1', 'y2']                             # Fafaru 2
extra3 = ['z1', 'z2']                             # Fafaru 3

# Firi Kakanu
patterns = ['CMVD', 'CMV', 'CVD', 'CV', 'VD']

# Kukupu ia fakatupu
num_words = 749

# Fakatupu Kukupu
def generate_word(pattern):
    word = ''
    phoneme_map = {'C': onset, 'V': vowel, 'M': median, 'T': tone, 'E1': extra1, 'E2': extra2, 'E3': extra3}
    for char in pattern:
        if char in phoneme_map:
            word += random.choice(phoneme_map[char])
        elif char == 'D':  # "D" mo kota teni aa na rea au ke.
            word += random.choice(coda)
    return word

# Pau Kukupu
def calculate_combinations():
    combinations = 0
    phoneme_map = {'C': len(onset), 'V': len(vowel), 'M': len(median), 'T': len(tone), 'E1': len(extra1), 'E2': len(extra2), 'E3': len(extra3)}
    for pattern in patterns:
        pattern_combinations = 1
        for char in pattern:
            if char in phoneme_map:
                pattern_combinations *= phoneme_map[char]
        combinations += pattern_combinations
    return combinations

# Tohi pau o kukupu
total_combinations = calculate_combinations()
print(f"Total possible combinations: {total_combinations}")

# Tohi Kukupu
generated_words = [generate_word(random.choice(patterns)) for _ in range(num_words)]
for word in generated_words:
    print(word)
