import streamlit as st

st.write('# Hi! Welcome to my app!')

st.write('반갑습니다. 저의 웹에 오신 것을 환영합니다.')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


option = st.selectbox(
    '좋아하는 동물은?',
    ('강아지', '고양이', '토끼'))

st.write('너가 좋아하는 동물은....   ', option)



txt = st.text_area('자신을 소개하세요.', '''
    
    ''')
st.write('입력한 내용은:', txt)


age = st.slider('몇살입니까?', 0, 130, 23)
st.write("저는 ", age, '살 입니다.')