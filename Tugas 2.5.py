import itertools, random

deck=list(itertools.product(range(1,14),['kriting','hati','wajik','sekop']))

random.shuffle(deck)
print('kamu mendapat: ')
for i in range(5):
    print(deck[i][o],'dari',deck[i][1])
