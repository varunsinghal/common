#Definition of args and kwargs

def f(*args, **kwargs):
  print args
  print kwargs
  
f('php','python', 3.4, name='varun', age=21, blog='https://web4code.blogspot.com')

'''
Output:
('php', 3.4)
{'name':'varun', 'age':21, 'blog':'https://web4code.blogspot.com'}

Caution: Args and kwargs should maintain a sequence as in the definition.
'''
