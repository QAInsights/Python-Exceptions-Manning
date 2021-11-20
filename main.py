# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def name_exception(name):
    # Use a breakpoint in the code line below to debug your script.
    try:
        print(name1)
    except NameError as e:
        print(e)


def index_exception(a):
    try:
        for i in a:
            print(a[4])
    except IndexError as e:
        print(e)


def file_exception():
    try:
        with open('test', 'r') as f:
            f.write("hello")
    except FileNotFoundError as e:
        print(e)


def zero_exception():
    try:
        ans = 0 / 0
        print(ans)
    except ZeroDivisionError as e:
        print(e)


def syntax_exception():
    try:
        eval('pass = True')
    except SyntaxError as e:
        print(e)
    else:
        pass
    finally:
        print("Exit")

def key_exception():
    try:
        ages = {'a': 30, 'b': 28, 'c': 24}
        ages['d']
    except KeyError as e:
        print("KeyError")
    finally:
        print("Exiting")


if __name__ == '__main__':
    # name_exception("Ria")
    n = [1, 2, 3]
    # index_exception(n)
    file_exception()
    zero_exception()
    syntax_exception()
    key_exception()