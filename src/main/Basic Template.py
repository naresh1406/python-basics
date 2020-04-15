class Basic:  # class name
    def greet(self, name):  # method definition
        print("Hi {}!!!".format(name))  # method body


def main():  # main function to initialize instance and call methods
    Basic().greet("Naresh")


if __name__ == '__main__':  # to run the main function
    main()
