import itertools

def is_prime(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

cnt = 0
numbers = '1111'
lst = []

for i in range(len(numbers)):
    s_numbers = itertools.permutations(numbers,i+1)
    s_numbers = list(set(list(s_numbers)))

    for j in s_numbers:
        tmp = ''.join(j)
        tmp = int(tmp)

        if tmp in lst:
            continue

        lst.append(tmp)

        if is_prime(tmp):
            cnt += 1
