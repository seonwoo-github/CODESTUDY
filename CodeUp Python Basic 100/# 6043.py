# Question
'''
실수 2개(f1, f2)를 입력받아
f1 을 f2 로 나눈 값을 출력해보자. 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.
'''

# Input
f1, f2 = input().split(' ')


# Answer
def solution(f1, f2):  
    f1 = float(f1)
    f2 = float(f2)
    
    A = f1/f2
    
    print('{:.3f}'.format(A))

solution(f1, f2)