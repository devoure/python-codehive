#! /usr/bin/python 
'''
This is a python program that provides random quizes
'''

import random

utdsquad = {
        'Bruno':'18',
        'Ronaldo':'7',
        'Rashy':'10',
        'Greenwood':'11',
        'Mata':'8',
        'DeGea':'1','Matic':'31', 'Sancho':'26', 'Martial':'11'}

for quiz in range(5):
    quizfile = open('quizfile{}'.format(quiz + 1), 'w')
    answerfile = open('answerfile{}'.format(quiz + 1), 'w')

    quizfile.write('First Name:\n\n Second Name:\n\n')
    quizfile.write('Guess the jersey numbers for the following players:\n\n')

    squad = list(utdsquad.keys())
    random.shuffle(squad)
    for quiz in range(9):
        correctanswer = utdsquad[squad[quiz]]
        wronganswer = list(utdsquad.values())
        del wronganswer[wronganswer.index(correctanswer)]
        wronganswer = random.sample(wronganswer, 3)
        answeroptions = wronganswer + [correctanswer]
        random.shuffle(answeroptions)
        quizfile.write('{}. What is the jersey number for {}\n'.format(quiz + 1,
            squad[quiz]))
        for i in range(4):
            quizfile.write('{}.{}\n'.format('ABCD'[i], answeroptions[i]))
        quizfile.write('\n')
        answerfile.write('{}.{}\n'.format(quiz + 1,
            'ABCD'[answeroptions.index(correctanswer)]))
quizfile.close()
answerfile.close()



