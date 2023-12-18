# Reddit Data Analysis Project

This project fetches data from Reddit using the Reddit API, performs analysis, and generates visualizations based on the data. It covers various aspects such as data retrieval, data cleaning, visualization, and additional analysis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [comments](#comments)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MohamadAshrafSalama/reddit-data-analysis.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have Python installed on your system.

2. Set up your Reddit API credentials in a file named `secrets.txt`. Follow the format:

    ```plaintext
    client_id=your_client_id
    client_secret=your_client_secret
    reddit_username=your_reddit_username
    reddit_password=your_reddit_password
    ```

3. Run the main script:

    ```bash
    python reddit_script.py
    ```

4. Follow the prompts to enter the start date, end date, and subreddit.

5. Check the output CSV file in the project directory (e.g., `vim.csv`).

## Dependencies

- requests==2.31.0
- pandas==1.5.3
- matplotlib==3.7.1
- seaborn==0.12.2
- wordcloud==1.9.3
- textblob==0.17.1

## Contributing

If you'd like to contribute to the project, feel free to fork the repository and submit a pull request.
## comments
The test file contains all my experiments. The "reddit2.0" file holds the final code used to extract data and apply data analytics.
Everything is then consolidated into a script along with its requirements and secret keys.
