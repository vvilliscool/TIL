f1=open('yesterday.txt', 'r')

total=''
while True:
    line = f1.read()
    if not line:
        break
    strings = line.strip('\n')
    total += (strings+' ')

low_total = total.lower()

words_list=set(low_total.split())
words_list=sorted(words_list)

words=low_total.split()

result = {}
for i in words_list:
    cnt= words.count(i)

    result= {i : cnt}
    print(result)

f1.close()

