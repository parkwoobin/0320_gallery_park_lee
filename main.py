import streamlit as st

#이 프로젝트는 202284051박우빈 202284060이승우 학생이 합작으로 만들었음을 기록합니다. - 24.03.20


st.set_page_config(
    page_title="사진첩",                 #페이지 타이틀(탭) 사진첩
    page_icon="./images/icon.png"       #사진첩 아이콘
)

print("page reloaded")                      #삭제 후 rerun() 될 때 마다 terminal에 출력

st.title("내 갤로그")                       #페이지 메인 타이틀
st.markdown("갤로그에 사진을 추가하세요") #타이틀 밑에 마크다운



initial_gallerys = [
    {
        "name": "이재용",
        "types": ["인물"],
        "year": "2009",
        "image_url": "https://i.namu.wiki/i/idWM1Rt41ytLhluRQAoomaBgvXtp4CGYe46J_nYkQTuFQv5IK8TqjUo85oOJ92XuCWr6YQ41Jf_zv_f3-9VyhMhBGLphrwfCqN3R0KVKIsUrK1aNyWg03MMX-sdQ-jFTvHeW7oHHt7T8uyUGh3yyFw.webp"
    },
    {
        "name": "금문교",
        "types": ["풍경","거리"],
        "year": "2011",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
    },
    {
        "name": "여행",
        "types": ["여행"],
        "year": "1998",
        "image_url": "https://news.kbs.co.kr/data/fckeditor/new/image/2021/05/07/314691620354493423.jpg",
    },
    {
        "name": "피자",
        "types": ["음식"],
        "year": "2020",
        "image_url": "https://i.namu.wiki/i/uYFNltVdSS5SiTw3LTfiW08fyl4HLv49BK88yBV7lLm32Rak1mlEru21TIt9GQWzefAzVLEpctviwnPvGykWESXDz6_b8K3NLe18wjxiZyVKSYRLpWAWunOG_bJbclMAxtIrCcqKrCl36YxJAYmBxg.webp"
    }
]



auto_complete = st.toggle("예시 데이터로 채우기")

type_emoji_dict = {
    "인물": "🧑",
    "풍경": "🎇",
    "여행": "🧳",
    "접사": "🐶",
    "패션": "🦹‍♀️",
    "음식": "🍙",
    "거리": "🌉",
    "스포츠": "👟",
    "연예인": "🤖",
    "기타": "🎸"
}   


example_gallery = {
    "name": "메시",
    "types": ["스포츠","인물"],
    "year": "2014",
    "image_url": "https://ilyo.co.kr/contents/article/images/2020/0901/1598949067637300.jpg"
}

if "gallerys" not in st.session_state:
    st.session_state.gallerys = initial_gallerys


with st.form(key="form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        name=st.text_input(label="사진 제목", value=example_gallery["name"] if auto_complete else "")
 
    with col2:
        types=st.multiselect(label="사진 타입", options=list(type_emoji_dict.keys()), max_selections=2, default=example_gallery["types"] if auto_complete else [])
        
    with col3:
        year=st.text_input(label="사진 연도", value=example_gallery["year"] if auto_complete else "")

    image_url=st.text_input(label="갤로그 사진 url", value=example_gallery["image_url"] if auto_complete else "")
    submit=st.form_submit_button(label="submit")
    if submit:
        
        if not name:
            st.error("사진 제목을 입력하세요")
        elif len(types) == 0:
            st.error("사진 타입을 입력하세요")
        elif len(year) == 0:
            st.error("사진 연도를 입력하세요")
        else:
            st.success("갤로그를 추가합니다.")
            print("name", name)
            print("types", types)
            print("year", year)
            print("image_url", image_url)
            st.session_state.gallerys.append({
                "name": name,
                "types": types,
                "year": year,
                "image_url": image_url if image_url else "./images/default.png",
            })

    
    

    


for x in range(0,len(st.session_state.gallerys),4):
    row_gallerys = st.session_state.gallerys[x:x+4]
    cols = st.columns(4)
    for y in range(len(row_gallerys)):
        with cols[y]:
            gallery = row_gallerys[y]
            with st.expander(label=gallery["name"], expanded=True):
                st.markdown(gallery["year"])
                st.image(gallery["image_url"])
                emoji_types = [f"{type_emoji_dict[x]}{x}" for x in gallery["types"]]
                st.markdown("/" .join(emoji_types))
                
                delete_button = st.button(label="삭제", key=x+y, use_container_width=True)
                if delete_button:
                    print("delete button clicked")
                    del st.session_state.gallerys[x+y]
                    st.rerun()

