from dotenv import load_dotenv, find_dotenv
import os
try:
    load_dotenv(find_dotenv())
except:
    pass

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

class APP_CONSTANTS:
    languages = [
        "English", "Vietnamese", "Chinese", "Korean", 
        "French", "German", "Spanish", "Italian", "Portuguese", 
        "Dutch", "Russian", "Arabic", "Turkish", "Polish", "Romanian", 
        "Hungarian", "Czech", "Slovak", "Bulgarian", "Greek", "Finnish", 
        "Swedish", "Danish", "Norwegian", "Lithuanian", "Latvian", "Estonian", 
        "Ukrainian", "Belarusian", "Georgian", "Armenian", "Azerbaijani", "Kazakh", 
        "Uzbek", "Tajik", "Turkmen", "Kyrgyz", "Mongolian", "Hindi", "Bengali", "Tamil", 
        "Telugu", "Urdu", "Gujarati", "Marathi", "Punjabi", "Kannada", "Malayalam", "Odia", 
        "Assamese", "Nepali", "Sinhala", "Burmese", "Khmer", "Lao", "Thai", "Burmese", "Khmer", 
        "Lao", "Thai", "Indonesian", "Filipino", "Malay", "Javanese", "Sundanese", 
        "Hausa", "Yoruba", "Igbo", "Kinyarwanda", "Kirundi", "Swahili", "Amharic", "Oromo"
    ]