import streamlit as st

st.title("Love App ❤️")

# Session state to track if answered
if "show_no_message" not in st.session_state:
    st.session_state.show_no_message = False

# Show buttons only if no message is shown
if not st.session_state.show_no_message:
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes 😍"):
            st.success("I love you more 😘")
            st.balloons()
            st.stop()
    
    with col2:
        if st.button("No 😢"):
            st.session_state.show_no_message = True
            st.rerun()

# Show "No" message
if st.session_state.show_no_message:
    st.error("Don't Lie...")
    
    if st.button("🥰 Say Truth"):
        st.session_state.show_no_message = False
        st.rerun()