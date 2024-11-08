# Portfolio Management
---
## Project Overview:

- In this project, the goal is to leverage time-series forecasting techniques to improve portfolio management strategies. With financial markets constantly fluctuating, accurately predicting future asset prices or other financial metrics is crucial for maximizing returns while minimizing risks. This project focuses on using historical financial data to build and evaluate various time-series forecasting models that can anticipate market trends.
---
## Project Objective:
1. **Data Collection and Preprocessing**
    - Gather and preprocess relevant historical financial data to create a clean dataset for model training and evaluation.
2. **Model Selection and Implementation**
    - Evaluate various time-series forecasting models, including ARIMA, SARIMA, and advanced neural network models like LSTM (Long Short-Term Memory).
3. **Forecase Future Market Trends**
    - Generate future forecasts for 6-12 months depending on the model.
    - Visualizing these forecasts together with previous historical data to look for long-term trends.
4. **Optimizing Portfolio Based on the Forecast**
---
## Project Directory Structure
- The repository is organized as follows:
    1. `github/workflows/`: Contains GitHub Actions for CI/CD and automated testing.
    2. `vscode/`: Development configuration for Visual Studio Code.
    3. `notebooks/`: Jupyter notebooks for data exploration, data visualization and model prototyping.
    6. `scripts/`: Scripts for data preprocessing, visualization, and model building.
    7. `tests/`: Unit tests for model integrity and data processing functions.
---
Table of Contents:
1. [Datasets](#datasets)
2. [Installation](#installation)
3. [License](#license)
4. [Contributing](#contributing)
---

## Datasets <a name="datasets"></a>

- The datasets used in this project are collected from the yfinance library (you can learn more about them here: https://pypi.org/project/yfinance/)
- The datasets collected are:
    1. Tesla historical stock prices (TSLA)
    2. Vanguard Total Bond Market ETF (BND)
    3. S&P 500 ETF (SPY)
- Each dataset includes:
    * `Date`: Trading day timestamp.
    * `Open`, `High`, `Low`, `Close`
    * `Volume`: The total number of shares/units traded each day.
    * `Stock Splits`: increasing the number of outstanding shares by dividing each existing share into a specified number of new shares
    * `Capital Gains` (specific for the Index bonds and S&P 500): profits or gains made from the sale of a capital asset

---
## Installation <a name="installation"></a>
Follow these steps to set up and run the project locally:
1. Clone the repository:

    ```bash
    git clone https://github.com/Leoul39/Portfolio-Management.git
    cd Porfolio-Management
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate   # For linux 
    venv/Scripts/activate # For Windows
    ```
3. install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

---
## License <a name="license"></a>
- This project is licensed under the MIT License. See the LICENSE file for details.
---
## Contributing <a name= 'contributing'></a>
- We welcome contributions to enhance the project:

    * Fork the repository and create a new branch.
    * Make changes with clear, descriptive commit messages.
    * Submit a pull request with a detailed explanation.