from LLM.gemini import answer
from LLM.blackbox import code
from LLM.phind import generate
from LLM.wolframalpha import stem_answers
from PIL.Image import open as openPIL
from requests import get
import settings
import re


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
        filepath = f"{settings.dir_agi}\\images\\Neuron_Generated_Image.jpg"
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        generated_img = openPIL(f"{settings.dir_agi}\\images\\Neuron_Generated_Image.jpg")
        generated_img.show()

    else:
        print(f"Sir I Failed to download image due to Bad Response")

def response(question):
  answer_of_the_question = memoized_answer()
  if re.search("Generate Code?", answer_of_the_question):
    code(question)
  if re.search("Stem-Based-Question", answer_of_the_question):
    stem_answers(question)
  if not re.search("Stem-Based-Question" or "Generate Code?"):
    return answer_of_the_question


