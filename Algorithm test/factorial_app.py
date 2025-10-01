import time

def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

def run_with_time(func, n: int):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

def menu():
    test_data = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]
    while True:
        print("\n===== Factorial Tester =====")
        print("1) 반복법으로 n! 계산")
        print("2) 재귀로 n! 계산")
        print("3) 두 방식 모두 계산 후 결과/시간 비교")
        print("4) 준비된 테스트 데이터 일괄 실행")
        print("q) 종료")
        choice = input("선택: ").strip()

        if choice == "q":
            print("종료합니다.")
            break

        elif choice in ["1", "2", "3"]:
            n_str = input("n 값(정수, 0 이상)을 입력하세요: ")
            if not n_str.isdigit():
                print("정수(0 이상)만 입력하세요.")
                continue
            n = int(n_str)

            try:
                if choice == "1":
                    result, t = run_with_time(factorial_iter, n)
                    print(f"[반복] {n}! = {result} (걸린 시간: {t:.6f}초)")
                elif choice == "2":
                    result, t = run_with_time(factorial_rec, n)
                    print(f"[재귀] {n}! = {result} (걸린 시간: {t:.6f}초)")
                elif choice == "3":
                    r1, t1 = run_with_time(factorial_iter, n)
                    r2, t2 = run_with_time(factorial_rec, n)
                    print(f"[반복] {n}! = {r1} (시간: {t1:.6f}초)")
                    print(f"[재귀] {n}! = {r2} (시간: {t2:.6f}초)")
            except ValueError as e:
                print(f"오류: {e}")

        elif choice == "4":
            print("테스트 데이터 실행 중...")
            for n in test_data:
                try:
                    r1, t1 = run_with_time(factorial_iter, n)
                    r2, t2 = run_with_time(factorial_rec, n)
                    print(f"\n== n={n} ==")
                    print(f"[반복] 결과 OK, 시간 {t1:.6f}초")
                    print(f"[재귀] 결과 OK, 시간 {t2:.6f}초")
                except Exception as e:
                    print(f"n={n} 실행 중 오류: {e}")
        else:
            print("올바른 메뉴를 선택하세요.")

if __name__ == "__main__":
    menu()