def check_relation(arr, fname, sname):
    first_array_of_friends = []
    second_array_of_friends = []

    def find_friends(name):
        array_of_pairs = []
        for item in arr:
            if name in item:
                array_of_pairs.append(item)

        result = []
        for elem in array_of_pairs:
            result.extend(elem if isinstance(elem, tuple) else [elem])

        for item in result:
            if item not in first_array_of_friends:
                first_array_of_friends.append(item)        

    def find_friends2(name):
        array_of_pairs = []
        for item in arr:
            if name in item:
                array_of_pairs.append(item)

        result = []
        for elem in array_of_pairs:
            result.extend(elem if isinstance(elem, tuple) else [elem])
                    
        for item in result:
            if item not in second_array_of_friends:
                second_array_of_friends.append(item)          

    find_friends(fname)    
    find_friends2(sname)  

    for i in range(len(first_array_of_friends)):
        find_friends(first_array_of_friends[i])

    for i in range(len(second_array_of_friends)):
        find_friends2(second_array_of_friends[i])

    result = list(set(first_array_of_friends) & set(second_array_of_friends))
    if len(result) == 0:
        return False
    else:
        return True    


if __name__ == '__main__':
    net = (
        ('Ваня', 'Леша'), ('Леша', 'Катя'),
        ('Ваня', 'Катя'), ('Вова', 'Катя'),
        ('Леша', 'Лена'), ('Оля', 'Петя'),
        ('Степа', 'Оля'), ('Оля', 'Настя'),
        ('Настя', 'Дима'), ('Дима', 'Маша')
    )

    assert check_relation(net, 'Петя', 'Степа') == True 
    assert check_relation(net, 'Маша', 'Петя') == True    
    assert check_relation(net, 'Ваня', 'Дима') == False  
    assert check_relation(net, 'Леша', 'Настя') == False 
    assert check_relation(net, 'Степа', 'Маша') == True 
    assert check_relation(net, 'Лена', 'Маша') == False 
    assert check_relation(net, 'Вова', 'Лена') == True 
