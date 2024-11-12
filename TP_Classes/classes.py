class StudyAdvisor:
    def __init__(self, country, degree=None):
        self.country = country
        self.degree = degree
        self.universities = {
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
                "Business Administration": ["University of St. Gallen", "University of Zurich"]
            }
        }

    def get_degrees(self):
        return list(self.universities.get(self.country, {}).keys())

    def get_universities(self):
        return self.universities.get(self.country, {}).get(self.degree, "No universities found for this degree in the specified country.")

def main():
    country = input("Enter the country: ")
    advisor = StudyAdvisor(country)
    
    degrees = advisor.get_degrees()
    if not degrees:
        print(f"No degrees found for the country: {country}")
        return
    
    print(f"Available degrees in {country}: {', '.join(degrees)}")
    degree = input("Enter the degree: ")
    
    advisor.degree = degree
    universities = advisor.get_universities()
    print(f"Universities in {country} for {degree}: {universities}")

if __name__ == "__main__":
    main()