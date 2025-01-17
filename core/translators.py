from core.prompts import get_prompt_for_translate_text, get_prompt_for_translate_words
from core.llms import get_model, safety_settings

def stream_text_generator(stream_response):
    def generator():
        for chunk in stream_response:
            if chunk.candidates[0].content:
                for chr in chunk.candidates[0].content.parts[0].text:
                    yield chr

    return generator

def translate_text(model_name, text, language, annotation_language, stream=False):
    """Translate text to target language."""
    model = get_model(model_name)
    prompt = get_prompt_for_translate_text(text, language, annotation_language)
    response = model.generate_content(prompt, stream=stream, safety_settings=safety_settings)
    if not stream:
        try:
            return response.candidates[0].content.parts[0].text
        except IndexError:
            return "An error occurred while translating the text."
        
    return stream_text_generator(response)

def translate_words(model_name, text, language, annotation_language, stream=False):
    """Translate words to target language."""
    model = get_model(model_name)
    prompt = get_prompt_for_translate_words(text, language, annotation_language)
    response = model.generate_content(prompt, stream=stream, safety_settings=safety_settings)

    if not stream:
        try:
            return response.candidates[0].content.parts[0].text
        except IndexError:
            return "An error occurred while translating the text."

    return stream_text_generator(response)