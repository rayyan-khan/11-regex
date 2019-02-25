# regex homework 4, due 3/1 10:30 am rayyan khan

# Determine a regular expression which will match only
# on the indicated strings, or else will find the indicated
# matches. The form for the submission will be a command
# line script that takes a single integer as input from 71
# to 80, inclusive, and outputs the corresponding regular
# expression pattern, just as with the prior HW. The pattern
# is to be delimited by forward slashes and any options
# should immediately follow the final slash.

import sys

inp = int(sys.argv[1]) - 71 if len(sys.argv) > 1 else 0

answerArray = [ # 71. Find the shortest word where some letter occurs 4 times.
                '/\\b\w*(\w)\w*\\1\w*\\b/i',

                # 72. Find the shortest word where each vowel appears at least once.
                '/\\b\w*(\w)(\w*\\1\w*){2}\\b/i',

                # 73. Find the longest word containing exactly 3 vowels.
                '/^([01])([01]*\\1)*$/',

                # 74. Find the longest word where the first three letters form a
                # palindrome with the final three letters.
                '/(?=\\b\w{6}\\b)\w*cat\w*/i',

                # 75. Find the longest word with the longest contiguous block of
                # one letter.
                '/(?=\w*bri.*)(?=\w*i?ng)\\b\w{7,9}\\b/i',

                # 76. Find the longest word with the greatest number of a repeated
                # letter.
                '/(?!\w*cat.*)\\b\w{6}\\b/i',

                # 77. Find the longest word with the most number of adjacent pairs
                # of identical letters. Mississippi?
                '/(?!\w*(\w)\w*\\1\w*)\\b\w+/i',

                # 78. Find the longest word where each letter is repeated at least
                # once.
                '/(?!.*10011.*)^[01]*$/',

                # 79. Find the longest word where each letter is repeated exactly
                # one time.
                '/\w*([aeiou])(?!\\1)[aeiou]\w*/i',

                # 80. Find the longest word where no letter is repeated more than
                # once.
                '/(?![01]*(1.1)[01]*)^[01]*$/'
]

print(answerArray[inp])
