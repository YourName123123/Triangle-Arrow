x =0
def triangle(num):
    for n in range(num):
        s = (num - n )*2
        a = 1 + (2*n)
        print(" "*s + "* "* a + " "*s)
    
def arrow(num):
    triangle(num=i)
    while True:
        global x
        s = ((num) - 1 )*2
        a = 1 + (2*1)
        print(" "*s + "* "* a + " "*s)
        x += 1
        if x == num:
            break


i = int(input("Enter the rows:"))
triangle(num=i)
arrow(num=i)
