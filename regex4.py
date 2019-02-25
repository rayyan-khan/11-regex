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
                '"/(?=\\b\w*(\w)(\w*\\1\w*){3}\\b)\w{,6}$/m"',

                # 72. Find the shortest word where each vowel appears at least once.
                '',

                # 73. Find the longest word containing exactly 3 vowels.
                '/(?=\\b(\w*[aieou]\w*){3}\\b)\w{,3}$/m',

                # 74. Find the longest word where the first three letters form a
                # palindrome with the final three letters.
                '',

                # 75. Find the longest word with the longest contiguous block of
                # one letter.
                '/(?=\\b\w*(\w)\w*\\1{3,}\w*\\b)\w*$/m',

                # 76. Find the longest word with the greatest number of a repeated
                # letters.
                '',

                # 77. Find the longest word with the most number of adjacent pairs
                # of identical letters. Mississippi?
                '',

                # 78. Find the longest word where each letter is repeated at least
                # once.
                '',

                # 79. Find the longest word where each letter is repeated exactly
                # one time.
                '',

                # 80. Find the longest word where no letter is repeated more than
                # once.
                ''
]

print(answerArray[inp])
