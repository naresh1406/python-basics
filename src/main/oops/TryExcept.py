import sys


class TryExcept:  # class name

    def raise_exception(self, name):  # method definition
        print("Hi {}!!!".format(name))  # method body
        raise Exception  # raise exception


def main():  # main function to initialize instance and call methods
    name = ""
    try:
        name = TryExcept().raise_exception("Naresh")
    except:
        print("exception raised")

    print(name)

    random_list = ['a', 0, '2']
    for entry in random_list:
        try:
            print("The entry is " + entry)
            r = 1 / int(entry)
            break
        except:
            # sys.exc_info()[0] - to print the type of exception
            print("Oops! ", sys.exc_info()[0], "occurred.")
            print("Next entry")
            print()

    print("The reciprocal of ", entry, "is ", r)

    # catching specific exception
    try:
        # do something
        pass

    except ValueError:
        # handle ValueError exception
        pass

    except (TypeError, ZeroDivisionError):
        # handle multiple exceptions
        # TypeError and ZeroDivisionError
        pass

    except:
        # handle all other exceptions
        pass


if __name__ == '__main__':  # to run the main function
    main()
