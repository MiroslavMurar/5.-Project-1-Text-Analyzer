'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''

]

users = {
    'bob' : '123',
    'ann' : 'pass123',
    'mike': 'password123',
    'liz' : 'pass123'
}


print ('Welcome to the app. Please log in:')
print (50*'-')

username = input('USERNAME: ')
password = input('PASSWORD: ')

print (50*'-')

if username in users.keys():
    if password == users[username]:
        print('We have 3 texts to be analyzed.')
        choice = None
        try:
            choice = int(input('Enter a number btw. 1 and 3 to select: '))
        except ValueError:
            print('Error when decoding the input. You have to insert a number!')
            exit()

        text = None
        try:
            text = TEXTS[choice - 1]
        except KeyError:
            print('There is no text', choice)
            exit()

        text_split = text.split()
        print('There are', len(text_split), 'words in the selected text.')

        capital_words = 0
        upper_words = 0
        lower_words = 0
        numeric_words = 0
        sum_numeric_words = 0


        for word in text_split:
            if word.istitle():
                capital_words += 1
            elif word.isupper():
                upper_words += 1
            elif word.islower():
                lower_words += 1
            elif word.isnumeric():
                numeric_words += 1
                sum_numeric_words += int(word)

        print('There are', capital_words, 'titlecase words')
        print('There are', upper_words, 'uppercase words')
        print('There are', lower_words, 'lowercase words')
        print('There are', numeric_words, 'numeric strings')

        all_freq = {}

        for i in text_split:
            if i[-1] in',.':
                i = i[:-1]
                if len(i) in all_freq:
                    all_freq[len(i)] += 1
                else:
                    all_freq[len(i)] = 1
            elif len(i) in all_freq:
                all_freq[len(i)] += 1
            else:
                all_freq[len(i)] = 1
        print(50 * '-')

        sorted_items = sorted(all_freq.items(), key = lambda item : item[0])

        for title, number in sorted_items:
            print(title, number * '*', number )

        print(50 * '-')
        print('If we summed all the numbers in this text we would get: ', sum_numeric_words)
        print(50 * '-')

    else:
        print('wrong login or password')
else:
    print('wrong login or password')



