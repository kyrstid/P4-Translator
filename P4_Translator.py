
# definitely just copied & pasted this from the example provided
intro = 'Welcome to the English to Spanish Translator'
text_width = len(intro)
screen_width = 80
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
print(' ' * left_margin + '*' * text_width)
print(' ' * left_margin + intro)
print(' ' * left_margin + '*' * text_width)
print('  ')


keys = ['1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'10',
'11',
'12',
'13',
'14',
'15',
'16',
'17',
'18',
'19',
'20',
'21',
'22',
'23',
'24',
'25',
'26',
'27',
'28']

english_phrase = ['Good morning.',
'Good afternoon.',
'Good evening. (greeting)',
'Hello, my name is John.',
'What is your name?',
'How are you?',
'I am fine.',
'Nice to meet you.',
'Goodbye.',
'See you later.',
'I am lost. Where is the restroom?',
'Excuse me.',
'Please.',
'Thank you.',
'Bless you.',
'You are welcome (it was nothing).',
'How much does it cost?',
'How many are there?',
'There are many.',
'Do you want to buy this?',
'What time is it?',
'How do you say maybe in Spanish?',
'Yes.',
'No.',
'I do not understand.',
'Would you speak slower, please.',
'Who?',
'Why?',]

spanish_phrase = ['Buenos días.',
'Buenas tardes.',
'Buenas noches.',
'Hola, me llamo Juan.',
'¿Cómo se llama usted?',
'¿Cómo está usted?',
'Estoy bien.',
'Mucho gusto.',
'Adiós.',
'Hasta luego.',
'Estoy perdido. ¿Dónde está el baño?',
'Con permiso. OR Perdóname',
'Por favor.',
'Gracías.',
'Salud.',
'De nada.',
'¿Cuánto cuesta?',
'¿Cuántos hay?',
'Hay muchos.',
'¿Quiere comprarlo usted?',
'¿Qué hora es?',
'¿Cómo se dice maybe en Español?',
'Sí.',
'No.',
'Yo no comprendo.',
'Por favor, habla mas despacio.',
'¿Quièn?',
'¿Por què?',]

phrase_list = dict(zip(keys, english_phrase))
phrase_list2 = dict(zip(keys, spanish_phrase))

print(phrase_list)
print('  ')

print('Hello!  This program translates common English phrases into Spanish.')
print('Please review the list of English phrases above then,')
    
# have user choose a # from a numbered list of provided English phrases

number = input('Enter a number to see the translation of that phrase: ')
print('  ')
print("You chose number " + number + ".")

if number in phrase_list:
    print("The Enlish phrase for number " + number + " is: " + '"' + phrase_list.get(number, 1) + '"')
    print('The Spanish translation for this phrase is: ' + '"' + phrase_list2.get(number, 1) + '"')
else: print('I am sorry, your number choice was not recognized.')

