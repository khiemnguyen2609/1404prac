from unreliable_car import UnreliableCar


def main():

    my_car = UnreliableCar("Hex", 50, 60)
    for i in range(1, 6):
        print("Attempting to drive {} km".format(i))
        print("{} drove {} km".format(my_car, my_car.drive(i)))
    print(my_car)


main()
