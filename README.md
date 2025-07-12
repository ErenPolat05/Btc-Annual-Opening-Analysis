# BTC Analysis Project

This project analyzes and visualizes the opening price of Bitcoin on January 1st of each year.

## Features
- Reads Bitcoin price data from a CSV file.
- Filters for the opening price on January 1st each year.
- Plots the prices and years on a line graph.
- Displays the actual price label on each data point.
- Saves the graph as a PNG file.

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib

## Installation
Install the required libraries:
```bash
pip install pandas numpy matplotlib
```

## Usage
1. Place the `BTC.csv` file in the `BtcAnalysisProject` folder.
2. Run the `main.py` file:
   ```bash
   python main.py
   ```
3. The graph will be saved as `BtcAnalysisProject/Btc_Grafic.png`.

## Example Graph
![BTC Graph](Btc_Grafic.png)

## License
This project is licensed under the MIT License.
