def func(name):
    def func_2():
        print("start")
        name()
        print("the end")

    return func_2()


def f():
    print("middle")


func(f)
