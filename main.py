import streamlit as st
st.title('나의 첫 Streamlit 앱')
st.write('안녕하세요!')
import streamlit as st
import pandas as pd
import plotly.express as px

# 웹앱 제목
st.title("CSV 데이터 시각화 (Plotly + Streamlit)")

# 데이터 불러오기
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    df = pd.read_csv(url)
    return df

df = load_data()

# 데이터 정보 표시
st.subheader("데이터 미리보기")
st.dataframe(df)

# 컬럼 선택
columns = df.columns.tolist()
x_axis = st.selectbox("X축 컬럼 선택", columns)
y_axis = st.selectbox("Y축 컬럼 선택", columns)

# 시각화
fig = px.line(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
st.plotly_chart(fig)
