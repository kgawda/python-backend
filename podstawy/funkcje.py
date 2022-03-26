def main():
    def f1(arg1, arg2, arg3=333):
        print(arg1, arg2, arg3)
    f1(1, 2, 3)
    f1(1, 2)
    f1(1, arg3=3, arg2=2)
    # nie zadziała: f1(1, arg3=3, 2)
    f1(arg1=1, arg3=3, arg2=2)
    # nie zadziała: f1(arg1=1, 3, 2)

    def f2(*args, **kwargs):
        print(args, kwargs)

    f2(1, 2, 3, test4=4, test5=5, cokolwiek=True)
    f2()

    def f3(arg1, *args, name, **kwargs):
        print(args, kwargs)
    f3(1, 2, 3, name="Test", cokolwiek=1234)

    t = (1, 2, 3)
    f1(*t)  # <--> f1(1, 2, 3)
    d = {'arg1': 1, 'arg2': 2, 'arg3': 3}
    f1(**d)  # <--> f1(arg1=1, arg2=2, arg3=3)

    # przekaż wszystkie argumenty:
    #def f4(*args, **kwargs):
    #    f3(*args, **kwargs)



if __name__ == '__main__':
    main()