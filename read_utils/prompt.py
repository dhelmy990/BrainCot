
basic_prompt = """
    I want you to summarize this research paper in your own voice, creating a concise and engaging 2-minute reel that focuses on being informative. Your summary should highlight the key points, methodology, findings, and significance of the research.

    Instructions:
    Preface the Summary: Start with "RELATED:" followed by a list of all key concepts, methodologies, and terms from the paper in bullet-point notation.

    Begin the Summary: Start the actual summary with "BEGIN:" and ensure it is clear, concise, and suitable for a 2-minute presentation.

    Tone and Style: Use a professional yet accessible tone, ensuring the summary is easy to understand for a general audience while retaining the technical depth of the paper.

    If you can't do this, explain why.
    """

image_prompt = """
    I want you to summarize a research paper in your own voice, creating a concise and engaging 2-minute reel that focuses on being informative. Your summary should highlight the key points, methodology, findings, and significance of the research.

    Instructions:
    Preface the Summary: Start with "RELATED:" followed by a list of all key concepts, methodologies, and terms from the paper in bullet-point notation.

    Begin the Summary: Start the actual summary with "BEGIN:" and ensure it is clear, concise, and suitable for a 2-minute presentation.

    Incorporate Figures: If figures from the paper would enhance the summary, signal when they should appear and disappear on screen using the following format:

    To indicate when a figure should appear:
    [START {page_figure_appears}_{zero_indexed_index_of_figure_on_page}]

    To indicate when a figure should be removed:
    [END {page_figure_appears}_{zero_indexed_index_of_figure_on_page}]

    Tone and Style: Use a professional yet accessible tone, ensuring the summary is easy to understand for a general audience while retaining the technical depth of the paper.

    If you can't do this, explain why.
    """