hello = '''오늘 하루도 새롭게 시작
이거 이렇게 하는게 맞는건가?
코가 너무 매워!!! '''

print(hello)


'''
파이썬은 문자열 연산도 가능!

ex)
1. 문자열 더하기
    head="python"
    tail="is fun"
    head + tail
    print(head+tail)
    >>> "python is fun"
   
2. 문자열 곱하기
    (2-1)a="python"
         a*2
         print(a*2)
         >>>"pythonpython"
    (2-2)print("="*50)
         print("My Program")
         print("="*50)
         
파이썬에서 문자열 길이를 나타낼 때 공백도 포함

파이썬은 문자열의 순서를 셀때는 0부터 센다.
파이썬은 -를 붙이면 문자열 뒤에서부터 순서를 셀 수 있다.
    *[-0] == [0]
    
문자열 인덱싱 + 슬라이싱 기법을 사용하면 
 a= "Life is too short, You need python"
 a[0:4] ----> a의 문자열중 0번째부터 3번째 까지의 문자열 보여줘 (끝 번호에 해당하는 문자의 순서는 포함하지 않음)
 >>> "Life" 
 
 a[19:-7] a의 문자열중 19번째부터 -8번째 까지의 문자열 보여줘 (끝 번호에 해당하는 문자는 포함하지 않음)
 >>> "You need"
 
 
 >>> a = "20230331Rainy"
>>> year = a[:4] 뒤에오는 값은 -1! 고로 맨 처음부터 3번째 순서까지
>>> day = a[4:8] 4번째 문자부터
>>> weather = a[8:]
>>> year
'2023'
>>> day
'0331'
>>> weather
'Rainy'



슬라이싱 기법을 활용해 '변경 불가능한 자료형'이라고 불리는 문자열을 변경할수 있음

>>> a = "Pithon"
>>> a[:1]
'P'
>>> a[2:]
'thon'
>>> a[:1] + 'y' + a[2:]
'Python'


%d 와 %s 는 ‘문자열 포맷 코드’ (변수 값으로 대입도 가능)
    %d : 숫자열을 넣기 위해서 사용
    %s : 문자열을 넣기 위해서 사용
        ex 1)"I eat %d apples." % 3 ---> "I eat 3 apples."
           2)"I eat s% apples." %"five" ---> "I eat five apples."
    *2개 이상의 값을 넣으려면 마지막 % 다음 괄호 안에 쉼표(,)로 구분하여 각각의 값을 넣어 주면 됨.
        ex) "I ate %d apples. so I was sick for %s days." % (number, day) 
            ---> 'I ate 10 apples. so I was sick for three days.'
            
        문자열 포맷 코드를 사용할 때, %d와 %가 같은 문자열 안에 존재하는 경우, %를 나타내려면 반드시 %%(%%사이에 원하는 값을 작성)를 써야 한다
        ex) >>> "Error is %d%%." % 98
                'Error is 98%.'
                
        %10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨두라는 뜻
        ex) >>> (오른쪽 정렬) "%10s" % "hi" ---> "        hi"
            >>> (왼쪽정렬) "%-10sjane." % 'hi' ---> 'hi        jane.'
            
format 함수를 사용한 포매팅
    숫자로 바로 대입하기 
        ex) >>> "I eat {0} apples".format(3) ---> 'I eat 3 apples'
    문자열 바로 대입하기
        ex) >>> "I eat {0} apples".format("five") ---> 'I eat five apples'
    숫자 값을 가진 변수로 대입하기
        ex) >>> number = 3
            >>> "I eat {0} apples".format(number) ---> 'I eat 3 apples'
    2개 이상의 값 넣기
        ex) >>> number = 10
            >>> day = "three"
            >>> "I ate {0} apples. so I was sick for {1} days.".format(number, day)
    이름으로 넣기 (인덱스와 이름을 혼용도 가능)
        ex) >>> "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
                    ---> 'I ate 10 apples. so I was sick for 3 days.'
'''