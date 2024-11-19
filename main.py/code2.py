import streamlit as st
from googleapiclient.discovery import build
import gspread
from oauth2client.service_account import ServiceAccountCredentials


API_KEY = "AIzaSyCQM0R3Lq8JiXS85G0WIyvD15Qso3Jbg1k"
CSE_ID = "a6ce18e333aa24a3b"


SERVICE_ACCOUNT_FILE = "service_account.json"  
SHEET_NAME = "Search Results"


def init_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("C:\ai_agent_project\main.py\service_account.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open(Search_Results).sheet1
    return sheet


def save_to_sheets(sheet, query, results):
    sheet.append_row(["Query", "Title", "Link"])
    for result in results:
        sheet.append_row([query, result["title"], result["link"]])


def perform_search(query):
    service = build("customsearch", "v1", developerKey=API_KEY)
    res = service.cse().list(q=query, cx=CSE_ID).execute()
    results = []
    if "items" in res:
        for item in res["items"]:
            results.append({"title": item["title"], "link": item["link"]})
    return results


def main():
    st.title("AI Agent Project")
    st.write("This application lets you search the web using Google Custom Search.")

    query = st.text_input("Enter your query:")
    save_to_sheets_option = st.checkbox("Save results to Google Sheets")

    if st.button("Search"):
        if not query.strip():
            st.error("Please enter a query to search.")
            return

        try:
            st.write("Searching...")
            results = perform_search(query)
            if not results:
                st.warning("No results found. Please try a different query.")
            else:
                st.success("Search completed! Here are the results:")
                for result in results:
                    st.write(f"*{result['title']}*")
                    st.write(f"[{result['link']}]({result['link']})")

                if save_to_sheets_option:
                    try:
                        sheet = init_sheets()
                        save_to_sheets(sheet, query, results)
                        st.success("Results saved to Google Sheets!")
                    except Exception as e:
                        st.error(f"Failed to save to Google Sheets: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    pass
    main()