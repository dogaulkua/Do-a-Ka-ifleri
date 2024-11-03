# Doğa Kaşifleri (Nature Explorers)

**Doğa Kaşifleri** is an innovative project designed to engage children in nature exploration through the integration of Natural Language Processing (NLP) and Fuzzy Logic systems. This project aims to inspire children to connect with nature, enhancing their autonomy and curiosity through personalized task suggestions based on their interests.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
- [API Endpoints](#api-endpoints)
- [Backend Code](#backend-code)
- [Frontend Code](#frontend-code)
- [Contributing](#contributing)
- [License](#license)

## Features
- **NLP Model Integration**: Understands and processes children’s queries related to nature.
- **Fuzzy Logic System**: Provides personalized task suggestions based on interest levels.
- **Flask API**: RESTful API that facilitates interaction between users and the system.
- **User-Friendly Interface**: Simple and intuitive frontend for children to engage with.

## Technologies Used
- **Python**: Main programming language.
- **Flask**: Web framework for building the API.
- **Hugging Face Transformers**: For NLP capabilities.
- **scikit-fuzzy**: For implementing fuzzy logic.
- **HTML/CSS/JavaScript**: Frontend technologies.

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/nature-explorers.git
   cd nature-explorers
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## How to Use
- Open your web browser and navigate to `http://127.0.0.1:5000`.
- Enter a nature-related query in the input field.
- Adjust the interest level slider to personalize your experience.
- Submit your query to receive tailored task suggestions.

## API Endpoints
- **POST /suggest_task**
  - **Request Body**:
    ```json
    {
      "interestLevel": 0.8,
      "query": "Tell me about this plant."
    }
    ```
  - **Response**:
    ```json
    {
      "suggestedTask": "Observe the nearest plant and take notes.",
      "nlpResponse": "This plant is known for its medicinal properties."
    }
    ```

## Backend Code

Below is the sample code for the Flask backend using Python:

```python
# app.py
from flask import Flask, request, jsonify
from transformers import pipeline
import skfuzzy as fuzz
import numpy as np

app = Flask(__name__)

# Load NLP model
nlp_model = pipeline("question-answering")

# Fuzzy logic setup
def fuzzy_task_suggestion(interest_level):
    # Example fuzzy logic for task suggestion
    x_interest = np.arange(0, 1.1, 0.1)
    x_task = np.arange(0, 101, 1)

    # Membership functions
    interest_low = fuzz.trimf(x_interest, [0, 0, 0.5])
    interest_medium = fuzz.trimf(x_interest, [0, 0.5, 1])
    interest_high = fuzz.trimf(x_interest, [0.5, 1, 1])

    # Suggestion levels based on interest
    task_low = fuzz.interp_membership(x_interest, interest_low, interest_level)
    task_medium = fuzz.interp_membership(x_interest, interest_medium, interest_level)
    task_high = fuzz.interp_membership(x_interest, interest_high, interest_level)

    # Example task suggestions
    if task_high:
        return "Go on a nature walk and document what you see!"
    elif task_medium:
        return "Draw your favorite plant."
    else:
        return "Read a book about local wildlife."

@app.route('/suggest_task', methods=['POST'])
def suggest_task():
    data = request.json
    interest_level = data['interestLevel']
    query = data['query']
    
    # Process the query
    nlp_response = nlp_model(question=query, context="Nature is full of wonders.")
    
    # Get task suggestion
    suggested_task = fuzzy_task_suggestion(interest_level)

    return jsonify({
        "suggestedTask": suggested_task,
        "nlpResponse": nlp_response['answer']
    })

if __name__ == '__main__':
    app.run(debug=True)
```

## Frontend Code

Here’s an example of the HTML and JavaScript for the frontend:

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doğa Kaşifleri</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { max-width: 600px; margin: auto; }
        input, button { padding: 10px; margin: 5px; width: 100%; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Doğa Kaşifleri</h1>
        <input type="text" id="query" placeholder="Ask about nature...">
        <input type="range" id="interestLevel" min="0" max="1" step="0.1" value="0.5">
        <button onclick="submitQuery()">Submit</button>
        <h2>Suggested Task:</h2>
        <p id="taskSuggestion"></p>
    </div>
    <script>
        async function submitQuery() {
            const query = document.getElementById('query').value;
            const interestLevel = document.getElementById('interestLevel').value;

            const response = await fetch('/suggest_task', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ interestLevel, query })
            });

            const data = await response.json();
            document.getElementById('taskSuggestion').innerText = data.suggestedTask;
        }
    </script>
</body>
</html>
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add a feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Create a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
