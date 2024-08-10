# Get in put from user

word = input('Input: ')
replace = ''

# Iterate through word to find vowels

for letter in word:
    if letter.lower() in ['a','e','i','o','u']:
        continue
    else:
        replace = replace + letter

print('Output: ',replace)




