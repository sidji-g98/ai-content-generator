from google import genai
import streamlit as st
import pandas as pd
import plotly.express as px
import time
import os

client = genai.Client(api_key=st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY"))

# ── Mock SEO Data ──
def get_mock_data():
    return pd.DataFrame({
        "Keyword": [
            "sustainable fashion brands",
            "eco friendly clothing",
            "ethical fashion india",
            "organic cotton clothes",
            "sustainable wardrobe tips",
            "slow fashion movement",
            "recycled fabric clothing",
            "green fashion trends",
            "affordable eco fashion",
            "sustainable style guide"
        ],
        "Clicks": [320, 280, 210, 190, 175, 160, 145, 130, 120, 110],
        "Impressions": [4200, 3800, 3100, 2900, 2600, 2400, 2100, 1900, 1800, 1600],
        "CTR": [7.6, 7.4, 6.8, 6.5, 6.7, 6.7, 6.9, 6.8, 6.7, 6.9],
        "Position": [3.2, 3.8, 4.1, 4.5, 4.3, 4.6, 4.8, 5.1, 5.3, 5.5]
    })

def get_ai_suggestions(keywords):
    prompt = f"""
    You are an SEO expert and content strategist.
    Based on these top performing keywords: {', '.join(keywords)}

    Provide:
    1. 5 Blog post title ideas
    2. 3 Meta description examples
    3. 3 Content gap opportunities
    4. 2 Long-tail keyword suggestions

    Be specific, creative and actionable.
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
    return "Error generating suggestions."

# ── UI ──
st.set_page_config(page_title="SEO Keyword Analyzer", page_icon="🔍")
st.title("🔍 SEO Keyword Analyzer")
st.subheader("by Siddharth Ganesh")
st.divider()

# Input
website = st.text_input("Enter your website/niche", 
                         placeholder="e.g. sustainable fashion blog")

if st.button("🔍 Analyze Keywords", use_container_width='stretch'):
    if website:
        with st.spinner("Loading keyword data..."):
            df = get_mock_data()

        # ── Metrics Row ──
        st.divider()
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Clicks", f"{df['Clicks'].sum():,}")
        col2.metric("Total Impressions", f"{df['Impressions'].sum():,}")
        col3.metric("Avg CTR", f"{df['CTR'].mean():.1f}%")
        col4.metric("Avg Position", f"{df['Position'].mean():.1f}")

        # ── Chart ──
        st.divider()
        st.markdown("### Top Keywords by Clicks")
        fig = px.bar(
            df.head(8),
            x="Keyword",
            y="Clicks",
            color="CTR",
            color_continuous_scale="Blues",
            title="Keyword Performance"
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width='stretch')

        # ── Data Table ──
        st.markdown("### Full Keyword Data")
        st.dataframe(df, use_container_width='stretch')

        # ── AI Suggestions ──
        st.divider()
        st.markdown("### AI-Powered Content Suggestions")
        with st.spinner("Generating AI suggestions..."):
            suggestions = get_ai_suggestions(df["Keyword"].tolist())
        st.write(suggestions)

        # ── Download ──
        st.download_button(
            label="📥 Download Keyword Report",
            data=df.to_csv(index=False),
            file_name=f"seo_report.csv",
            mime="text/csv"
        )
    else:
        st.warning("Please enter your website or niche!")