<div align="center">

# AI Data Science Project Backend - Text Analysis

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

---

### **Description**

This is the backend of the AI Data Science Project. The project is a web application that allows users to interact with various machine learning models that were trained on textual feedback from Polytech's alumni.

This project studies the textual feedback from former students of Polytech Montpellier Engineering School regarding their education and professional integration. This feedback is collected through surveys conducted at 6 months, 18 months, and 30 months after obtaining their diploma.

Many of the textual responses address feedback on the education, particularly the courses. Former students express their opinions on courses they find useful, useless, missing, and those that could have been beneficial or require strengthening for better professional integration. This project proposes to analyze these responses to determine, for each program, which courses are deemed useful, useless, etc.

---

[Installation and Execution](#installation) •
[Documentation](#documentation) •
[Contributions](#contributions)

**Please read the thourough documentation provided.**
</div>

## Features

- Summary graphs of the data
- Sentiment analysis
- K-means clustering
- Neural networks
- Word clouds

## Table of Contents

- [Installation](#installation)
  - [Setup](#setup)
- [Documentation](#documentation)
  - [Project Structure](#project-structure)
- [Contributions](#contributions)
  - [Authors](#authors)
  - [Version control](#version-control)

# Installation
<sup>[(Back to top)](#table-of-contents)</sup>

## Setup
<sup>[(Back to top)](#table-of-contents)</sup>

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

# Documentation
<sup>[(Back to top)](#table-of-contents)</sup>

Thourough documentation is provided.

## Project Structure
<sup>[(Back to top)](#table-of-contents)</sup>

- `neural_networks` contains the code for the neural network models and the trained models
- `kmeans` contains the code for the k-means clustering model
- `ETL` contains the code for the ETL process
- `app` contains the code for the interactive decison tool web application
- `new_data` contains the most recent data
- `old_data` contains the older data
- `formatted_data` contains the cleaned and formatted data
- `infos` contains the extracted information about the data
- `training_and_graph_data` contains the data used for training the models and the data used for the graphs

# Contributions
<sup>[(Back to top)](#table-of-contents)</sup>

## Authors
<sup>[(Back to top)](#table-of-contents)</sup>

- [**Alexandre Deloire**](https://github.com/alexdeloire)
- [**Remi Jorge**](https://github.com/RemiJorge)
- [**Jiayi He**](https://github.com/JiayiHE95)
- [**Charlene Morchipont**](https://github.com/charleneMrcp)

## Version control
<sup>[(Back to top)](#table-of-contents)</sup>

Git is used for version control.


