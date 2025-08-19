## 2025년 8월 19일 화이팅입니다!!

# 오류가 발생하는 두가지 상황

# 1. 코드를 실행하기 이전에 발생 (SyntaxError - 구문오류)
# 2. 코드를 실행하는 도중에 발생 (RuntimeError - 예외)


## 두번째 예외를 처리하기 위한 조치 - 예외처리
user_input = input("반지름 입력")

if user_input.isdigit():

    num_input = int(user_input)
    print(f"원의 반지름: {num_input}")
    print(f"원의 둘레: {num_input * 2 * 3.14}")
    print(f"원의 넓이: {num_input ** 2 * 3.14}")

#여기가 예외처리
else:
    print("정수를 입력해 주십시오")


## 모든 경우의 수를 if else로 나누기 힘든 경우 ->
## try, except 구문!!!

# try:
    # 예외 발생 가능한 구문
# except:
    # 예외 발생시 실행할 구문

try:
    num_input = int(input("정수만 입력해 주십시오"))
    print(f"원의 반지름: {num_input}")
    print(f"원의 둘레: {num_input * 2 * 3.14}")
    print(f"원의 넓이: {num_input ** 2 * 3.14}")
except:
    print("오류가 발생했습니다!")

## 강제 종료를 막는 코드
try:
    num_input = int(input("정수만 입력해 주십시오"))
    print(f"원의 반지름: {num_input}")
    print(f"원의 둘레: {num_input * 2 * 3.14}")
    print(f"원의 넓이: {num_input ** 2 * 3.14}")
except:
    pass

list_a = [1,2,3,"사",5,6,"八"]
list_num = []
for i in list_a:    
    try:
        list_num.append(float(i))
    except:
        pass
print(list_num)


## try except 이후 
# else - 예외 가능성 코드를 try except로, 나머지 구문은 else에 넣는다고 보면 됨
# finally - 두 경우 모두에 마지막으로 실행할 코드 close() 등의 파일처리가 자리하는 부분 (반복문이나 함수 내에서 try 구문 사용시)

# try:
    # 예외발생 가능 구문
# except:
    # 예외 발생시 구문
# else:
    # 예외 발생하지 않았을 시 구문

try:
    num_input = int(input("반지름을 입력해주십시오"))
except:
    print("정수가 입력되지 않았습니다")
else:
    print(f"원의 반지름: {num_input}")
    print(f"원의 둘레: {num_input * 2 * 3.14}")
    print(f"원의 넓이: {num_input ** 2 * 3.14}")
finally:
    print("프로그램을 마칩니다.")


## 예외 객체 except를 예외의 종류별로 사용하고자 할 때
