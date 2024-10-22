def add(a, b):
    print('function add!!')
    c = a + b
    return c

def print_result(string):
    print(f'string to print : {string}')


def main():
    print('start')
    result = add(10, 20)
    print_result(result)
    print('end')
    
    for i in range(4):
        

if __name__ == '__main__':
    main()