spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
# 'black'
print(spam)
# {'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white')
# 'black'