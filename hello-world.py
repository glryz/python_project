def fibonacci(n):
    sequence = [1,1]
    for i in range(1,n):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

sequence = fibonacci(8):

print('fibonacci :',sequence)
