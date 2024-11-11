# add aconstractor for the  cohort class
# add a method to the class that prints the cohort name and the total number of students
# create a new instance of the cohort class


class Cohort:
    def __init__(self, name, students):
        """Constructor for the Cohort class.
        
        Args:
            name (str): The name of the cohort.
            students (list): A list of students in the cohort.
        """
        self.name = name
        self.students = students

    def print_cohort_info(self):
        """Prints the cohort name and the total number of students."""
        total_students = len(self.students)
        print(f"Cohort Name: {self.name}")
        print(f"Total Number of Students: {total_students}")

# Create a new instance of the Cohort class
my_cohort = Cohort("Python Developers", ["Alice", "Bob", "Charlie", "Diana"])

# Call the method to print cohort information
my_cohort.print_cohort_info()