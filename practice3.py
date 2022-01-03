
def input_member(fn):
    f = open(fn, 'a')
    while True:
        name = input('멤버를 입력하세요 (종료는 q):')
        if name == 'q':
            break
        data=name +'\n'
        f.write(f'{name}\n')
    f.close()

def output_member(fn):
    try:
        f=open(fn,'r')
    except FileNotFoundError:
        print('파일이 없습니다.')
    else:
        while True:
            line= f.read()
            if not line:
                break
            print(line)
        f.close()

while True:
    num = input('저장 1,출력 2, 종료 q : ')
    if num=='1':
        filename= input('멤버 명단을 저장할 파일명 :')
        input_member(filename)

    elif num=='2':
        filename = input('멤버 명단 파일명 :')
        output_member(filename)


    elif num=='q':
        break

