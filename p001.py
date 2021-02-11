def solution(n: int) -> int:
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

def main():
    print(solution(1000))

if __name__ == "__main__":
    main()