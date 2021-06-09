def error_handling(error):
    error_switch = {
        "ValueError":  wrong_type(), #You can place here a function, or whatever u want!
        "IndexError": "IndexError occurred!",
        "AttributeError": "AttributeError occurred!",
        "KeyError": "KeyError occurred!"
        #more expections...
    }
    return error_switch[error]


def wrong_type():
    return "Wrong type!"


def sum_two_number(a, b):
    return int(a) + int(b)


def main():
    try:
        sum_two_number(3, "e")
    except Exception as ex:
        print(error_handling(str(type(ex).__name__)))


if __name__ == '__main__':
    main()