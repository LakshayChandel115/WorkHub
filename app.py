import streamlit as st

# Page config
st.set_page_config(page_title="WorkHub - Freelancing Platform", page_icon="💼", layout="wide")

# Header section
st.title("💼 WorkHub")
st.subheader("Hire your freelancer instantly 🚀")

st.markdown("---")

# About / Features section
st.header("Why choose WorkHub?")
st.write("""
- **Client & Freelancer Profiles**: Build your profile and showcase your work.
- **Review System**: Get rated and reviewed to build trust.
- **Secure Payment Method**: Hassle-free transactions with escrow protection.
""")

st.markdown("---")

# Call-to-Action
st.header("Get Started Today")
st.success("WorkHub connects clients with talented freelancers instantly!")

if st.button("👉 Hire Talented"):
    st.balloons()
    st.write("Welcome to WorkHub! 🎉 Start exploring talent now.")

# Footer
st.markdown("---")
st.caption("© 2025 WorkHub | Smart India Hackathon Prototype")
