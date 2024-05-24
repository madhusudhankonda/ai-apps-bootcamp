from crewai import Agent, Task, Crew, Process

ba = Agent(
    role = "business_analyst",
    goal = "Writing a Story for a feature",
    backstory="You are a Business Analyst in an IT team, who would be writing technical stories with a format: 'As a [persona], I [want to], [so that].'"
)

ba_task = Task(
    description = "An Employee login feature",
    expected_output = "Write a user story for a login feature of an Employee being built in the webapp. Follow the story format as: 'As a [persona], I [want to], [so that].'. Make sure you write the details covering the various scenarios",
    agent = ba,
    output_file = "user-story.md"
)

crew = Crew(
    agents = [ba],
    tasks = [ba_task],
    process = Process.sequential,
    memory = True,
    share_crew = True,
    verbose = True
)

result = crew.kickoff()
print(result)