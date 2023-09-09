import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(
    page_title='NINO_HOME',
    page_icon='✨'
)

sch_img = 'https://gangdong.dge.hs.kr/upload/schl/gangdongh/widg/M_visual.png'
club_img = Image.open('NULL 홍보지.jpg')
dog_img = Image.open('mini.jpg')
band_img = 'https://image.bugsm.co.kr/album/images/500/40790/4079061.jpg'
game_img = 'https://i.pinimg.com/564x/5a/26/ca/5a26ca4d4db8de541434ad1466d99af7.jpg'
schlogo_img = 'https://gangdong.dge.hs.kr/images/schl/web/gangdongh/sub/img0101_0401.png'
movie_img = 'https://i.pinimg.com/564x/03/9c/30/039c309ada7f4189559303944948cc71.jpg'
swim_img = 'https://i.pinimg.com/564x/4e/fc/f9/4efcf9ef0498d2eb4dc2364b36e56d27.jpg'
piano_img = 'https://i.pinimg.com/564x/6e/ff/a1/6effa154ab473877c1ae8c9d1be3c722.jpg'

menu = st.sidebar.selectbox(
    'MENU', ['About Me', 'About My School', 'About My Club'])

# 자기소개
if menu == 'About Me':
    st.header('About Me')
    tab1, tab2 = st.tabs(['ABOUT', 'What I love'])

    with tab1:
        st.header('조은경(Cho Eunkyeong)')
        st.write('_🎂:grey[2006.04.04]_')
        st.write('_📧:grey[slowhale19@gmail.com]_')
        st.write('게임개발자가 꿈인 강동고 조은경입니다😊')

    with tab2:
        bar1, bar2, bar3 = st.columns([2, 2, 2])
        with bar1:
            st.image(dog_img)
            st.image(movie_img)
        with bar2:
            st.image(band_img)
            st.image(swim_img)
        with bar3:
            st.image(game_img)
            st.image(piano_img)

# 학교소개
elif menu == 'About My School':
    st.header('About My School')

    st.image(sch_img)
    st.subheader('대구강동고등학교')
    st.write('대구광역시 동구 금강로 65 :grey[(053)231-6320-6322]')

    bar1, bar2 = st.columns([3, 4])

    with bar1:
        st.image(schlogo_img)
    with bar2:
        st.write('교장 : 정희석')
        st.write('교훈 : 인의예지')
        st.write('교목 : 주목')
        st.write('교화 : 목련')

# 동아리소개
elif menu == 'About My Club':
    st.header('About My Club')

    bar1, bar2 = st.columns([2, 3])

    with bar1:
        st.image(club_img, caption='동아리 홍보지')

    with bar2:
        st.subheader('NULL')
        st.write(':blue[코딩 동아리 2021~]')
        st.write('부장 : 조은경')

        df = pd.DataFrame({
            '활동': ['컴퓨터 기초', 'Java 학습', '협업 프로젝트', '아두이노', '게임 제작'],
            '진행': ['완료', '완료', '진행 중', '진행 중', '예정']
        })
        st.dataframe(df)


else:
    st.subheader('관심분야')
