import streamlit as st

# Day2
# st.write('Hello world!')

# Day3
# st.header('st.button')

# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')

# Day5
# import numpy as np
# import altair as alt
# import pandas as pd
# import streamlit as st

# st.header('st.write')

# # Example 1

# st.write('Hello, *World!* :sunglasses:')

# # Example 2

# st.write(1234)

# # Example 3

# df = pd.DataFrame({
#      'first column': [1, 2, 3, 4],
#      'second column': [10, 20, 30, 40]
#      })
# st.write(df)

# # Example 4

# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# # Example 5

# df2 = pd.DataFrame(
#      np.random.randn(200, 3),
#      columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(
#      x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# st.write(c)

# Day15
import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
