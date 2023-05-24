from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()

def print_summary(birth,death,summary,scientistName):
    print("\n\nScientist Name: ",scientistName)
    print("Birth: ",birth)
    print("Death: ",death)
    print("Age: ",death-birth)
    print("Summary : ",summary)
    print("\n\n\n")
    
    
    
def search(scientistName):
    # for scientist in SCIENTISTS:
    robot.search_scientist_by_name(scientistName)
    birth_year=robot.get_birth_date()
    death_year=robot.get_death_date()
    age=death_year-birth_year
    summary=robot.get_summary()
    print_summary(birth_year,death_year,summary,scientistName)
    

def main():
    introduce_yourself()
    robot.open_webpage("https://www.wikipedia.org")
    for scientist in SCIENTISTS:
        search(scientist)


if __name__ == "__main__":
    main()
