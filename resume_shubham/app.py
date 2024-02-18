import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl2(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl1("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
proimg=load_lottieurl2("https://lottie.host/5aa6aabc-2ebf-4269-b99c-f3fd0e40c61f/6dm7tHVs41.json")
img_contact_form = Image.open("images/dashboard2.jpg")
img_lottie_animation = Image.open("images/arogya.jpg")
img_profile = Image.open("images/my-passport-photo.jpg")


# ---- HEADER SECTION ----
with st.container():
    left_column, mid_column,right_column = st.columns((1,3,2))
    with left_column:
        st.image(img_profile,width=200)
        
    with mid_column:
        st.subheader("Hi, I am Shubham :wave:")
        st.title("Aspiring Data Scientist")
        st.write(
            "I am passionate about Data Science and machine learning. I love to learn new things and share my knowledge with others. I am proficient in Python and Java"
        )
    
    with right_column:
        st_lottie(proimg, height=300, key="upper") 
   

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            
Aspiring Data Scientist with a passion for data science, focusing on computer vision and machine learning.

- Led the development of a Disease Prediction Web App and an AI-assisted Kiosk for medical data collection, integrating GPT-3.5 Turbo.

- Proficient in Java, Python and skilled in frameworks like TensorFlow and Flask. Cloud computing expertise with AWS.

- Winner, SIH 2023: Recognized for creating an AI-assisted Telemedicine Kiosk, showcasing problem-solving skills and innovation.

- Worked as an AWS Cloud intern at F13 Technologies, gaining hands-on experience in diverse cloud architectures.

- Continuous Learner: Actively participated in conferences, hackathons, and tech boot camps, demonstrating a commitment to staying updated with industry trends.
            """
        )
        st.write("[My Linkedin >](https://www.linkedin.com/in/shubham-gupta-72a7751a5/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("AI assisted Telemedicine Kiosk for rural India")
        st.write(
            """This project employs the OpenAI GPT-3.5 Turbo model to analyze user prompts,
            extract key points, and generate reports with specialist recommendations for patients.
            The interactive interface is built on Streamlit using the MERN stack, facilitating 
            seamless communication by sending patient data to specific doctors via the e-Sanjivani app.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/34pqG2Ysmzc)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Sales Insight Dashboard")
        st.write(
            """
            I developed a comprehensive sales insights dashboard using Power BI, leveraging global financial sales data. The process began with connecting various data sources including SQL, NoSQL, Excel, and text files. I meticulously analyzed tables and their relationships to gain a deep understanding of the data structure. Utilizing Power Query Editor and DAX, I performed thorough data cleaning to ensure accuracy and consistency. With a solid foundation established, I developed a robust data model to facilitate insightful analysis. Finally, I crafted an intuitive and visually appealing dashboard that presents key sales metrics and trends, empowering stakeholders to make informed decisions.
            """
        )
        st.markdown("[Watch Video...](https://lnkd.in/gEyh5VUu)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/aryangupta007d@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
