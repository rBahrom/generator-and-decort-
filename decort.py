import time


def lesson():
    print("lesson start")
    time.sleep(2)
    for number in range(1, 50, 6):
        if number % 2 == 1:
            print(number)
            yield "lesson"

            def lesson_1():
                print("Lesson 1")
                yield f"{number**2}"

            return lesson_1()

def vazifa(a):
    yield "start vazifa"
    yield "power step"
    for m in range(1, a*2, a):
        print(m**2)
        yield "power the end"

def vazifa_1(b):
    yield "Vazifa_1 start"
    data = []
    for n in range(1, b):
        if n % 2 == 0:
            data.append(n)
    print(data)


def vazifa_2(a, b):
    print("start vazifa_2")
    yield f"(a+b) = {a+b}"
    yield f"(a*b) = {a*b}"
    yield f"(a+b)^2 = {a**2 + 2*a*b + b**2}"
    yield f"(a-b)^2 = {a**2 - 2*a*b + b**2}"
    yield vazifa(4)

def test():
    yield lesson()
    yield vazifa(5)
    yield vazifa_1(15)
    yield vazifa_2(2, 3)


for i in test():
    print("next")
    time.sleep(1)
    for j in i:
        time.sleep(1)
        print(j)


print("The end")
