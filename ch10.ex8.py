# Exercise 8, Chapter 10


""" Exercise 8
This exercise pertains to the so-called Birthday Paradox, which you can read
about at http://en.wikipedia.org/wiki/Birthday_paradox.
If there are 23 students in your class, what are the chances that two of you
have the same birthday? You can estimate this probability by generating random
samples of 23 birthdays and checking for matches. Hint: you can generate random
birthdays with the randint function in the random module."""


import random

def birthday_paradox_1(trials=1000):
    """"""
    totals = list()
    for trial in range(trials):
        total = 0
        bDayList = sorted([random.randint(0, 365) for _ in range(23)])
        for bday1, bday2 in zip(bDayList, bDayList[1:]):
            if bday1 == bday2:
                total += 1
        totals.append(total)
    avg = sum(totals) / len(totals)
    print('\nThe probability is {} percent ({}).'.format(avg * 100, 'fn 1'))

def birthday_paradox_2(trials=1000):
    """"""
    totals = list()
    for trial in range(trials):
        bDayList = [random.randint(0, 365) for _ in range(23)]
        totals.append(len(bDayList)-len(set(bDayList)))
    avg = sum(totals) / len(totals)
    print('\nThe probability is {} percent ({}).'.format(avg * 100, 'fn 2'))

def birthday_paradox_3(trials=1000):
    """Combine both methods and ensure the results are the same."""
    totals1 = list()
    totals2 = list()
    for trial in range(trials):
        total = 0
        bDayList = sorted([random.randint(0, 365) for _ in range(23)])
        for bday1, bday2 in zip(bDayList, bDayList[1:]):
            if bday1 == bday2:
                total += 1
        totals1.append(total)
        totals2.append(len(bDayList)-len(set(bDayList)))
    avg1 = sum(totals1) / len(totals1)
    avg2 = sum(totals2) / len(totals2)
    print('\nProbability: {}% ({}).'.format(avg1 * 100, 'count dups w/counter'))
    print('Probability: {}% ({}).'.format(avg2 * 100, 'count dups w/set'))
    if avg1 != avg2:
        same = ' not '
    else:
        same = ' '
    print('The results are{}the same when using counter and dups.'.format(same))


birthday_paradox_1()
birthday_paradox_2()
birthday_paradox_3()
