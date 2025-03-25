# Book Genre Prediction

## Overview
This project predicts the genre of a book based on its plot summary using a machine learning model. Users can input a book summary through a web interface, and the model will analyze the text and return the predicted genre.

## Dataset
Link : https://www.kaggle.com/datasets/athu1105/book-genre-prediction

## Features
- User-friendly web interface built with Flask and Bootstrap.
- Machine learning model for genre classification.
- Example metadata for better understanding of dataset structure.

## Installation
### Prerequisites
Ensure you have Python installed along with the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/book-genre-prediction.git
   cd book-genre-prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Flask app:
   ```bash
   python app.py
   ```
4. Open a web browser and go to `http://127.0.0.1:5000/` to use the application.

## Usage
1. Enter the summary of a book in the text box.
2. Click the **Predict** button.
3. The model will analyze the summary and display the predicted genre.

## Project Structure
```
book-genre-prediction/
│-- static/
│-- templates/
│   │-- index.html
│-- app.py
│-- model.pkl  # Trained machine learning model
│-- README.md
│-- requirements.txt
```

## Technologies Used
- **Python**
- **Flask** (for the web interface)
- **Scikit-learn** (for machine learning)



