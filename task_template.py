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

users = { 'bob' : '123',
          'ann' : 'pass123',
          'mike': 'password123',
          'liz' : 'pass123' }


print ('Welcome to the app. Please log in:')
print (50*'-')

username = input('USERNAME: ')
password = input('PASSWORD: ')

print (50*'-')

if username in users.keys():
    if password == users[username]:
        print('We have 3 texts to be analyzed.')
        try:
            int_text = int(input('Enter a number btw. 1 and 3 to select: '))
            text = TEXTS[int_text-1]

            text_split = text.split()
            print('There are ', len(text_split), ' words in the selected text.')

            capital_letters = 0
            upper_letters = 0
            lower_letters = 0
            numeric_letters = 0
            sum_numeric_letter = 0


            for word in text_split:
                if word.istitle():
                    capital_letters += 1

                elif word.isupper():
                    upper_letters += 1

                elif word.islower():
                    lower_letters += 1

                elif word.isnumeric():
                    numeric_letters += 1
                    sum_numeric_letter += int(word)

            print('There are ', len(text_split), ' words in the selected text.')
            print('There are ', capital_letters, ' titlecase words')
            print('There are ', upper_letters, ' uppercase words')
            print('There are ', lower_letters, ' lowercase words')
            print('There are ', numeric_letters, ' numeric strings')


            all_freq = {}

            for i in text_split:
                if i in all_freq:
                    all_freq[i] += 1
                else:
                    all_freq[i] = 1

            sorted_items = sorted(all_freq.items(), key = lambda item : item[1])
            count = 1
            for title, number in sorted_items:
                print(count, number * '*', number )

                count += 1

            print(50 * '-')

            print('If we summed all the numbers in this text we would get: ', sum_numeric_letter)

            print(50 * '-')

        except:
            print('Integer must be inserted ')

    else:
        print('wrong login or password')
else:
    print('wrong login or password')



