import google.generativeai as genai
from utils.consts import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

def get_model(model_name):
    return genai.GenerativeModel(model_name)

list_model_name = [
    model.name 
    for model in genai.list_models() 
    if "generateContent" in model.supported_generation_methods and "latest" in model.name and "vision" not in model.name
]