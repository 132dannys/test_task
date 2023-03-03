def check_relation(arr, fname, sname):
    array_of_fname_connects = list()
    visited = set()

    def depth_first_search(name):
        visited.add(name)
        for pair in arr:
            if name in pair:
                for elem in pair:
                    array_of_fname_connects.append(elem)
        for item in array_of_fname_connects:
            if item not in visited:
                depth_first_search(item)

    depth_first_search(fname)
    
    if sname in set(array_of_fname_connects):
        return True
    else:
        return False    


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
