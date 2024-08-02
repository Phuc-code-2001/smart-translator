translate_text_prompt = """
    Translate the following text into {language}.
    For keywords or technical terms, keep them as they are and add annotations below.
    If a word cannot be translated, write "Cannot be translated" in {annotation_language}.
    If the text below is in the target language, optimize the content but still annotate keywords or technical terms.
    IMPORTANT NOTES:
        1. Use {annotation_language} for annotations.
        2. If the text contains sensitive words, replace them with non-sensitive synonyms, translate them, and issue a warning.
    The text is as follows:
    {text}
"""

def get_prompt_for_translate_text(text, language, annotation_language):
    return translate_text_prompt.format(text=text, language=language, annotation_language=annotation_language)


translate_words_prompt = """
    Translate the following text word by word or phrase by phrase into {language}.
    For each word, provide its usage contexts and construct sentences (in the same language as the input text) demonstrating its usage.
    If possible, analyze the prefix, suffix, and root of the word.
    Finally, introduce the etymology of the word and create a table listing words that share the same root.
    IMPORTANT NOTES:
        1. Use {annotation_language} for annotations.
        2. If the text contains sensitive words, replace them with non-sensitive synonyms, translate them, and issue a warning.
    The text is as follows:
    {text}
"""

def get_prompt_for_translate_words(text, language, annotation_language):
    return translate_words_prompt.format(text=text, language=language, annotation_language=annotation_language)