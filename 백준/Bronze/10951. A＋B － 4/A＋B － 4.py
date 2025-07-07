import sys

while 1:
    line = sys.stdin.readline()
    if not line:
        break # 예외처리 (EOF 검사) 먼저 하고
    a, b = map(int, line.split()) # 할 거 진행, 안그러면 map(~)이 먼저 실행되면서 ValueError 발생
    print(a+b)

