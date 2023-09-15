def felismer():
    x = int(input("adj meg egy számot"))
    y = int(input("adj meg egy másik számot"))


    if x > y:
        print("az első szám nagyobb")
        print(f'a nagyobb szám: {x}')

    elif x < y:
        print("a második szám nagyobb")
        print(f'a nagyobb szám: {y}')
    else:
        print("a két szám egyenlő")

felismer()


