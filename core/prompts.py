translate_text_prompt = """
    Hãy dịch văn bản sau sang {language}.
    Đối với các từ khóa hoặc các từ chuyên ngành, hãy giữ nguyên chúng và thay vào đó thêm chú thích ở bên dưới.
    Nếu không thể dịch được, hãy ghi "Không thể dịch được" bằng ngôn ngữ {annotation_language}.
    Nếu văn bản bên dưới trùng với ngôn ngữ đích, hãy tối ưu nội dung nhưng vẫn chú thích từ khóa hoặc từ chuyên ngành.
    LƯU Ý QUAN TRỌNG: 
        1. Đối với chú thích dùng ngôn ngữ {annotation_language}
        2. Nếu văn bản chứa từ ngữ nhạy cảm, hãy thay thế chúng bằng từ khác không nhạy cảm nhưng đồng nghĩa, dịch và đưa ra cảnh báo.
    Văn bản như sau:
    ```
    {text}
    ```

"""

def get_prompt_for_translate_text(text, language, annotation_language):
    return translate_text_prompt.format(text=text, language=language, annotation_language=annotation_language)


translate_words_prompt = """
    Hãy dịch văn bản sau theo từng từ hoặc cụm từ sang {language}.
    Với mỗi từ, cho biết các tình huống sử dụng và đặt câu (bằng ngôn ngữ trùng với ngôn ngữ đầu vào).
    Nếu có thể, hãy phân tích tiền tố, hậu tố, gốc từ của từ đã cho.
    Sau cùng, giới thiệu về nguồn gốc từ và tạo một bảng gồm các từ có chung gốc từ với từ đó.
    LƯU Ý QUAN TRỌNG: 
        1. Đối với chú thích dùng ngôn ngữ {annotation_language}
        2. Nếu văn bản chứa từ ngữ nhạy cảm, hãy thay thế chúng bằng từ khác không nhạy cảm nhưng đồng nghĩa, dịch và đưa ra cảnh báo.
    Văn bản như sau:
    {text}
"""

def get_prompt_for_translate_words(text, language, annotation_language):
    return translate_words_prompt.format(text=text, language=language, annotation_language=annotation_language)