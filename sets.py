# sets cant have duplicates unlike lists

groceries = {'cereal', 'milk', 'beer', 'beef', 'beer'}
groceriesdictonary = {'cereal': '100', 'beer': '250', 'wine': '260'}

print(groceries)
print(groceriesdictonary['cereal'])

if 'milk' in groceries:
    print('you already have milk')
else:
    print('213sadsaff')

for k, v in groceriesdictonary.items():
    print(k + " " + v)
