"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".

Example 1:

```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```

Example 2:

```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```

Example 3:

```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```

Notes:

- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""
def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str

    Output:
    bool
    """
    # Build a dictionary structure to lookup the index of each character
    # What do I know? The character
    # What do I want to lookup? Its index in the alphabet
    # So my dictionary has characters for keys, and alphabet indices for values
    alphabet = {letter: i for (i, letter) in enumerate(alpha_order)}

    # Starting at the beginning of the words list, look through and compare each word to the next...
    for i in range(len(words)-1): # for loop O(n)
        word1 = words[i] # O(1)
        word2 = words[i+1] # O(1)
        
        # Compare the two words letter by letter as needed:
        for j in range(min(len(word1), len(word2))):
            letter1 = word1[j]
            letter2 = word2[j]
            if letter1 != letter2:
                if alphabet[letter1] > alphabet[letter2]: # O(1) dictionary lookups
                    return False
                # Otherwise, these words are sorted! Move on to the next word
                break

            # Otherwise, keep going

        # If all the letters match, then compare by length
        if len(word1) > len(word2):
            return False

    # Looks like everything is good!
    return True

print(are_words_sorted(["lambda","school"], "hlabcdefgijkmnopqrstuvwxyz")) #--> True
print(are_words_sorted(["were","where","yellow"], "habcdefgijklmnopqrstuvwxyz")) #--> False
print(are_words_sorted(["lambda","lamb"], "abcdefghijklmnopqrstuvwxyz")) #--> False

# Time complexity: O(n)
# Space complexity: O(n) in general, O(1) because the prompt specified dictionary size n = 26