from google import genai
import streamlit as st
import os
import time

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def generate_content(brand_name, niche, tone, audience, content_type):
    prompt = f"""
    You are a digital marketing expert.
    Brand: {brand_name}
    Niche: {niche}
    Tone: {tone}
    Target Audience: {audience}
    Generate the following: {content_type}
    Be concise, creative, and on-brand.
    """
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            if "429" in str(e):
                time.sleep(30)
            else:
                raise e
    return "Error: Could not generate content."

# ── UI ──
st.set_page_config(page_title="AI Content Generator", page_icon="🤖")
st.title("🤖 AI Content Generator")
st.subheader("by Siddharth Ganesh")
st.divider()

col1, col2 = st.columns(2)
with col1:
    brand_name = st.text_input("Brand Name", placeholder="e.g. EcoWear")
    niche = st.text_input("Niche / Industry", placeholder="e.g. Sustainable Fashion")
with col2:
    tone = st.selectbox("Tone of Voice", 
                        ["Friendly", "Professional", "Witty", "Inspirational"])
    audience = st.text_input("Target Audience", 
                             placeholder="e.g. Millennials who care about the planet")

content_type = st.multiselect("What do you want to generate?", [
    "3 Instagram captions with hashtags",
    "1 LinkedIn post",
    "Email newsletter intro",
    "Blog post outline",
    "3 Google Ad headline variants"
])

st.divider()

if st.button("✨ Generate Content", use_container_width=True):
    if brand_name and niche and audience and content_type:
        for item in content_type:
            st.markdown(f"### {item}")
            with st.spinner(f"Generating {item}..."):
                result = generate_content(
                    brand_name, niche, tone, audience, item
                )
            st.write(result)
            st.divider()

        # Download button
        full_output = "\n\n".join([
            generate_content(brand_name, niche, tone, audience, i)
            for i in content_type
        ])
        st.download_button(
            label="📥 Download All Content",
            data=full_output,
            file_name=f"{brand_name}_content.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please fill in all fields and select at least one content type!")