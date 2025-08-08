#2025년 8월 6일 화이팅입니다!!!
lista = [1, 2, 3, 4, 5]
listb = [6, 7, 8, 9, 10]

listc = lista + listb  # 리스트 연결
print(listc)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

listd = listc * 2  # 리스트 반복
print(listd) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# insert, append, extend : 파괴적 리스트 연산 (원본 리스트에 직접적인 변경을 가함)

lista.insert(0, 0)  # 리스트.insert(위치, 값)
print(lista)  # [0, 1, 2, 3, 4, 5]

listb.append(11)  # 리스트.append(값) -> 뒤에 추가
print(listb)  # [6, 7, 8, 9, 10, 11]

listc.extend([12, 13])  # 리스트.extend(리스트) 인자로 리스트를 받아 뒤에 추가
# extend는 리스트를 확장하는데 사용, append는 단일 요소를 추가
print(listc)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]


#리스트 요소 제거 : 인덱스로 제거, 값으로 제거, 모두 제거

# 1. 인덱스로 제거하기
lista.pop(2)  # 리스트에서 해당 값을 제거하며 반환까지 한다는 점에 유의!! (Ex - poped_out = lista.pop(2)
              # 인덱스값을 소괄호 안에 넣어서 헷갈렸던 구문
del lista[2]  # 해당 값을 제거 + 슬라이싱도 된다는거!
del lista[1:3]  # 슬라이싱이 되는 del 구문

# 2. 값으로 제거하기
listb.remove(7)  # 리스트에서 해당 값을 제거 - 중복되는 값이 있다면 첫 번째 값만 제거

# 3. 모두 제거하기
listc.clear()  # 리스트의 모든 요소를 제거
print(listc)  # []


# 리스트 정렬 : sort, reverse
lista = [5, 3, 1, 4, 2]
lista.sort()  # 리스트.sort() -> 원본 리스트를 오름차순 정렬 (리스트를 직접 변경함 - 파괴적 연산)
lista.sort(reverse=True)  # 내림차순 정렬


# 리스트 내 값 확인
print(3 in lista)  # True
print(6 in lista)  # False


# for문
# 기본적인 구조는 for 변수 in 리스트: 후 다음 줄 들여쓰기
for i in lista:
    print(i)  # 1, 2, 3, 4, 5 순서대로 출력

for _ in lista: # 반복문에서 변수명을 사용하지 않을 때 주로 사용
    print("집에가고싶다")  

# 이중 for문 예제
list_of_lists = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
for i in list_of_lists:
    for j in i:
        print(j)  # 각 리스트의 요소를 순차적으로 출력


# 리스트 전개 연산자 - 원본 리스트의 변경 없이 사용하기 위함
# *리스트 형태로 사용
lista = [1, 2, 3, 4]
listb = [*lista, 5]     # 여기서 lista의 모든 값들이 전개됨.
print(listb)
print(*lista)           # 마찬가지로 리스트a속 모든 값들이 전개되어 print됨




# 딕셔너리
dicta = {
    "짜장면" : "짬뽕",
    "콜라" : "사이다",
    "물냉" : "비냉"
}
print(dicta)

dicta["콜라"] # 딕셔너리 내부 값에 접근할때는 리스트 인덱싱처럼 [] 대괄호를 이용한다.

# 딕셔너리도 value로 list를 가질 수 있다.
dictb = {
    "한식" : ["비빔밥", "냉면", "잡채"],
    "중식" : ["어항가지", "팔보채", "건전복"],
    "일식" : ["스시", "냉모밀", "우동"]
}
print(dictb["한식"])
print(dictb["일식"][1])     # 마찬가지로 인덱싱과 슬라이싱이 가능하다.

# 딕셔너리에 key와 value를 직접 추가하기
dictb["양식"] = ["파스타", "리조토", "피자"]    # 리스트에 인덱스로 직접 추가하는 방법과 같다. (이미 있는 key면 value가 대체됨)
print(dictb)

del dictb["양식"]               # 딕셔너리 요소를 삭제할때 del은 리스트와 동일하다.
print(dictb)

key = input("접근하고자 하는 키를 입력하시오")
if key in dictb:            # 딕셔너리도 마찬가지로 in 혹은 not in 구문을 사용가능함
    print(dictb[key])
else:
    print("존재하지 않는 key에 접근하고 있습니다.")

# else:
dictb.get("양식")   # 존재하지 않는 key에 접근할 경우 None 반환함.
dictb.get("일식")

# 딕셔너리와 for문
for i in dictb:
    pass        # 마찬가지로 코드를 짜면 된다

# 예제
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}
for i in numbers:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

print(counter)

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "홍염의 검",
        "armor" : "풀 플레이트"
    },
    "skills" : ["베기", "찌르기", "구르기"]
}

for i in character:
    if character[i] is dict:
        for j in i:
            print(j,":",i[j])
    else:
        print(i,":",character[i])


# 25년 8월 8일 화이팅입니다~!!

# 인덱싱의 세가지 방법
for i in range(10):
    print(i)

for i in range(5,10):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(10,-1,-1):
    print(i)

for i in reversed(range(10)):
    print(i)


# for _ in 뒤에 range를 넣을지 자료를 넣을지
array = [332, 1321, 112, 123, 541]

for i in array:
    print(i)

for i in range(len(array)):
    print(i, array[i])


#예제
n = int(input("피라미드의 층수:"))
for i in range(n):
    print("*" * (i+1))


output = ""
for i in range(9):
    output += "*"
    print(output)

n = int(input("층수는?"))
for i in range(n):
    print(" " * (n - 1 - i) + "*" * (2 * i + 1))

output = ""
for i in range(1, 15):
    for j in range(14,i,-1):
        output += " "
    for k in range(0,2*i-1):
        output += "*"
    output += "\n"
print(output)


# 무한반복 - while True
while True:
    print("집에가고싶어")
# Ctr + C 로 종료하기

m = 0
while m < 10:
    print(f"{m+1}번째 반복입니다.")
    m += 1


import time
target_tick = time.time() + 5
number = 0
while time.time() < target_tick:
    number += 1
print(f"{number}만큼 반복했습니다.")


# 무한반복을 푸는 break
i = 0

while True:
    i += 1
    print(f"{i}번째 반복입니다.")
    input_text = input("종료하시겠습니까?(Y/N)")
    if input_text in ["Y", "y"]:
        break

# 조건부 건너뛰기, continue
listk = [10,13,13,41,51,123,43,52,62,26,73]
for i in listk:
    if i < 30:
        continue
    print(i)

#예제 - 딕셔너리 만들기
key_list = ['name', 'hp', 'mp', 'level']
value_list = ['knight', 200, 30, 5]
character = {}

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]
print(character)


# 예제 - n * (n + 1) / 2
sum_value = 0
limit = 1000
count=0

while sum_value < limit:
    count += 1
    sum_value += count

print(f"{count}를 더할 때 {limit}을 넘으며, 이때의 값은 {sum_value}입니다.")


#예제 - 99까지 최대의 곱
mtpvalue = 0
for i in range(100):
    if mtpvalue < i * (100 - i):
        x = i
        y = 100 - i
        mtpvalue = i * (100 - i)
print(f"{x} X {y} = {mtpvalue}일 때가 최대의 값입니다.")