from crewai import Task

def create_tasks(planner, writer, editor):
    """Create the CrewAI tasks"""
    plan = Task(
        description=(
            "1. Prioritize the latest trends, key players, and noteworthy news on {topic}.\n"
            "2. Identify the target audience, considering their interests and pain points.\n"
            "3. Develop a detailed content outline including the introduction, key points, and a call to action.\n"
            "4. Include SEO keywords and relevant data or sources."
        ),
        expected_output="A comprehensive content plan document with an outline, audience analysis, SEO keywords, and relevant data or sources",
        agent=planner
    )
    
    write = Task(
        description=(
            "1. Use the content plan to craft a compelling blog post on {topic}.\n"
            "2. Incorporate SEO keywords naturally.\n"
            "3. Sections/Subtitles are properly named in an engaging manner.\n"
            "4. Ensure the post is structured with an engaging introduction, insightful body, and summarizing conclusion.\n"
            "5. Proofread for grammatical errors and alignment with the brand's voice."
        ),
        expected_output="A well-written blog post in markdown format, ready for publication, each section is properly formatted having 2 to 3 paragraphs with headings and subheadings.",
        agent=writer
    )
    
    edit = Task(
        description=(
            "Proofread the blog post for grammatical errors, punctuation, and formatting issues.\n"
            "Ensure the post is aligned with the brand's voice and tone.\n"
            "Check for consistency in style, tone, and structure.\n"
            "Provide detailed feedback for improvements."
        ),
        expected_output="A well-edited blog post with no grammatical errors, punctuation issues, and formatting inconsistencies.",
        agent=editor
    )
    
    return plan, write, edit