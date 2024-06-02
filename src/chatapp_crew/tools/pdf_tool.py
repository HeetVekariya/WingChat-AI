from crewai_tools import PDFSearchTool

# Initialize the PDF Search Tool
pdf_search_tool = PDFSearchTool()

# Search for the text in the PDF
tool = PDFSearchTool(
    pdf="src\chatapp_crew\data\\blood test report.pdf",
    config=dict(
        llm=dict(
            provider="ollama",
            config=dict(
                model="llama2"
            ),
        ),
        embedder=dict(
            provider="google", 
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
            ),
        ),
    )
)