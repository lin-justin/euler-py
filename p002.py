def fibonacci(n: int) -> int:
    result = 0
    x, y = 1, 2
    while x <= n:
        if x % 2 == 0:
            result += x
        x, y = y, x + y
    return result

def main():
    print(fibonacci(4000000))

if __name__ == "__main__":
    main()