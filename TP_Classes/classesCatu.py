class StudyAdvisor:
    universities_data = {
        "Spain": {
                "Computer Science": ["University of Barcelona", "Polytechnic University of Madrid", "University of Valencia"],
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

    def __init__(self, country=None, degree=None):
        self.country = country
        self.degree = degree

    def get_degrees(self):
        if self.country:
            return list(self.universities_data.get(self.country, {}).keys())
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

    def display_options(self):
        universities = self.get_universities()
        if isinstance(universities, list):
            print(f"Universities for {self.degree} degree:")
            for university in universities:
                print(f"    - {university}")
        else:
            print(universities)

def main():
    print('-------------')
    print('STUDY ADVISOR')
    print('-------------')
    
    while True:
        options = [
            '---------------------------------',
            '[1] Search by Country and Degree.',
            '[2] Search by Degree.',
            '[3] Exit.',
            '---------------------------------'
        ]
        for option in options:
            print(option)

        option = int(input("Please select an option:\t"))

        if option == 1:
            print('Available Countries:')
            for country in StudyAdvisor.universities_data:
                print(f"    - {country}")

            country = input("Please enter the country you'd like to study in:\t").strip()
            country = country.title()

            if country not in StudyAdvisor.universities_data:
                print("Sorry, we don't have information for that country.")
                return

            degrees = StudyAdvisor(country).get_degrees()
            print("Available degrees in", country)
            print("------------------------------")
            for degree in degrees:
                print(f"    - {degree}")
            print("------------------------------")
            
            degree = input("Please enter the degree you'd like to study:\t").strip()
            degree = degree.title()

            if degree not in StudyAdvisor.universities_data[country]:
                print("Sorry, we don't have information for that degree in", country)
                return

            advisor = StudyAdvisor(country, degree)
            advisor.display_options()
        
        elif option == 2:
            degree = input("Please enter the degree you'd like to study:\t").strip()
            degree = degree.title()

            advisor = StudyAdvisor(degree=degree)
            advisor.display_options()
        
        elif option == 3:
            print("Goodbye! Thank you for using the Study Advisor.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()