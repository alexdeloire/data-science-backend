# Data Science Project - Text Analysis

This project studies the textual feedback from former students of Polytech Montpellier Engineering School regarding their education and professional integration. This feedback is collected through surveys conducted at 6 months, 18 months, and 30 months after obtaining their diploma.

Many of the textual responses address feedback on the education, particularly the courses. Former students express their opinions on courses they find useful, useless, missing, and those that could have been beneficial or require strengthening for better professional integration. This project proposes to analyze these responses to determine, for each program, which courses are deemed useful, useless, etc.

# Project Structure

- `neural_networks` contains the code for the neural network models and the trained models
- `kmeans` contains the code for the k-means clustering model
- `ETL` contains the code for the ETL process
- `app` contains the code for the interactive decison tool web application
- `new_data` contains the most recent data
- `old_data` contains the older data
- `formatted_data` contains the cleaned and formatted data
- `infos` contains the extracted information about the data
- `training_and_graph_data` contains the data used for training the models and the data used for the graphs


# Setup

Create virtual environment:

```bash
python3 -m venv env
```

Activate virtual environment (Linux):

```bash
source env/bin/activate
```

Activate virtual environment (Windows):

```bash
.\env\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python main.py
```