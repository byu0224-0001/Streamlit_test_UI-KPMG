import streamlit as st
import pandas as pd # 데이터 처리를 위해 pandas 추가
import plotly.express as px # 차트 생성을 위해 plotly 추가

# --- 1. 페이지 상태 초기화 ---
if 'page' not in st.session_state:
    st.session_state.page = 'Main'

# --- 2. 페이지 변경을 위한 콜백 함수 정의 ---
def set_page(page_name):
    st.session_state.page = page_name

# --- 3. CSS 스타일 적용 코드 (모든 디자인 수정사항 통합) ---
st.markdown("""
<style>
    /* 전체 앱 배경 */
    .stApp {
        background-color: black;
    }

    /* 상단 헤더 배경 */
    [data-testid="stHeader"] {
        background-color: gold;
    }

    /* 사이드바 배경 */
    [data-testid="stSidebar"] {
        background-color: gold;
    }
    
    /* 사이드바 접기/펴기 버튼 */
    [data-testid="stSidebarNav"] button {
        background-color: gold;
        color: black;
    }
    [data-testid="stSidebarNav"] button:hover {
        background-color: #e6c300; /* gold보다 약간 어두운 색 */
        color: black;
    }

    /* 사이드바 타이틀 ("ThinkWise") */
    [data-testid="stSidebar"] .st-emotion-cache-17x134l {
        color: black;
        font-size: 24px;
    }

    /* 사이드바의 모든 버튼에 대한 기본 스타일 (선택되지 않았을 때) */
    [data-testid="stSidebar"] .stButton button[kind="secondary"] {
        width: 100%;
        text-align: left;
        background-color: transparent;
        color: black;
        border: none;
        padding: 14px;
        margin-bottom: 4px;
        border-radius: 0.5rem;
    }

    /* 사이드바 버튼에 마우스를 올렸을 때 스타일 */
    [data-testid="stSidebar"] .stButton button[kind="secondary"]:hover {
        background-color: rgba(0, 0, 0, 0.1); /* 약간 어두운 효과 */
        color: black;
    }
    
    /* 현재 선택된 페이지 버튼 스타일 (primary 타입) */
    [data-testid="stSidebar"] .stButton button[kind="primary"] {
        width: 100%;
        text-align: left;
        background-color: black;
        color: white;
        border: none;
        padding: 14px;
        margin-bottom: 4px;
        border-radius: 0.5rem;
        font-weight: bold;
    }

    /* 일반 텍스트 색상 (메인 화면) */
    .st-emotion-cache-1y4p8pa, .st-emotion-cache-zz1m3p, .st-emotion-cache-1n7693, p, li {
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# --- 4. 페이지 함수 선언 (분석 대시보드 함수 추가) ---
def main_page():
    st.markdown("<h1 style='text-align: center; color: gold;'>ThinkWise</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>튜토리얼</h2>", unsafe_allow_html=True)
    st.video('data/Y2K_프로토타입_시연_영상.mp4')

def page2():
    st.markdown("<h1 style='text-align: center; color: gold;'>리포트 생성</h1>", unsafe_allow_html=True)

def page3():
    st.markdown("<h1 style='text-align: center; color: gold;'>커뮤니티</h1>", unsafe_allow_html=True)

# --- 1. '분석 대시보드' 페이지 함수 새로 만들기 ---
def dashboard_page():
    st.markdown("<h1 style='text-align: center; color: gold;'>분석 대시보드</h1>", unsafe_allow_html=True)
    
    # 예시 데이터프레임 생성
    data = {
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [23, 45, 55, 30, 61],
        'Ratio': [0.2, 0.3, 0.1, 0.25, 0.15]
    }
    df = pd.DataFrame(data)

    # 대시보드 레이아웃 구성
    st.subheader("카테고리별 데이터 현황")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="총합", value=df['Value'].sum(), delta="5%")
        st.dataframe(df) # 데이터 테이블 표시
    with col2:
        # 파이 차트 생성
        fig = px.pie(df, names='Category', values='Ratio', title='카테고리별 비율')
        st.plotly_chart(fig, use_container_width=True)

# --- 1. '분석 대시보드' 페이지 함수 새로 만들기 ---


# 2. 딕셔너리 페이지
page_names_to_funcs = {
    'Main': main_page, 
    '리포트 생성': page2, 
    '커뮤니티': page3,
    '분석 대시보드': dashboard_page
}

# --- 5. 사이드바 메뉴 생성 (st.button과 콜백 사용) ---
st.sidebar.title("ThinkWise")

# --- 3. for 루프가 자동으로 새 버튼 생성 ---
for page_name in page_names_to_funcs.keys():
    is_selected = (st.session_state.page == page_name)
    button_type = "primary" if is_selected else "secondary"
    
    st.sidebar.button(
        page_name, 
        on_click=set_page, 
        args=(page_name,), 
        type=button_type,
        use_container_width=True
    )

# --- 6. 선택된 페이지 실행 ---
page_names_to_funcs[st.session_state.page]()
