from crewai import Agent, Task, Crew, Process

ai_researcher = Agent(
    role="researcher",
    goal="Researching trends in AI",
    verbose=True,
     backstory=(
        "You are a great resource for researching latest trends in AI"
    ),
)

ai_writer = Agent(
    role="Writer",
    goal="Writing in depth technical articles specifically on AI",
    verbose=True,
     backstory=(
        "You are at the edge of AI revolution"
    ),
)

research_task = Task(
    description=(
        "Write a 3 sentence topic outlines on the AI trends"
    ),
    expected_output='A comprehensive 3 sentences on latest AI trends.',
    agent = ai_researcher

)

writer_task = Task(
    description=(
        "Write an engaging article on latest of the AI trends"
    ),
    expected_output='A couple of pages of comprehensive article on latest AI trends.',
    agent = ai_writer,
    output_file='new-ai-blog-post.md'
)

crew = Crew(
    agents = [ai_researcher, ai_writer],
    tasks = [research_task, writer_task],
    process = Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

result = crew.kickoff()
print(result)