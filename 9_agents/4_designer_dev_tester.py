from crewai import Agent, Task, Crew, Process

designer = Agent(
    role = "designer",
    goal = "Design UML diagrams in PlantUML for a given requirement",
    backstory = "You are an application architect who creates designs such as UML class diagrams"
)

developer = Agent(
    role = "developer",
    goal = "Write code in Java",
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
    agent = developer
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
    agents = [designer, developer, tester],
    tasks = [design_task, dev_task, test_task],
    process = Process.sequential,
    memory = True,
    share_crew = True
)

result = crew.kickoff()
print(result)