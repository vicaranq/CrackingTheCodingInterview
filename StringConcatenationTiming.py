import timeit

def normalConca():
    temp = ''
    for char in range(1000):
        temp += str(char)
    return temp

def joinConca():
    temp = ''
    for char in range(1000):
        temp.join(str(char))
    return temp

def joinConca2():

    temp = ''.join(map(str ,range(1000)))
    return temp

def listToString():

    l = []
    for i in range(1000):
        l.append(i)

    return ''.join(map(str,l))


def timefunct(name):
    SETUP_CODE = f'''from __main__ import {name}'''

    TEST_CODE = f'''{name}()'''

    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
    return times


if __name__ == '__main__':
    #
    # times = timefunct('normalConca')
    # print(f'Normal Concatenation time:  {min(times)}')
    #
    # times = timefunct('joinConca')
    # print(f'joinConca Concatenation time:  {min(times)}')
    #
    # times = timefunct('joinConca2')
    # print(f'joinConca2 Concatenation time:  {min(times)}')

    times = timefunct('listToString')
    print(f'listToString Concatenation time:  {min(times)}')

    '''
    Normal Concatenation time:  3.4618344999999997
    joinConca Concatenation time:  4.332490100000001
    joinConca2 Concatenation time:  1.9204395999999981
    listToString Concatenation time:  2.5347735

    '''