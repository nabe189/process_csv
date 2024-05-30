import pandas as pd
import streamlit as st
from apps import concat_csv, merge_csv

def main():
    st.set_page_config(
        page_title='CSV処理',
        layout='wide'
    )

    st.title('CSV処理')

    selected_page = st.sidebar.radio("App一覧", ["結合", "マージ"])

    if selected_page == "結合":
        concat_csv.main()
    elif selected_page == "マージ":
        merge_csv.main()
    else:
        pass

if __name__ == "__main__":
    main()