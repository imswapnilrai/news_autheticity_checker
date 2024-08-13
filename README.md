# News Authenticity Checker

## Overview

The News Authenticity Checker is a web application designed to assess the authenticity of news articles using Natural Language Processing (NLP) techniques and a Logistic Regression model. This tool helps users distinguish between 'Real News' and 'Super Fake' news content based on textual analysis.

## Features

- **Text Input:** Users can paste news content into a textarea to evaluate its authenticity.
- **Prediction Result:** Displays the prediction result indicating whether the news is 'Real News' or 'Super Fake!!!'.
- **Model:** Utilizes a Logistic Regression model trained on a dataset of labeled news articles.
- **Preprocessing:** Includes text preprocessing steps such as stemming and stopwords removal.

## Screenshot

Below is a screenshot of the News Authenticity Checker web application:
![Screenshot](https://github.com/user-attachments/assets/16d4ffc5-d56d-4d40-ae5c-adf3aaf74474)


## How It Works

1. **Data Collection:** Collects a dataset of news articles labeled as either real or fake.
2. **Preprocessing:** Cleans and normalizes the text using techniques like stemming and removing stopwords.
3. **Feature Extraction:** Converts text data into numerical features using the Tf-IDF Vectorizer.
4. **Model Training:** Trains a Logistic Regression model using the vectorized features to classify news content.
5. **Deployment:** Deploys the model in a Flask web application where users can input news content and receive predictions.

## Getting Started

To run the News Authenticity Checker locally, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/imswapnilrai/news-authenticity-checker.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd news-authenticity-checker
    ```

3. **Set Up a Virtual Environment (Optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the Required Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask Application:**

    ```bash
    flask run
    ```

6. **Access the Application:**

    Open your web browser and go to `http://127.0.0.1:5000` to use the News Authenticity Checker.

## Technologies Used

- **Python**
- **Flask**: Web framework for deploying the application.
- **Natural Language Processing (NLP)**: Techniques for analyzing text data.
- **Logistic Regression**: Statistical model for classification.
- **Tf-IDF Vectorization**: Method for converting text into numerical features.
- **HTML/CSS**: For creating and styling the web interface.

## Skills Demonstrated

- **Data Collection and Preprocessing:** Handling and preparing text data for analysis.
- **Feature Engineering:** Using Tf-IDF Vectorizer to transform text data.
- **Model Training and Evaluation:** Building and evaluating a Logistic Regression model.
- **Web Development:** Creating a user-friendly web application with Flask.

## Connect with Me

- **[LeetCode](https://leetcode.com/u/swapnilrai80/)**
- **[GitHub](https://github.com/imswapnilrai)**
- **[LinkedIn](https://www.linkedin.com/in/swapnil-rai-1bb124217/)**
- **[Download Resume](static/Swapnil%20Rai%20Resume-%20DA.pdf)**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **NLTK (Natural Language Toolkit):** For text preprocessing and analysis.
- **Scikit-learn:** For implementing the Logistic Regression model.
