from prac_06 import Guitar


def main():

    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)

    print(guitar1)

    if guitar1.is_vintage():
        print(guitar1.name)






main()