import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import pymongo
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=conn["ojt"]#database of mongodb
my=mydb["user_info"]#it is collection(table)
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
    background-attachment:fixed;
}

/* Title */
h1{
    background:linear-gradient(90deg,#00c6ff,#ffffff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    font-size:42px !important;
    font-weight:bold;
    text-align:center;
}

/* Labels */
div[data-testid="stWidgetLabel"] label,
div[data-testid="stTextInput"] label,
div[data-testid="stDateInput"] label{
    color:#90E0EF !important;
    font-size:18px !important;
    font-weight:bold !important;
}

/* Input Text */
div[data-testid="stTextInput"] input{
    color:white !important;
}

/* Date Input */
div[data-testid="stDateInput"] input{
    color:white !important;
}
</style>
""", unsafe_allow_html=True)
st.title("🔐 Sign Up")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
t3=st.text_input(" Confirm Password",type="password")
t4=str(st.text_input("Mobile Number"))
t5=st.text_input("Email Id")
t6=st.date_input("DOB")
with stylable_container(
    key="signup_btn",
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
    b1=st.button("CREATE ACCOUNT")
if b1:
    if t1 == "" or t2 == "" or t3 == "" or t4 == "" or t5 == "":
        st.success("⚠ Please fill all fields.")

    elif t2 != t3:
        st.success("⚠ Password and Confirm Password do not match.")

    else:
        my.insert_one({"Username":t1,"Password":t2,"Confirm Password":t3,"Mobile Number":str(t4),"Email Id":t5,"DOB":str(t6)});
        st.success("✅ Account Created Successfully")

st.markdown("""
  <div style="text-align:center; color:#9CA3AF; margin-top:20px;">
   Already have an account
  </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3,1,3])
with col2:
 with stylable_container(
    key="signin_btn",
    css_styles="""
    button{
        background:none;
        border:none;
        color:#90E0EF;
        padding:0;
        font-weight:bold;
        box-shadow:none;
    }
    
    button:hover{
        color:#60A5FA;
        text-decoration:underline;
    }
    """
 ):
    if st.button("Sign In"):
        st.switch_page("pages/1SignIn.py")

                  
