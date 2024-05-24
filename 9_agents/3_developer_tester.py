from crewai import Agent, Task, Crew, Process

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
    agents = [developer, tester],
    tasks = [dev_task, test_task],
    process = Process.sequential,
    memory = True,
    share_crew = True
)

result = crew.kickoff()
print(result)