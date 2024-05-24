from crewai import Agent, Task, Crew, Process

quote_finder = Agent(
    role = "finder",
    goal = "finding Inspirational Quotes",
    backstory="You are great at collating and collecting inspirational quotes from famous scientists"
)

quote_writer = Agent(
    role = "writer",
    goal = "writing two paragraphs about life lessons that surround the inspirational quotes provided to you. You can explain the quotes too",
    backstory = "Your job is to write succint, very human-like quote explanations that would help depressed and downtrodden"
)


finder_task = Task(
    description = "Research and collect a quote from this century's famous scientists",
    expected_output = "A famous quote with the author citation attributed",
    agent = quote_finder
)
writer_task = Task(
    description = "Write an engaging two-paragraphs about the quote provided to you",
    expected_output = "The quote is explained in an inspirational way. Write it down in one or two paragraphs",
    agent = quote_writer,
    output_file = "quotes.md"
)

crew = Crew(
    agents = [quote_writer, quote_writer],
    tasks = [finder_task, writer_task],
    process = Process.sequential,
    memory = True,
    share_crew = True
)

result = crew.kickoff()
print(result)