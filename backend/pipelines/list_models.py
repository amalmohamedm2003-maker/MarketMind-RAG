import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAj3VwtUhug0Ouj55zMgHmqFWb67cnJEOg")

for m in genai.list_models():
    print(m.name, "->", m.supported_generation_methods)
