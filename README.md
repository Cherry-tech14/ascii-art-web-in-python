# ASCII Art Web Generator in Python

A lightweight, modular web application built with **Flask** that translates plain text into multi-line graphical ASCII art using custom banner styles (`standard`, `shadow`, and `thinkertoy`).


##  Features
- **Web-based GUI**: Clean HTML interface with text input and radio-button font selection.
- **Modular Architecture**: Clean separation of concerns across `app.py` (web routing), `render.py` (stitching logic), and `banner.py` (file parsing).
- **Multiple Font Styles**: Supports `standard`, `shadow`, and `thinkertoy` banner configurations.
- **Browser-Friendly Output**: Uses preformatted text tags (`<pre>`) to preserve character spacing and alignment.



## Project Structure

ascii-art-web-in-python/
│
├── app.py              # Flask server and route handlers
├── render.py           # Core text-stitching and formatting logic
├── banner.py           # Banner file parser and character dictionary loader
├── standard.txt        # Standard font banner data file
├── shadow.txt          # Shadow font banner data file
├── thinkertoy.txt      # Thinkertoy font banner data file
├── requirements.txt    # Python project dependencies
├── .gitignore          # Files and folders excluded from Git tracking
└── templates/
    └── index.html      # Frontend HTML form interface

## Getting Started Locally

### Clone the Repository
git clone [https://github.com/your-username/ascii-art-web-in-python.git](https://github.com/your-username/ascii-art-web-in-python.git)
cd ascii-art-web-in-python

### Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate

### Install Dependencies
python3 -m pip install -r requirements.txt

### Run the Flask Application

python3 app.py

### Open in your Browser
http://127.0.0.1:8080/

### Tech Stack
* python 3
* Flask
* HTML