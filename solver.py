def clear():
    print('\n'*5)
clear()
n = input('Input an upper bound for this list. Default: 100. \nResponse:        ')
float_str = float(n)
n = int(float_str)
clear()
d = input('Input the first number. Default: 3. \nResponse:        ')
float_str = float(d)
d = int(float_str)
clear()
e = input('Input the second number. Default: 5. \nResponse:        ')
float_str = float(e)
e = int(float_str)
clear()
k=b=c=0
finished = False
a_list = list(range(1, n+1))
while finished == False:
    if a_list[k]==(b*d)+(c*e):
        a_list.pop(k)
    k=k+1
    if k >= len(a_list):
        k = 0
        b = b + 1
        if b >= (n / d)+1:
            c = c + 1
            b = 0
            if c >= (n / e)+1:
                clear()
                print('Completed!','\n'*5,a_list)
                finished = True
