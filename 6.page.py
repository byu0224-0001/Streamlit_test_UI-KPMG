import streamlit as st

# --- 1. 페이지 상태 초기화 (처음 실행 시 'ThinkWise' 페이지로 설정) ---
if 'page' not in st.session_state:
    st.session_state.page = 'ThinkWise'

# --- 2. 페이지 변경을 위한 콜백 함수 정의 ---
def set_page(page_name):
    st.session_state.page = page_name

# --- 3. CSS 스타일 적용 코드 (수정 및 추가) ---
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
        background-color: gold; /* 사이드바 배경을 검은색으로 변경 */
    }
    
    /* 사이드바 접기/펴기 버튼 */
    [data-testid="stSidebarNav"] button {
        background-color: gold;
        color: black;
}
    /* 마우스 올렸을 때 약간 어둡게 변경 (선택사항) */
    [data-testid="stSidebarNav"] button:hover {
        background-color: #e6c300; /* 기존 gold보다 약간 어두운 색 */
        color: black;
}
            
    /* 사이드바 타이틀 ("ThinkWise") */
    [data-testid="stSidebar"] .st-emotion-cache-17x134l {
        color: black; /* 글자색을 검은색으로 */
        font-size: 24px; /* 폰트 크기 조정 (원하는 크기로 변경) */
}

    /* 사이드바의 모든 버튼에 대한 기본 스타일 */
    [data-testid="stSidebar"] .stButton button {
        width: 100%;
        text-align: left;
        background-color: transparent; /* 기본 배경 투명 */
        color: black; /* 기본 글자색을 검은색으로 변경 */
        border: none;
        padding: 14px;
        margin-bottom: 4px;
        border-radius: 0.5rem;
}   

    /* 사이드바 버튼에 마우스를 올렸을 때 스타일 */
    [data-testid="stSidebar"] .stButton button:hover {
        background-color: #333333;
        color: white; /* 호버 시 글자색은 흰색으로 */
}

    /* 사이드바 버튼에 마우스를 올렸을 때 스타일 */
    [data-testid="stSidebar"] .stButton button:hover {
        background-color: #333333;
        color: white;
    }
    
    /* 현재 선택된 페이지 버튼을 위한 특별 스타일 (st.session_state 값에 따라 Python에서 직접 제어) */
    /* 이 부분은 CSS 대신 Python 로직으로 처리합니다. */

</style>
""", unsafe_allow_html=True)

# --- 4. 페이지 함수 선언 (내용 동일) ---
def main_page():
    st.markdown("<h1 style='text-align: center; color: gold;'>ThinkWise</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>튜토리얼</h2>", unsafe_allow_html=True)
    st.video('data/Y2K_프로토타입_시연_영상.mp4')

def page2():
    st.markdown("<h1 style='text-align: center; color: gold;'>리포트 생성</h1>", unsafe_allow_html=True)

def page3():
    st.markdown("<h1 style='text-align: center; color: gold;'>커뮤니티</h1>", unsafe_allow_html=True)

# 딕셔너리 선언
page_names_to_funcs = {'ThinkWise': main_page, '리포트 생성': page2, '커뮤니티': page3}

# --- 5. 사이드바 메뉴 생성 (st.button과 콜백 사용) ---
st.sidebar.title("ThinkWise")

for page_name in page_names_to_funcs.keys():
    # 현재 선택된 페이지에 따라 버튼 타입을 다르게 설정하여 시각적 효과를 줍니다.
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
