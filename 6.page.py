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
            
 /* 페이지 제목 색상 (뉴스 분석 대시보드) */
    h1 {
        color: gold;
    }
    
    /* 페이지 부제목 색상 */
    p {
        color: grey;
    }

    /* st.metric 라벨 색상 */
    [data-testid="stMetricLabel"] {
        color: #D3D3D3; /* 밝은 회색 */
    }
    
    /* st.subheader, st.markdown 제목 색상 (트렌딩 토픽 등) */
    h3, h5 {
        color: gold;
    }

    /* st.text 및 st.caption 색상 (인공지능 혁신, 1247 기사 등) */
    .st-emotion-cache-1629p8f, .st-emotion-cache-1xarl3l {
        color: white;
    }

    /* st.info 박스 안의 글자색 */
    .st-emotion-cache-1wivap2 {
        color: black;
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

def dashboard_page():
    # 페이지 제목
    st.markdown("<h1 style='text-align: center; color: white;'>뉴스 분석 대시보드</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: grey;'>실시간 뉴스 데이터 분석 및 트렌드 인사이트</p>", unsafe_allow_html=True)
    st.divider()

    # --- 상단 핵심 지표 (KPI) ---
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric(label="총 뉴스 기사", value="8,146", delta="120")
    with kpi2:
        st.metric(label="분석된 토픽", value="245", delta="-5")
    with kpi3:
        st.metric(label="분석 정확도", value="89%", delta="1.2%")
    with kpi4:
        st.metric(label="실시간 업데이트", value="활성")
    st.divider()

    # --- ▼▼▼ 메인 차트 영역 컬럼 비율 수정 ▼▼▼ ---
    chart1, chart2 = st.columns([1, 1.5]) # 왼쪽과 오른쪽 컬럼의 너비 비율을 1:1.5로 수정

    with chart1:
        # subheader 대신 markdown을 사용하여 아이콘과 색상 추가
        st.markdown("<h5>📈 트렌딩 토픽</h5>", unsafe_allow_html=True)
        trending_topics = {
            '인공지능 혁신': ('1247 기사', '23.6%'),
            '빅데이터 분석': ('892 기사', '15.2%'),
            '패키지 여행': ('634 기사', '-45.8%'),
            '클라우드 컴퓨팅': ('323 기사', '5.3%'),
            '사이버보안': ('488 기사', '-12.7%')
        }
        for topic, (count, delta) in trending_topics.items():
            st.text(topic)
            st.caption(count)
            progress_value = abs(float(delta.strip('%'))) / 100
            st.progress(progress_value, text=delta)

    with chart2:
        st.markdown("<h5>📊 카테고리별 분포</h5>", unsafe_allow_html=True)
        category_data = {
            'Category': ['기술', '경제', '사회', '국제'],
            'Count': [2847, 2284, 1792, 1223],
            'Percentage': [35, 28, 22, 15]
        }
        df_category = pd.DataFrame(category_data)
        fig_bar = px.bar(df_category, y='Category', x='Count',
                         text=[f'{p}%' for p in df_category['Percentage']],
                         orientation='h',
                         color_discrete_sequence=px.colors.qualitative.Plotly)
        fig_bar.update_layout(yaxis={'categoryorder':'total ascending'},
                              xaxis_title="기사 수", yaxis_title="")
        st.plotly_chart(fig_bar, use_container_width=True)
    
    st.divider()

    # --- ▼▼▼ 하단 차트 영역 컬럼 비율 수정 ▼▼▼ ---
    chart3, chart4 = st.columns([1.2, 1]) # 왼쪽과 오른쪽 컬럼의 너비 비율을 1.2:1로 수정

    with chart3:
        st.markdown("<h5>🏭 관심 산업 분포</h5>", unsafe_allow_html=True)
        industry_data = {
            'Industry': ['반도체', 'IT서비스', '자동차', '금융', '기타'],
            'Value': [40, 25, 15, 10, 10]
        }
        df_industry = pd.DataFrame(industry_data)
        fig_donut = px.pie(df_industry, names='Industry', values='Value', hole=0.6)
        st.plotly_chart(fig_donut, use_container_width=True)

    with chart4:
        st.markdown("<h5>💡 AI의 맞춤형 성장 제안</h5>", unsafe_allow_html=True)
        st.info("최근 'IT/반도체' 산업에 대한 분석이 60%를 차지합니다.")
        st.write("시장께서 주목받고 있는 '친환경 에너지' 산업에 대한 분석을 시작해보는 것은 어떨까요?")
        if st.button("친환경 에너지 관련 뉴스 분석하기"):
            st.success("'친환경 에너지' 토픽 분석을 시작합니다...")


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
