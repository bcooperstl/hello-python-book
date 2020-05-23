#!/usr/bin/python3

test_dictionary = {'one':1,
                   'two':2,
                   'list':[1,2,3],
                   'dict': {'one':1, 'two':2},
                   }

print(test_dictionary['list'])
del test_dictionary['list']
test_dictionary['list']=[3,4,5]
print(test_dictionary['list'])
print(test_dictionary.keys())
print(test_dictionary.values())
print(test_dictionary.items())
