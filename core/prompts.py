translate_text_prompt = """
    Hãy dịch văn bản sau sang {language}.
    Đối với các từ khóa hoặc các từ chuyên ngành, hãy giữ nguyên chúng và thay vào đó thêm chú thích ở bên dưới.
    Nếu không thể dịch được, hãy ghi "Không thể dịch được" bằng ngôn ngữ {annotation_language}.
    Nếu văn bản bên dưới trùng với ngôn ngữ đích, hãy tối ưu nội dung nhưng vẫn chú thích từ khóa hoặc từ chuyên ngành.
    LƯU Ý QUAN TRỌNG: hãy dùng ngôn ngữ {annotation_language} để chú thích.
    Văn bản như sau:
    ```
    {text}
    ```

"""

def get_prompt_for_translate_text(text, language, annotation_language):
    return translate_text_prompt.format(text=text, language=language, annotation_language=annotation_language)