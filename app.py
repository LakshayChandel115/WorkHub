import streamlit as st

# Title & Header
st.title("🌐 WorkHub")
st.header("Hire your freelancer instantly")

st.markdown("---")

# About Section
st.subheader("📌 About WorkHub")
st.write("""
WorkHub is a modern freelancing platform connecting **clients** with **skilled freelancers** instantly.  
We ensure:
- ✅ Verified Client & Freelancer Profiles  
- ✅ Secure Payments  
- ✅ Ratings & Review System  
""")

st.markdown("---")

# Features / Highlights
st.subheader("⚡ Why Choose WorkHub?")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("50+", "Active Clients")
with col2:
    st.metric("200+", "Skilled Freelancers")
with col3:
    st.metric("100%", "Secure Payments")

st.markdown("---")

# Category Selection
st.subheader("🎯 What do you want?")
category = st.selectbox(
    "Choose a category:",
    ["Frontend Developer", "Backend Developer", "AI/ML Expert", "Video Editor", "Graphic Designer", "Content Writer","Many More"]
)

st.info(f"You selected: **{category}**")

if st.button("Find Freelancers"):
    st.success(f"✨ Showing top {category}s available for hire!")

st.markdown("---")

# Interactive Hire Form
st.subheader("📝 Post Your Project")
with st.form("hire_form"):
    name = st.text_input("Your Name")
    project = st.text_area("Project Details")
    budget = st.number_input("Budget ($)", min_value=100, step=50)
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success(f"Thanks {name}! We'll connect you with top freelancers for '{project}' 🚀")

st.markdown("---")

# Testimonials
st.subheader("⭐ Testimonials")
st.write("💬 *'WorkHub helped me find the best developer in 24 hours!'* – Client A")
st.write("💬 *'As a freelancer, I got my first project within 2 days of joining WorkHub.'* – Freelancer B")

st.markdown("---")

# Footer
st.markdown("© 2025 WorkHub Inc. | All Rights Reserved")
