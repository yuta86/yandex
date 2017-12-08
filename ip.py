'''

Предположим, у нас есть access.log веб-сервера. Как с помощью стандартных консольных средств найти десять IP-адресов,
от которых было больше всего запросов? А как сделать это с помощью программы на вашем любимом языке программирования?

'''

import re

pattern = r'^(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])(\.(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])){3}$'

result_ip = {}
print('start analysis...')
with open('access.log', 'r', encoding='utf-8') as file:
    for line in file:
        # print(line)
        result = re.match(pattern, line)
        if result:
            # print(result.group(0))
            if result.group(0) in result_ip:
                result_ip[result.group(0)] += 1
            else:
                result_ip[result.group(0)] = 1

# print('all')
# print(result_ip)

result_ip_sort = sorted(result_ip.items(), key=lambda x: x[1])

# print('all sorted')
# print(result_ip_sort)

# print('10 sorted')
# print(type(result_ip_sort))

result_ip_sort = result_ip_sort[:-11:-1]
print(result_ip_sort)

print('end analysis...')
