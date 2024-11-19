import streamlit as st
import pandas as pd
from googleapiclient.discovery import build
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def setup_google_sheets(sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name).sheet1


def save_to_google_sheets(sheet, query, results):
    for result in results:
        sheet.append_row([query, result['title'], result['link'], result.get('snippet', 'No description')])


def search_google(query):
    api_key = "AIzaSyCQM0R3Lq8JiXS85G0WIyvD15Qso3Jbg1k"  
    cse_id = "a6ce18e333aa24a3b"  
    service = build("customsearch", "v1", developerKey=api_key)
    result = service.cse().list(q=query, cx=cse_id).execute()
    return result.get('items', [])


def main():
    st.title("AI Agent Dashboard")
    st.sidebar.title("Dashboard Features")
    choice = st.sidebar.radio("Choose an option:", ["Search Google", "Upload File"])

    if choice == "Search Google":
        st.header("Google Search")
        query = st.text_input("Enter your search query:")
        if st.button("Search"):
            if query:
                try:
                    results = search_google(query)
                    if results:
                        st.success(f"Found {len(results)} results for '{query}'")
                        for result in results:
                            st.write(f"*{result['title']}*")
                            st.write(result['link'])
                            st.write(result.get('snippet', 'No description'))
                            st.write("---")


                        if st.button("Save to Google Sheets"):
                            try:
                                sheet = setup_google_sheets("AI_Agent_Results")  
                                save_to_google_sheets(sheet, query, results)
                                st.success("Results saved to Google Sheets successfully!")
                            except Exception as e:
                                st.error(f"Error saving to Google Sheets: {e}")
                    else:
                        st.warning("No results found.")
                except Exception as e:
                    st.error(f"Error performing search: {e}")
            else:
                st.warning("Please enter a query.")

    elif choice == "Upload File":
        st.header("Upload a File")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file:
            try:
                
                data = pd.read_csv(uploaded_file)
                st.write("Uploaded File Data:")
                st.dataframe(data)

             
                if st.button("Save File Data to Google Sheets"):
                    try:
                        sheet = setup_google_sheets("AI_Agent_File_Uploads") 
                        for _, row in data.iterrows():
                            sheet.append_row(row.tolist())
                        st.success("File data saved to Google Sheets successfully!")
                    except Exception as e:
                        st.error(f"Error saving file data to Google Sheets: {e}")
            except Exception as e:
                st.error(f"Error reading file: {e}")

if __name__ == "__main__":
    main()