#2025년 8월 10일 화이팅입니다!!

def three_hello():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

three_hello()


def print_n_times(value, n=3):  # 가변 매개변수인 n이 기본으로 3으로 설정되어있다. 
    for i in range(n):          # 마치 print()함수가 end = "\n" 인것과 마찬가지이다.
        print(value)            # 여기서 일반 매개변수인 value는 절대 n 뒤에 위치하게 정의하지 못한다

print_n_times("안녕하세요", n=5)


#예제
def f(x):
    return 2*x+1
print(f(10))

def f(x):
    return x**2+x*2+1
print(f(10))

scores = [85, 92, 78, 96, 88]
*others, highest = sorted(scores)
print(highest)

def mul(*values):
    answer = 1
    for i in values:
        answer *= i
    return answer
print(mul(5, 7, 9, 10))

def factorial(x):       ## 반복문이 아닌 재귀함수를 이용한 팩토리얼 계산
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(3))     ## 재귀함수는 컴퓨팅 자원을 많이 소모한다는 이야기가 있다.


##재귀함수를 이용해 도출한 피보나치 수열 (재귀함수의 위험성)
counter = 0

def fib(n):
    print(f"fibonacci_{n}를 구합니다")
    global counter                      ## 함수 내부에서 원래 불가능한 외부 값 참조를 위해 사용하는 global 함수.
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

fib(35)
print("---")
print(f"피보나치 35을 구하는데 사용된 계산 횟수는 {counter}회 입니다.")
## 피보나치 35의 경우에는 18454929번 계산함. 
## 재귀 함수는 한번 구한 값도 반복해서 다시 계산하기 때문

## 이를 위해 메모화(memoization)을 활용하는 것임
## 다시 말해 한번 계산한 값은 다시 계산하지 않게 만들기 위함임.

counter = 0

dictionary = {
    1 : 1,
    2 : 1
}

def fib(n):
    global counter
    counter += 1
    if n in dictionary:
        return dictionary[n]
    else:
        output = fib(n-2) + fib(n-1)
        dictionary[n] = output
        return output

print(fib(35))
print(f"fib 35를 구하기 위한 계산 횟수는 {counter}회 입니다.")

## 메모화 이전 계산횟수 : 18454929
## 메모화 이후 계산횟수 : 67회

