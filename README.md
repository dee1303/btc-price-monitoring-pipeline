# Real-Time Price Monitoring Pipeline

A robust, automated ETL pipeline written in Python that fetches live cryptocurrency data, stores it, and provides real-time moving average analytics.

## Technical Highlights
*   **Data Engineering:** Implemented a continuous ETL (Extract, Transform, Load) loop.
*   **Data Handling:** Used `pandas` for efficient data transformation and moving average calculation.
*   **Robustness:** Integrated error handling for API connection stability.
*   **Scalability:** Designed for persistent data storage using CSV.

## Technologies Used
*   Python (3.x)
*   Pandas (Data Manipulation)
*   Requests (API Integration)

## How to Run
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python tracker.py`