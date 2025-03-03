
basic_prompt = """
    What I want is to send a PDF file of a research paper. I want to supply a persona for you to talk like (like {persona}).
    I want you to create a 2-minute reel summarizing the content of the paper.

    Having read the paper, if figures from the paper would be useful, I would like you to signal that the image should appear on screen with 
    [START {page_figure_appears}_{zero_indexed_index_of_figure_on_page}], and end with the same tag but the word START replaced with END.

    I want you to also return the key terms that were discussed in the paper.
    """