# PDF to Audio Converter

A simple Python project that extracts text from a PDF document and converts the extracted text into an audio file using text-to-speech.

This project can be useful for listening to resumes, documents, notes, or other text-based PDF files without having to read them manually.

## Features

* Extracts text from PDF files
* Converts extracted text to speech
* Saves the generated speech as an audio file
* Adjustable speech rate
* Simple and lightweight Python implementation

## Technologies Used

* **Python**
* **PyMuPDF (fitz)** — PDF text extraction
* **pyttsx3** — Text-to-speech conversion

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/pdf-to-audio.git
cd pdf-to-audio
```

Install the required dependencies:

```bash
pip install PyMuPDF pyttsx3
```

## Project Structure

```text
pdf-to-audio/
│
├── main.py
├── Charles_Akinnurun_Resume.pdf
├── pdf_audio.mp3
└── README.md
```

## How It Works

The project follows three main steps:

1. Opens the PDF using **PyMuPDF**.
2. Extracts and combines the text from each page.
3. Uses **pyttsx3** to convert the extracted text into an MP3 audio file.

### Example

```python
import fitz
import pyttsx3

pdf = fitz.open("Charles_Akinnurun_Resume.pdf")

text = "".join(page.get_text() for page in pdf)

engine = pyttsx3.init()

engine.set_property("rate", 150)

engine.save_to_file(text, "pdf_audio.mp3")

print("PDF -> Audio Done")
```

## Usage

Place the PDF you want to convert in the project directory and update the filename:

```python
pdf = fitz.open("your_document.pdf")
```

Run the Python script:

```bash
python main.py
```

After execution, the generated audio file will be saved as:

```text
pdf_audio.mp3
```

## Customizing Speech Rate

You can change the speaking speed using:

```python
engine.set_property("rate", 150)
```

For example:

```python
engine.set_property("rate", 180)
```

A higher value generally produces faster speech, while a lower value produces slower speech.

## Use Cases

* Listening to resumes
* Converting study notes into audio
* Accessibility for text-based documents
* Listening to reports and documentation
* Reviewing documents while multitasking

## Future Improvements

* Add a graphical user interface
* Allow users to upload PDFs
* Support multiple PDF files
* Add voice selection
* Add different output audio formats
* Add command-line arguments for input/output files
* Add support for selecting specific PDF pages

## License

This project is open source and available under the MIT License.
