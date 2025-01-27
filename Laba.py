def calculator(a, b, operation='add', *args, **kwargs):
    result = 0
    
    if operation == 'add':
        result = a + b        
        for num in args:
            result += num

    elif operation == 'subtract':
        result = a - b
        for num in args:
            result -= num

    elif operation == 'multiply':
        result = a * b
        for num in args:
            result *= num
            
    elif operation == 'divide':
        if b == 0 or 0 in args:
            return 'Помилка: Ділити на нуль не можна!'
        result = a / b
        for num in args:
            if num != 0:
                result /= num
    
    if 'round_result' in kwargs and kwargs['round_result']:
        result = round(result)

    if 'log_result' in kwargs and kwargs['log_result']:
        print(f'Result: {result}')
    
    return

