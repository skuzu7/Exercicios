def fibonacci(n):
    # Calcula a sequência de Fibonacci até o valor n
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

# Pede ao usuário para informar um número
num = int(input("Digite um número: "))

# Calcula a sequência de Fibonacci até o valor informado pelo usuário
fib_seq = fibonacci(num)

# Verifica se o número fornecido pertence à sequência de Fibonacci
if num in fib_seq:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")