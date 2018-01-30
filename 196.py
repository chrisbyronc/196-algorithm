def one_nine_six_algorithm(a):
    b = a
    count = 0
    if a > 9:
        while str(b)[::-1] != str(b):

            c = str(b)[::-1]
            b += int(c)
            count += 1
        return { 'number' : a , 'palendrome' : b , 'iter' : count}

run = []
for x in range(10, 393):
    if x != 196 and x != 295:
        run.append(one_nine_six_algorithm(x))

longestIter = 0
for i in range(0, len(run)):
    if i != 196 and x != 295:
        if(run[i]['iter'] > longestIter):
            longestIter = run[i]['iter']
            longest = {
             'number' : run[i]['number'],
             'palendrome' : run[i]['palendrome'], 
             'iter' : longestIter
          }
            


print longest