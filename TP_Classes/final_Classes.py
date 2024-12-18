'''
Welcome to your Digital University Advisor!
Are you unsure about where you want to study and what you want to study?
Our Digital University Advisor allows the user to search by two options.

The first option allows the user to narrow down their search by asking the user for the country
they want to study in and degree. After the user inputs the country of their choice, a list will be
printed with the degrees in that specific country.

If the user is unsure about where they want to study but know what degree, the second option
allows the user to search by degree. If the user chooses this option (inputs 2), the user will be
given a list of the degrees to choose from. Once the user inputs the degree, a list of countries will
be printed with that specific degree.

The list contains 15 degrees: 'Computer Science','Business Administration','Law','Medicine','Engineering',
'Fashion Design', "Psychology", "Philosophy", "Art History", "Architecture", "Environmental Science",
"Economics", "Sustainable Development", "Design", "Hospitality Management"

A list of 8 countries: "Spain", "France", "Germany", "Italy", "Netherlands", "Sweden",
"United Kingdom", "Switzerland"

The program works so that no matter how the user inputs "Spain" "spain" "SPain", the program will
continue to run

The program will continue to run until the user inputs "3" which then the program will end.
'''


class UniversityAdvisor: #We define the class

#First we create a list under class UniversityAdvisor, with all the current degrees this program has in its database.
    degree_2 = ['Computer Science',
              'Business Administration',
              'Law',
              'Medicine',
              'Engineering',
              'Fashion Design',
              'Psychology',
              'Philosophy',
              'Art History',
              'Architecture',
              'Environmental Science',
              'Economics',
              'Sustainable Development',
              'Design',
              'Hospitality Management'
              ]

#We create a nested dictionary with the information for the different universities available filtered by degree and country.
    universities_data = {
        "Spain": {
            "Computer Science": ["University of Barcelona", "Polytechnic University of Madrid",
                                 "University of Valencia"],
            "Business Administration": ["IE Business School", "ESADE Business School", "EADA Business School"],
            "Law": ["University of Salamanca", "University of Granada"],
            "Medicine": ["University of Navarra", "Autonomous University of Barcelona"]
        },

        "France": {
            "Engineering": ["École Polytechnique", "CentraleSupélec"],
            "Business Administration": ["HEC Paris", "INSEAD", "ESSEC Business School"],
            "Fashion Design": ["Paris College of Art", "École de la Chambre Syndicale de la Couture Parisienne"],
            "Psychology": ["University of Paris", "University of Bordeaux"]
        },

        "Germany": {
            "Computer Science": ["Technical University of Munich", "RWTH Aachen University"],
            "Engineering": ["Karlsruhe Institute of Technology", "TU Berlin"],
            "Medicine": ["Charité - Universitätsmedizin Berlin", "University of Heidelberg"],
            "Philosophy": ["Ludwig Maximilian University of Munich", "University of Freiburg"]
        },

        "Italy": {
            "Art History": ["University of Bologna", "University of Florence"],
            "Business Administration": ["Bocconi University", "Luiss Guido Carli University"],
            "Architecture": ["Politecnico di Milano", "Sapienza University of Rome"],
            "Law": ["University of Milan", "University of Padua"]
        },

        "Netherlands": {
            "Psychology": ["University of Amsterdam", "Utrecht University"],
            "Economics": ["Erasmus University Rotterdam", "Tilburg University"],
            "Environmental Science": ["Wageningen University", "Leiden University"],
            "Medicine": ["University of Groningen", "Radboud University"]
        },

        "Sweden": {
            "Sustainable Development": ["Lund University", "Uppsala University"],
            "Engineering": ["KTH Royal Institute of Technology", "Chalmers University of Technology"],
            "Business Administration": ["Stockholm School of Economics", "University of Gothenburg"],
            "Design": ["Umeå Institute of Design", "Konstfack University of Arts"]
        },

        "United Kingdom": {
            "Law": ["University of Oxford", "University of Cambridge", "LSE"],
            "Engineering": ["Imperial College London", "University of Manchester"],
            "Computer Science": ["University of Edinburgh", "University of Warwick"],
            "Business Administration": ["London Business School", "Cranfield University"]
        },

        "Switzerland": {
            "Hospitality Management": ["EHL (École Hôtelière de Lausanne)", "Les Roches"],
            "Business Administration": ["University of St. Gallen", "University of Zurich"],
            "Medicine": ["University of Basel", "University of Geneva"],
            "Environmental Science": ["ETH Zurich", "EPFL (École Polytechnique Fédérale de Lausanne)"]
        }
    }
