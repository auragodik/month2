x = int(input('введи число лее'))
c = list(range(1, x + 1))
print("Список:", c)
z = sum(c)
print(z)
q = 1
for w in c:
    q *= w
    print('произведение', q)
c_lambda = list(filter(lambda x: x % 2 == 0, c ))
print('chetnye', c_lambda)
