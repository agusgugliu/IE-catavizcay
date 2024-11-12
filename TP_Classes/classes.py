class Car:
    def __init__(self, make, model, year, mileage=0):
        self.make = make.upper()
        self.model = model.title()
        self.year = year
        self.mileage = mileage

    def drive(self, miles):
        if miles > 0:
            self.mileage += miles
        else:
            print("Miles driven must be positive.")

    def display_info(self):
        print(f"CAR INFO: {self.year} {self.make} - {self.model}.\nMileage: {self.mileage} miles")

def add_and_drive_cars():
    make = input("Enter the car make: ")
    model = input("Enter the car model: ")
    year = int(input("Enter the car year: "))
    mileage = float(input("Enter the car mileage: "))

    #NEW CAR
    car = Car(make, model, year, mileage)
    car.display_info()

    #DRIVE CAR
    miles = float(input("Enter the number of miles to drive: "))
    car.drive(miles)

    car.display_info()


#EXECUTE
add_and_drive_cars()