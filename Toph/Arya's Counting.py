for i in range(int(input())):
    l =[int(x) for x in input().split()]
    if l.count(max(l)) > 1:ans = 'Confused'
    else:ans = 'ABC'[l.index(max(l))]
    print('Case {}: {}'.format(i+1, ans))
