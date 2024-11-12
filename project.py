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

    def __init__(self, country, degree=None):
        self.country = country
        self.degree = degree

    def get_degrees(self):
        return list(self.universities_data.get(self.country, {}).keys())

    def get_universities(self):
        return self.universities_data.get(self.country, {}).get(self.degree, "No universities found for this degree in the specified country.")