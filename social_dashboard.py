from google import genai
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import os

client = genai.Client(api_key=st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY"))
# ── Mock Social Media Data ──
def get_mock_social_data():
    return pd.DataFrame({
        "Date": pd.date_range(start="2026-04-01", periods=30, freq="D"),
        "Platform": ["Instagram"] * 10 + ["LinkedIn"] * 10 + ["Twitter"] * 10,
        "Likes": [120,145,98,210,180,95,230,175,160,200,
                  45,62,38,75,55,48,82,70,65,78,
                  30,42,28,55,48,35,60,45,40,52],
        "Comments": [15,22,12,35,28,10,40,25,20,32,
                     8,12,6,15,10,8,18,14,12,16,
                     5,8,4,12,9,6,14,9,8,10],
        "Shares": [8,12,6,20,15,5,25,14,11,18,
                   12,18,9,22,16,11,24,20,17,21,
                   3,5,2,8,6,3,10,6,5,7],
        "Reach": [1200,1450,980,2100,1800,950,2300,1750,1600,2000,
                  450,620,380,750,550,480,820,700,650,780,
                  300,420,280,550,480,350,600,450,400,520],
        "Post_Type": ["Reel","Carousel","Image","Reel","Carousel",
                      "Image","Reel","Carousel","Image","Reel",
                      "Article","Poll","Image","Article","Poll",
                      "Image","Article","Poll","Image","Article",
                      "Thread","Image","Thread","Image","Thread",
                      "Image","Thread","Image","Thread","Image"]
    })

def get_engagement_rate(df):
    df["Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]
    df["Engagement_Rate"] = (df["Engagement"] / df["Reach"] * 100).round(2)
    return df

def get_ai_summary(metrics):
    prompt = f"""
    You are a social media marketing expert.
    Here are this week's social media performance metrics:
    {metrics}

    Write a friendly, insightful weekly performance summary covering:
    1. Overall performance highlights
    2. Best performing platform
    3. Best performing content type
    4. 3 specific actionable recommendations for next week

    Keep it concise, positive and data-driven.
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
    return "Error generating summary."

# ── UI ──
st.set_page_config(page_title="Social Media Dashboard", page_icon="📊")
st.title("📊 Social Media Dashboard")
st.subheader("by Siddharth Ganesh")
st.divider()

# Platform filter
platform = st.selectbox("Select Platform", 
                         ["All Platforms", "Instagram", "LinkedIn", "Twitter"])

if st.button("📊 Generate Dashboard", use_container_width=True):

    df = get_mock_social_data()
    df = get_engagement_rate(df)

    # Filter
    if platform != "All Platforms":
        filtered_df = df[df["Platform"] == platform]
    else:
        filtered_df = df

    # ── Metrics Row ──
    st.divider()
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Likes", f"{filtered_df['Likes'].sum():,}")
    col2.metric("Total Reach", f"{filtered_df['Reach'].sum():,}")
    col3.metric("Avg Engagement Rate", 
                f"{filtered_df['Engagement_Rate'].mean():.1f}%")
    col4.metric("Total Posts", len(filtered_df))

    st.divider()

    # ── Chart 1: Engagement Over Time ──
    st.markdown("### Engagement Over Time")
    fig1 = px.line(
        filtered_df,
        x="Date",
        y="Engagement_Rate",
        color="Platform" if platform == "All Platforms" else None,
        title="Daily Engagement Rate (%)"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # ── Chart 2: Post Type Performance ──
    st.markdown("### Performance by Post Type")
    post_perf = filtered_df.groupby("Post_Type")["Engagement_Rate"].mean().reset_index()
    fig2 = px.bar(
        post_perf,
        x="Post_Type",
        y="Engagement_Rate",
        color="Engagement_Rate",
        color_continuous_scale="Greens",
        title="Average Engagement Rate by Post Type"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # ── Chart 3: Platform Comparison ──
    if platform == "All Platforms":
        st.markdown("### Platform Comparison")
        plat_perf = df.groupby("Platform")[["Likes","Comments","Shares"]].sum().reset_index()
        fig3 = px.bar(
            plat_perf,
            x="Platform",
            y=["Likes", "Comments", "Shares"],
            title="Total Engagement by Platform",
            barmode="group"
        )
        st.plotly_chart(fig3, use_container_width=True)

    # ── AI Weekly Summary ──
    st.divider()
    st.markdown("### AI Weekly Performance Summary")
    metrics_summary = f"""
    Platform: {platform}
    Total Likes: {filtered_df['Likes'].sum()}
    Total Reach: {filtered_df['Reach'].sum()}
    Avg Engagement Rate: {filtered_df['Engagement_Rate'].mean():.1f}%
    Best Post Type: {filtered_df.groupby('Post_Type')['Engagement_Rate'].mean().idxmax()}
    Total Posts: {len(filtered_df)}
    """
    with st.spinner("Generating AI summary..."):
        summary = get_ai_summary(metrics_summary)
    st.write(summary)

    # ── Download ──
    st.download_button(
        label="📥 Download Report",
        data=filtered_df.to_csv(index=False),
        file_name="social_media_report.csv",
        mime="text/csv"
    )