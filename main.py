import streamlit as st

def _get_embed_text(url):
    parsed_list = url.split('/')
    if parsed_list[-1] == '':
        parsed_list.pop()
    vid = parsed_list[-1].split('?')[0]
    handle = parsed_list[-3]
    return f'''<blockquote class="tiktok-embed" cite="{url}" data-video-id="{vid}" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="{handle}" href="https://www.tiktok.com/{handle}?refer=embed">{handle}</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>'''

def RUN():
    st.set_page_config(layout="wide")
    st.title('SxS TikTok Videos')
    l1, l2 = st.columns(2)
    url_1 = l1.text_input('URL 1:', '')
    url_2 = l2.text_input('URL 2:', '')
    if url_1 and url_2:
        col1, col2 = st.columns(2)
        with col1:
            st.components.v1.html(_get_embed_text(url_1), width=None, height=1000, scrolling=False)
        with col2:
            st.components.v1.html(_get_embed_text(url_2), width=None, height=1000, scrolling=False)
    # st.write(url)
    # st.components.v1.html(url, width=None, height=1000, scrolling=False)
    # st.video(url)

if __name__ == "__main__":
    RUN()