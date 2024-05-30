import pandas as pd
import streamlit as st

def main():
    #st.title("CSV結合")
    file1 = st.file_uploader('CSVファイルを選択してください', type='csv', accept_multiple_files=False, key='file1')
    file2 = st.file_uploader('CSVファイルを選択してください', type='csv', accept_multiple_files=False, key='file2')
        
    if (file1 is not None) & (file2 is not None):
        df1 = pd.read_csv(file1, dtype='object')
        df2 = pd.read_csv(file2, dtype='object')

        key_columns = set(df1.columns) & set(df2.columns)

        on_columns = st.multiselect('ON', key_columns)
        
        if len(on_columns)>0:
            df = pd.merge(df1, df2, on=on_columns, how='left')
            st.write(df.head())
            st.download_button(label="Download CSV", data=df.to_csv(index=False), file_name="merged.csv", mime="application/csv")

        

        
