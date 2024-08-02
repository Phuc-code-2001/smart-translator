import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

from utils.consts import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

def get_model(model_name):
    return genai.GenerativeModel(model_name)

list_model_name = [
    model.name 
    for model in genai.list_models() 
    if "generateContent" in model.supported_generation_methods and "latest" in model.name and "vision" not in model.name
]

safety_settings = {
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
}