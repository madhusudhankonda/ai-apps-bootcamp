import streamlit as st
import numpy as np
st.write("""
         My first Streamlit App!\n
         How are you all?
         """)

st.markdown("""
            # Title
            ## Title2
            ### Title2
            """)


df = np.random.randn(0,20)
st.dataframe(df)

import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)