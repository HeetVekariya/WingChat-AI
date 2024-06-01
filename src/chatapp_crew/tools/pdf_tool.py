from crewai_tools import PDFSearchTool

# Initialize the PDF Search Tool
pdf_search_tool = PDFSearchTool()

# Search for the text in the PDF
tool = PDFSearchTool(
    pdf="src\chatapp_crew\data\\blood test report.pdf",
    config=dict(
        llm=dict(
            provider="llama3", # or google, openai, anthropic, llama2, ...
            config=dict(
                #model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)