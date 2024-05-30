import pandas as pd
import streamlit as st

def main():
    #st.title("CSV結合")
    files = st.file_uploader('CSVファイルを選択してください', type='csv', accept_multiple_files=True)

    if len(files)<2:
        st.error('2つ以上のCSVファオルを選択してください')
    
    if len(files)>1:
        dfs = [pd.read_csv(f, dtype='object') for f in files]
        flag = True

        columns = list(dfs[0].columns)
        for i in range(1, len(dfs)):
            if columns != list(dfs[i].columns):
                st.error('結合するファイルはすべて同じカラムを持つようにしてください')
                flag = False
                break
        
        if flag:
            df = pd.concat(dfs)
            st.download_button(label="Download CSV", data=df.to_csv(index=False), file_name="concatenated.csv", mime="application/csv")

        

        
