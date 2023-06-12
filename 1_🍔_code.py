import streamlit as st

st.set_page_config(
    page_icon="😊",
    page_title="내가 만든 사이트",
    layout="wide",
)

st.subheader("코드보기")

if st.button("home.py 코드 보기"):
    code = '''import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_icon="🍕",
    page_title="체질량 지수 계산하기",
    layout="wide",
)

st.header(":blue[스마트모빌리티] 과제용 사이트에 오신걸 환영합니다🖐") #페이지 제목
st.subheader("2022362 이강준") #페이지 부제목

st.write("체질량 지수 계산기🗿")

st.info('BMI = 체중(kg) / (키(m) * 키(m))') #정보 위젯

st.caption('체질량 지수(BMI)는 개인의 체중과 키를 바탕으로 측정되는 지수로, 비만 여부를 판단하는 데 일반적으로 사용됩니다. ') #캡션달기
st.caption('BMI는 체지방량을 대략적으로 추정하는 데 도움이 되며, 건강과 관련된 위험 요소를 파악하는 데 일부 도움이 될 수 있습니다. ')
  
height = st.number_input('신장 (cm)',value = 177,step=5)
st.write(height,'cm')

weight = st.number_input('체중 (kg)',value = 80,step = 5)
st.write(weight,'kg')

bmi = weight/((height/100)**2) #bmi 예제

if st.button('계산'): #누를시 bmi에 따라 다른 문장 출력
    
    st.write('당신의 체질량 지수는',round(bmi,2),'입니다.')
    if bmi >= 35:
        st.error('비만입니다.') #에러박스 출력
    elif bmi >= 25:
        st.warning('과체중입니다.') #경고박스 출력
    elif bmi >= 18.5:
        st.success('정상 체중입니다!') #성공박스 출력
    else:
        st. warning('저체중입니다.') #경고박스 출력
    st.caption('저체중: BMI < 18.5') #bmi 범주 출력
    st.caption('정상 체중: 18.5 ≤ BMI < 25')
    st.caption('과체중: 25 ≤ BMI < 30')
    st.caption('비만: 30 ≤ BMI')

if st.button("초기화"):
        weight = 0
        height = 0

st.write('✅정상 체중을 위한 체크리스트')
d= st.checkbox('신선한 과일과 채소를 다양하게 섭취합니다')
if d:
    d =0
d= st.checkbox('영양가 있는 전체곡물을 선호한다')
if d:
    d=0
d= st.checkbox('단백질을 충분히 섭취합니다')
if d:
    d=0
d= st.checkbox('건강한 지방을 선택합니다')

st.write("재미로 보는 MBTI별 다이어트 유형🗿")

mbti = st.selectbox(
    '당신의 MBTI의 무엇입니까?',  # 사용자에게 MBTI 선택을 묻는 질문 출력
    ('INFP','INFJ','INTP','INTJ','ISFP','ISFJ','ISTP','ISTJ','ENFP','ENFJ','ENTP','ENTJ','ESFP','ESFJ','ESTP','ESTJ')
)

# 사용자가 선택한 MBTI에 따라 다른 메시지 출력
if mbti == 'INFP':
    st.write('요가, 필라테스 등 혼자 할 수 있는 운동으로 다이어트 하는 유형')
elif mbti == 'INFJ':
    st.write('항상 밤마다 야식 고민하면서 정작 먹지는 않는 의지 강한 유형')
elif mbti == 'INTP':
    st.write('일단 다이어트에 필요한 영양제, 운동 기구 부터 구매하는 유형')
elif mbti == 'INTJ':
    st.write('오늘은 그래도 돼~ 항상 오늘의 운동을 내일로 미루는 유형')
elif mbti == 'ISFP':
    st.write('헬스장 가기까지 시간은 오래 걸리지만, 정작 헬스장 가면 가장 열심히 하는 유형')
elif mbti == 'ISFJ':
    st.write('운동 다이어리 어플로 칼로리 소모량, 식단 등 꼼꼼하게 정리하는 유형')
elif mbti == 'ISTP':
    st.write('워너비 몸매 사진 붙여놓고 다이어트 의지 불태우는 유형')
elif mbti == 'ISTJ':
    st.write('목표 달성하기 위해 1:1 PT 받으면서 열성적으로 다이어트 하는 유형')
elif mbti == 'ENFP':
    st.write('헬스장 등록만 해두고 안 가는 유형(헬스장 기구 하나는 ENFP가 들여온 셈)')
elif mbti == 'ENFJ':
    st.write('혼자하는 운동보다는 운동 동아리 가입해서 많은 사람들과 함께 운동하는 유형')
elif mbti == 'ENTP':
    st.write('단기간 다이어트 방법만 검색하면서 정작 운동은 안하는 유형')
elif mbti == 'ENTJ':
    st.write('헬스 트레이너에게 체중 관리 식단과 운동법 등 운동 정보부터 알아보는 유형')
elif mbti == 'ESFP':
    st.write('매일매일의 변화를 기록으로 남기면서 운동 의지 불태우는 유형')
elif mbti == 'ESFJ':
    st.write('운동은 무조건 친구와 함께! 친구 꼬드겨서 같이 운동하는 유형')
elif mbti == 'ESTP':
    st.write('유튜브 찾아보면서 새로운 타입의 운동을 찾는 것을 즐기는 유형')
elif mbti == 'ESTJ':
    st.write('한번 결심하면 끝까지 해내서 결국 다이어트 성공하는 유형')
else:
    st.write("자신의 MBTI를 알려주세요.")

    '''
    st.code(code,language="python")