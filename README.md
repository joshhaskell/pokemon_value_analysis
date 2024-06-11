# Pokémon Value Analysis

This project analyzes the value of Pokémon cards using data from the Pokémon TCG API. It includes data gathering, cleaning, exploratory data analysis (EDA), and visualization of key findings.

## Setup Instructions

### Environment Setup and Install Dependencies

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/pokemon_value_analysis.git
    cd pokemon_value_analysis
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up your API key:**
    - Create a `.env` file in the root directory of the project.
    - Add your Pokémon TCG API key to the `.env` file:
        ```plaintext
        pokemon_tcg_api_key=YOUR_API_KEY_HERE
        ```
    - You can obtain an API key from [Pokémon TCG Developer Portal](https://dev.pokemontcg.io/).

## Data Collection

The `get_data.py` script handles data collection from the Pokémon TCG API. It fetches data, combines it, and saves it as a CSV file in the `data` folder.

## Utilities

The `utilities` folder contains various functions for data aggregation and plotting. These utility functions are used throughout the project for processing and visualizing the data.

## Exploratory Data Analysis (EDA)

The main analysis was conducted in the `EDA.ipynb` Jupyter notebook. This notebook includes:
- Data cleaning and preparation
- Exploratory data analysis to understand the distribution and relationships in the data
- Initial visualizations to identify key patterns and insights

## Presentation

The `presentation.ipynb` Jupyter notebook provides an overview and main findings of the analysis. It is designed to present the insights in a concise and visually appealing format.

## Usage

1. **Run Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```

2. **Open `EDA.ipynb` for detailed exploratory data analysis.**

3. **Open `presentation.ipynb` for an overview of the main findings.**