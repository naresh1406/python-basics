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


if __name__ == '__main__':  # to run the main function
    main()
