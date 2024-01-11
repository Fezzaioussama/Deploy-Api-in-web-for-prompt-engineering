# Deploy-Api-in-web-for-prompt-engineering
# Unified Categories Generator

This repository provides a simple yet powerful solution for unifying catalogs related to different themes using OpenAI's GPT-3.5 Turbo model. The project consists of two main scripts: `app.py` and `client.py`.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Backend](#running-the-backend)
  - [Running the Frontend](#running-the-frontend)
- [Workflow](#workflow)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use the Unified Categories Generator, follow these installation steps:

1. Clone the repository:
   
```bash
git clone https://github.com/your-username/unified-categories-generator.git
cd unified-categories-generator
Certainly! Here's the README content provided in Markdown format:
```
## Install dependencies:

1. Clone the repository:

```bash
pip install -r requirements.txt
```
## Usage
Running the Backend

app.py is a Flask web application that serves as the backend for the Unified Categories Generator.

Ensure you have Flask and OpenAI Python SDK installed:

``` bash

pip install flask openai
```

## Running the Frontend

client.py is a Streamlit-based frontend for interacting with the Unified Categories Generator.

``` bash

streamlit run client.py
```
Ensure you have Streamlit and requests installed:

``` bash

pip install streamlit requests
```
## Workflow

    Enter catalog data for Été, Enfants, and Noël in the provided text areas.
    Click the "Generate Unified Categories" button to initiate the generation process.
    View the unified categories displayed on the Streamlit interface.
