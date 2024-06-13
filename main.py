from datetime import time


def lesson():
    yield "lesson"
    time.sleep(2)
    for number in range(1, 50):
        if number % 2 == 1:
            print(number)

            def lesson_1():
                yield f"{number**2}"
                print("lesson the end")