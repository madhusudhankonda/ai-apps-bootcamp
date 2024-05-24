from crewai import Agent, Task, Crew, Process

designer = Agent(
    role = "designer",
    goal = "Design UML diagrams in PlantUML for a given requirement",
    backstory = "You are an application architect who creates designs such as UML class diagrams"
)

db_modeller = Agent(
    role = "modeller",
    goal = "Design Data Model for the given requirements",
    backstory = "You are a database architect who declares and creates data model"
)

developer = Agent(
    role = "developer",
    goal = "Writing code in Java",
    backstory=("You are a Java expert")
)

tester = Agent(
    role = "tester",
    goal = "Writing JUnit tests",
    backstory = ("Your job is to write JUnit Tests")
)

design_task = Task(
    description = "An Employee has a firstname, lastname and age.",
    expected_output = "Design a class diagram for the given Employee class with the given attributes. The class diagram should be created using PlatUML",
    agent = designer, 
    output_file="plantuml.md"
)

modeller_task = Task(
    description = "Model Employee Data Model",
    expected_output = "Design a ERD data model for the given Employee class with the given attributes. The class diagram should be created using PlatUML",
    agent = designer, 
    output_file="plantuml-dm.md"
)

dev_task = Task(
    description = "An Employee has a firstname, lastname and age.",
    expected_output = "Write the Employee class with the given attributes. The class name should be produced under src folder with a name Employee.java",
    agent = developer,
    output_file = "Employee.java"
)

test_task = Task(
    description = "Write two JUnit test cases for the given class",
    expected_output = "Two Junit tests, one a positive and one and a negative junit based test cases to be written for the given class",
    agent = tester,
    output_file = "EmployeeTest.java"
)

crew = Crew(
    agents = [designer, db_modeller, developer, tester],
    tasks = [design_task, modeller_task, dev_task, test_task],
    process = Process.sequential,
    memory = True,
    share_crew = True,
    verbose = True
)

result = crew.kickoff()
print(result)