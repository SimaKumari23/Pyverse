import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import pymongo
import time
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=conn["ojt"]
my=mydb["user_info"]
st.markdown("""
<style>
.stApp{
    background:
        radial-gradient(
            circle at center,
            rgba(168,85,247,0.28) 0%,
            rgba(168,85,247,0.18) 20%,
            rgba(168,85,247,0.08) 40%,
            transparent 70%
        ),

        linear-gradient(
            135deg,
            #0B1026 0%,
            #11122A 45%,
            #1A1D3A 75%,
            #0B1026 100%
        );
           background-attachment: fixed;
}
h1{
    background: linear-gradient(90deg,#00c6ff,#ffffff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    font-size:42px !important;
    font-weight:bold;
    text-align:center;
}

/* Username & Password Label */
div[data-testid="stWidgetLabel"] label,
div[data-testid="stTextInput"] label{
    color:#90E0EF !important;
    font-size:18px !important;
    font-weight:bold !important;
}

/* Input Text */
div[data-testid="stTextInput"] input{
    color:white !important;
}
</style>
""",unsafe_allow_html=True)
st.title(" 🔑 SignIn")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
with stylable_container(
    key="signin_btn",
    css_styles="""
    button{
        background:linear-gradient(90deg,#0040ff,#8c00ff);
        color:white;
        border:none;
        border-radius:10px;
        padding:10px 22px;
        font-weight:bold;
    }

    button:hover{
        background:linear-gradient(90deg,#005eff,#a855f7);
    }
    """
):
    b1 = st.button("🔑 SIGNIN")
valid=0
if b1:
       ans=my.find({"Username":t1,"Password":t2})
       for i in ans:
          valid = valid + 1

          st.session_state["username"] = i['Username']
          st.session_state["password"] = i['Password']
          st.session_state.logged_in = True
          st.switch_page("main.py")
       if valid==0:
              st.success("Invalid User login details")
st.markdown("""
  <div style=" text-align:center;color:#9CA3AF; margin-top:20px;">
   Don't have an account?
  </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3,1,3])
with col2:
 with stylable_container(
    key="signup_btn", 
    css_styles="""
    button{
        background:none;
        border:none;
        color:#90E0EF;
        padding:0;
        text-align:center;
        font-weight:bold;
        box-shadow:none;
    }

    button:hover{
        color:#60A5FA;
        text-decoration:underline;
    }
    """
 ):
    if st.button("Sign Up"):
        st.switch_page("pages/2SignUp.py")
