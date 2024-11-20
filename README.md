AI Agent Project

Description

The AI Agent Project is a Python-based application with a user-friendly dashboard for performing Google searches, uploading CSV files, and storing data in Google Sheets. This project incorporates error handling for reliable operations and provides an interactive dashboard for streamlined use.

Key Features

1. Google Search:

Perform Google searches using a custom search engine.

Save search results (title, link, description) to Google Sheets.

2. File Upload and Processing:

Upload CSV files via the dashboard.

View the contents and save data to Google Sheets.

3. Error Handling:

Graceful handling of missing or incorrect inputs during search and file uploads.

Proper error messages displayed for issues like invalid file formats or API errors.

4. Dashboard Interface:

Built using Streamlit, offering an intuitive interface for users.

Sidebar for easy navigation between features.

Tools Used

1. Python - Primary programming language.
2. Streamlit - For creating the web-based dashboard.
3. Google Custom Search API - To fetch Google search results.
4. Google Sheets API - For saving search results and uploaded file data to Google Sheets.
5. Pandas - For handling and displaying CSV file data.
6. Gspread - For Google Sheets operations.
7. OAuth2Client - For authenticating with Google Sheets API.

Setup Instructions

Step 1: Prerequisites

1. Install Python: Ensure Python 3.x is installed on your system. Download from python.org.

2. Google Cloud Setup:

Create a project on Google Cloud Console.

Enable the Google Sheets API and Google Custom Search API.

Download the service_account.json file for your project.

Create a Custom Search Engine from Google CSE and get your API Key and Search Engine ID.

Step 2: Install Dependencies

Install the required Python libraries:

pip install streamlit pandas gspread oauth2client googleapiclient

Optional: Create a requirements.txt file:

streamlit
pandas
gspread
oauth2client
googleapiclient

To install from requirements.txt, use:

pip install -r requirements.txt

Usage Guide

Run the Application

1. Navigate to the project folder:

cd AI_Agent_Project

2. Start the dashboard:

streamlit run app.py

3. Open the browser link to access the dashboard.

Features Usage

1. Google Search

Enter a query in the search bar and click "Search."

View the results with their title, link, and description.

Click Save to Google Sheets to store results in a sheet (AI_Agent_Results).

2. File Upload

Upload a CSV file in the "Upload File" section.

View the file contents on the dashboard.

Click Save File Data to Google Sheets to save data in a sheet (AI_Agent_File_Uploads).

3. Error Handling

Errors such as missing search queries, invalid files, or failed Google Sheets authentication are handled gracefully, with user-friendly messages.

Additional Features

1. Error Handling:

Detects and displays proper error messages for invalid inputs or system issues.

Prevents application crashes due to missing or incorrect data.

2. Dashboard Interface:

Sidebar navigation between search and file upload functionalities.

Intuitive design for easy interaction.

What We Used in this Project

1. Programming Language:

Python 3.x

2. Libraries Installed:

streamlit for the dashboard.

pandas for handling CSV files.

gspread, oauth2client, googleapiclient for Google Sheets integration.

3. Google Cloud APIs:

Google Custom Search API.

Google Sheets API.

4. Credentials:

Service account file (service_account.json).

Setup Process Recap

1. Enable APIs and download service_account.json.

2. Install required libraries with pip.

3. Organize files (app.py, credentials, etc.).

4. Run the project using Streamlit.


Potential Use Cases

1. Automated Data Management:

Fetch data from Google searches and save for later use.

Quickly analyze and store uploaded CSV data in Google Sheets.

2. Error-Free Interaction:

Avoid crashes with robust error handling.

Friendly messages ensure smooth user experience.

3. Dashboard Convenience:

Intuitive interface for non-technical users to perform complex operations easily


https://drive.google.com/file/d/1ln1kxBaGRekSOPo7NI6Ha7sgS8k0wHWX/view?usp=sharing  (Working Video Of Project-Drive)

https://www.kapwing.com/w/giyQhQVL3V  (Working Video Of Project-kapwing)

https://drive.google.com/drive/folders/1iW_Rt1KqOeeiko_fq8kog3mZRUmKAmOP (Folder)
