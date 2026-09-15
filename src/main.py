import fitz
import pyttsx3

pdf = fitz.open("Charles_Akinnurun_Resume.pdf")
text = "".join(page.get_text() for page in pdf)

engine = pyttsx3.init()
engine.set_property("rate", 150)

engine.save_to_file(text, "pdf_audio.mp3")

print("PDF -> Audio Done")