#Function to tell the computer that the user will input a country and a degree, set the variables
    def __init__(self, country=None, degree=None): #(int) initializer, class parameters
        self.country = country #Initialize the study advisor with the specified country(parameter 1)
        self.degree = degree #Initialize the study advisor with the specified degree(parameter 2)

    def get_degrees(self): #function to filter dictionary with degree input by user.
        if self.country: #if the country from the user input is part of the classes
            return list(self.universities_data.get(self.country, {}).keys()) #filter by the country
        else:
            degrees = set()
            for country_data in self.universities_data.values():
                degrees.update(country_data.keys())
            return list(degrees)

    def get_universities(self):
        if self.country:
           return self.universities_data.get(self.country, {}).get(self.degree, "No universities found for this degree in the specified country.")
        else:
            universities = []
            for country, degrees in self.universities_data.items():
                if self.degree in degrees:
                    universities.extend(degrees[self.degree])
            return universities if universities else "No universities found for this degree."

    def display_options(self):#If the list exists, it creates a list called universities with the information required
        universities = self.get_universities()#Here is the list
        if isinstance(universities, list):#check that the variable university is a list then do the following actions
            print(f"Universities for {self.degree} degree:")
            for university in universities: #loop to print for all universities in the list in this way
                print('    -',university)
        else:
            print('    -',universities)


def main(): #Format the program, tell the user what the program is, (lines added for aesthetic)
    print('-------------------------------------------')
    print('Welcome to your Digital University Advisor!')
    print('-------------------------------------------')

    while True:
        #Create a list with the different options for the user to choose from.
        options = [
            '---------------------------------',
            '[1] Search by Country and Degree.', #Option 1 to filter by country and degree
            '[2] Search by Degree.', #Option 2 to filter only by degree, when the user don't know where they want to study
            '[3] Exit.', #Option 3 to close the program
            '---------------------------------'
        ]
        for option in options:#Create a loop to go over all the options and print them, for the user to see
            print(option)

        option = int(input("Please select an option:\t")) #Create a user input and give it a name for program to understand

        if option == 1: #create a conditional statement for option 1
            print('Available Countries:')
            for country in UniversityAdvisor.universities_data: #for the key 'country' in our nested dictionary within our classes
                print('    -',country)#print the countries

            country = input("Please enter the country you'd like to study in:\t").strip()#strip to remove spaces that the user input extra + user input
            country = country.title()

            if country not in UniversityAdvisor.universities_data: # If the country the user inputted is not in the dictionary, print text bellow
                print("Sorry, we don't have information for that country.")
                return

            degrees = UniversityAdvisor(country).get_degrees()#If the country the user inputted is on our nested dictionary, print the available degrees in that country
            print("Available degrees in", country) #Print initial intro
            print("------------------------------")
            for degree in degrees:#Create a loop to go over all the lines
                print('    -',degree) #Print available degrees
            print("------------------------------")

            degree = input("Please enter the degree you'd like to study:\t").strip() #create variable for user to input the degree of their choice
            degree = degree.title()#.title is to capitalize first letter, for format purposes

            if degree not in UniversityAdvisor.universities_data[country]: #if the degree is not in the nested dictionary for that country
                print("Sorry, we don't have information for that degree in", country) #text
                return

            advisor = UniversityAdvisor(country, degree)
            advisor.display_options()

        elif option == 2:# Create a conditional statement for the second option, to only filter by country
            print('Available Degrees:')
            for degree_2 in UniversityAdvisor.degree_2:#for the degrees in degree_2 (the list)
                print('    -',degree_2)#Telling the computer to print the available degrees no matter the country
            degree = input("Please enter the degree you'd like to study:\t").strip() #create input statement for computer to recognize input
            degree = degree.title()#format the degree names

            advisor = UniversityAdvisor(degree=degree)
            advisor.display_options()

        elif option == 3:#Create a conditional statement for the third option to exit the program
            print("Goodbye! Thank you for using the University Advisor.")
            break
        else:# To avoid the program breaking we say that of they input anything other than 1,2 or 3, print the text bellow
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()