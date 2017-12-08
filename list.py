names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
num = ['11', '12', '13', '4', '5', '6', '7', '8', '9', '10']

result = {}
print('names =' + str(names))
print('num = ' + str(num))

for i, val in enumerate(names):
    print (i)
    print(val)
    result[val] = num[i]

print (num [0:1])
print(str (result))
