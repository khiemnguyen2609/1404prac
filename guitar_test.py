from prac_06.guitar import Guitar

def main():

    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2012, 100)

    guitars = [guitar1, guitar2]
    print(guitars)

    for guitar in guitars:
        print(guitar.get_age())
        if guitar.is_vintage():
            print(guitar.name)






main()