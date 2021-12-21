'''Array setup'''

num_strings = ['15','100','55','42']
num_ints = [15,100,55,42]
num_floats = [12.5,34.6,666.666,2132.213]
num_list = [[1,2,3],[4,5,6],[7,8,9]]

'''Summary of num_strings'''

print('The variable num_strings is a: '+str(num_strings.__class__))
print('It contains the elements: '+str(num_strings))
print('The element '+str(num_strings[2])+' is '+str(num_strings[2].__class__))

'''Summary of num_ints'''

print('\nThe variable num_ints is a: '+str(num_ints.__class__))
print('It contains the elements: '+str(num_ints))
print('The element '+str(num_ints[2])+' is '+str(num_ints[2].__class__))

'''Summary of num_floats'''

print('\nThe variable num_floats is a: '+str(num_floats.__class__))
print('It contains the elements: '+str(num_floats))
print('The element '+str(num_floats[2])+' is '+str(num_floats[2].__class__))

'''Summary of num_list'''

print('\nThe variable num_list is a: '+str(num_list.__class__))
print('It contains the elements: '+str(num_list))
print('The element '+str(num_list[2])+' is '+str(num_list[2].__class__))

'''Sorting Arrays'''

print('\nNow sorting num_strings and num_ints')
num_strings.sort()
num_ints.sort()
print('Sorted num_strings: '+str(num_strings))
print('Sorted num_ints: '+str(num_ints))

print('Strings are sorted alphabetically while integers are sorted numerically!')