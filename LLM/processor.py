from LLM.gemini import answer
from LLM.blackbox import code
from LLM.phind import generate
from PIL.Image import open as openPIL
from requests import get
dir_agi = "\\Neuron_App"
import re
import time


def memoized_answer():
  cache = {}

  def inner_answer(question):
    if question not in cache:
      try:
        result = answer(question)
      except:
        result = generate(question)
      cache[question] = result
    return cache[question]

  return inner_answer


def image_generation(query):
    image_url = answer(query)
    response = get(image_url, stream=True)
    if response.status_code == 200:
        filepath = f"{dir_agi}\\images\\Neuron_Generated_Image.jpg"
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        generated_img = openPIL(f"{dir_agi}\\images\\Neuron_Generated_Image.jpg")
        generated_img.show()

    else:
        print(f"Sir I Failed to download image due to Bad Response")

def response(question):
  f = time.time()
  answer_of_the_question = memoized_answer()
  s = time.time()
  print("Time Taken: " + int(s - f))
  if re.search("Generate Code?", answer_of_the_question):
    return code(question)
  if not re.search("Generate Code?"): 
    return answer_of_the_question
  




