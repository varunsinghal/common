''' 
  Code works in Python 3
'''

#Unpacking the variables of unknown length
row = ('Python', 'R', 'PHP', 'SAS')
prime, secondary, *tertiary = row
print(tertiary)
#Output = ['PHP', 'SAS']

#Dealing with grouped variables in a tuple
row = ('Python', '2.7', ('2012','March','12'))
language, version, (*date_var, date) = row
print(date_var)
#Output = ['2012', 'March']
