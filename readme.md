# ML Data Analyzer - FastAPI Based Application

* A Machine learning Data Analyzer built using
FastAPI, designed to analyze structured datasets
(CSV,Excel,Json) and generates data preview, statistical
insights for numerical and categorical data such as
(Mean,Median,Mode,Std Dev,Count,missing values etc..,)

# Features 
* Upload datasets(CSV,Excel,Json)
* Data Preview
  * rows
  * cols
  * total_cells
  * df.head()

* Automatic detection of:
  * Numerical features
  * Categorical features

* Statistical analysis
  * Mean, Median, Standard Deviation
  * Min, Max
  * Mising Values
  * Unique values

* Data Quality
   * Cardinality

# Project structure
|
|---main.py   # FastAPI server and API routes

|---analyzer.py # Core data processing & analyis logic

|---readme.md
|---requirements

# How it Works 
1. Upload File

2. Backend processing
 * File read based on type (CSV,Excel,Json)
 * Data is analyzed using pandas
 * Numerical & Categorical statistics are computed

3. Output 
 Result are returned via API endpoints (used internally or via Swagger UI)

# Tech Stack

Technology      Purpose

Python         Core language
FastAPI        Backend API
Pandas         Data Analysis
NumPy          Numerical Operations
Uvicorn        ASGI server

# How to Run the Project

1 Clone the repository
git clone https://github.com/Ajju-03/files_analyzer.git

cd your-repo-name

2 Install dependencies
pip install -r requirements.txt

3 Run the FastAPI server
uvicorn main:app --reload
