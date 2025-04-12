#1
def task_1(a: int, b: float, c: str, d: list, e: bool):
    return(type(a), type(b), type(c), type(d), type(e))

print(task_1(3, 9.2, "hello", [5, "May", True], False))

#2
def task_2(a=[1, 2, 3, 5, 8, 13, 21]) -> list:
    print(a[0:2])

task_2()

