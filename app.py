from flask import Flask, render_template, request
from render import render_art

app = Flask(__name__)

@app.route('/')
def home():
    #Renders the main home page with the ASCII art form.
    return render_template('index.html')

@app.route('/ascii-art', methods=['POST'])
def handle_ascii_art():
    #Handles form submission, generates ASCII art, and displays it.
    
    user_text = request.form.get('text')
    selected_banner = request.form.get('banner')
    
    if not user_text:
        return "Error: No text provided!", 400

    try:

        ascii_result = render_art(user_text, selected_banner)
    except Exception as e:
        return f"An error occurred while generating art: {e}", 500
    
    print(f"Rendered text using banner: {selected_banner}")
    
    return f"<pre>{ascii_result}</pre><br><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(debug=True, port=8080)