# 🏠 Zillow Clone Data Automation

## 🌟 Overview

The **Zillow Clone Data Automation** project scrapes real estate data from a Zillow-like website and automates the process of filling out a Google Form with property details, including addresses, prices, and links. This project demonstrates the power of web scraping and automation using **BeautifulSoup** and **Selenium**.

## 🛠 Features
* **Web Scraping:** Extracts property addresses, prices, and links from the Zillow Clone website.
* **Google Form Automation:** Automatically fills and submits a Google Form with the scraped data.
* **Dynamic Data Handling:** Handles a varying number of properties on the page.

## 📂 Project Structure

    .
    ├── main.py                 # Main Python script for scraping and automation
    ├── requirements.txt        # Project dependencies
    ├── README.md               # Project documentation

## 🔧 Setup Guide

**Prerequisites**

* Python 3.x installed.
* Google Chrome installed.
* Chrome WebDriver compatible with your browser version.

**Installation**

1. Clone this repository:

    ```bash
    git clone https://github.com/matanohana433/zillow-data-automation.git
    cd zillow-data-automation
    ```

2. Create and activate a virtual environment (optional but recommended):

**Windows:**

    
    python -m venv venv
    venv\Scripts\activate
    

**macOS/Linux:**

    
    python3 -m venv venv
    source venv/bin/activate
    

3. Install dependencies:

    
    pip install -r requirements.txt
    

4. Download and set up Chrome WebDriver:

* Ensure the Chrome WebDriver version matches your Chrome browser version.
* Add the WebDriver to your system PATH or place it in the project directory.

## 🚀 Usage

1. **Run the Application:**

    
    python main.py
    

2. **What It Does:**

* Scrapes property data (addresses, prices, and links) from the Zillow Clone website.
* Fills out the provided Google Form with the scraped details.
* Submits the form automatically for each property.

## 🌟 Key Features

1. **Web Scraping:**
   * Extracts dynamic property data from the Zillow Clone website using BeautifulSoup.
2. **Form Automation:**
   * Fills out Google Forms automatically with Selenium.
3. **Seamless Integration:**
   * Combines scraping and automation for end-to-end data handling.

## 🚀 Future Enhancements

1. Add error handling for unavailable or malformed data.
2. Support additional real estate platforms for data scraping.
3. Integrate with a database to store scraped data for later analysis.

## 📬 Contact

For questions or collaboration:

* **Email:** matanohana433@gmail.com
* **GitHub:** [matanohana433](https://github.com/matanohana433)