import streamlit as st
import os
# ── Custom CSS ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Space+Grotesk:wght@400;500;600&display=swap');

* { font-family: 'DM Sans', sans-serif; }

/* ── App Background ── */
.stApp {
    background: #F7F8FC;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #FFFFFF;
    border-right: 1px solid #EAEEF5;
}
[data-testid="stSidebar"] .stRadio label {
    display: flex;
    align-items: center;
    padding: 10px 14px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 500;
    color: #64748B;
    cursor: pointer;
    transition: all 0.2s ease;
    margin: 2px 0;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: #F1F5FF;
    color: #4338CA;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #64748B;
    font-size: 13px;
}
[data-testid="stSidebar"] h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 16px !important;
    font-weight: 600 !important;
    color: #1E293B !important;
    letter-spacing: -0.3px;
}

/* ── Main Content ── */
.main .block-container {
    padding: 2rem 2.5rem;
    animation: fadeUp 0.4s ease forwards;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ── Headings ── */
h1 {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 28px !important;
    font-weight: 600 !important;
    color: #1E293B !important;
    letter-spacing: -0.5px !important;
    -webkit-text-fill-color: #1E293B !important;
    margin-bottom: 0.25rem !important;
}
h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #1E293B !important;
    font-weight: 500 !important;
}

/* ── Subheader ── */
[data-testid="stSubheader"] {
    color: #64748B !important;
    font-size: 14px !important;
    font-weight: 400 !important;
}

/* ── Input Fields ── */
.stTextInput label, .stSelectbox label,
.stMultiSelect label, .stTextArea label {
    font-size: 13px !important;
    font-weight: 500 !important;
    color: #475569 !important;
    margin-bottom: 4px !important;
}
.stTextInput input {
    border: 1.5px solid #E2E8F0 !important;
    border-radius: 10px !important;
    padding: 10px 14px !important;
    font-size: 14px !important;
    background: #FFFFFF !important;
    color: #1E293B !important;
    transition: all 0.2s ease !important;
}
.stTextInput input:focus {
    border-color: #4338CA !important;
    box-shadow: 0 0 0 3px rgba(67,56,202,0.1) !important;
}
.stTextInput input::placeholder { color: #94A3B8 !important; }

/* ── Select / Dropdown ── */
[data-baseweb="select"] {
    border-radius: 10px !important;
}
[data-baseweb="select"] > div {
    border: 1.5px solid #E2E8F0 !important;
    border-radius: 10px !important;
    background: #FFFFFF !important;
    color: #1E293B !important;
    font-size: 14px !important;
    transition: all 0.2s ease !important;
}
[data-baseweb="select"] > div:focus-within {
    border-color: #4338CA !important;
    box-shadow: 0 0 0 3px rgba(67,56,202,0.1) !important;
}

/* ── Multiselect ── */
[data-baseweb="tag"] {
    background: #EEF2FF !important;
    border-radius: 6px !important;
    color: #4338CA !important;
    font-size: 12px !important;
}

/* ── Buttons ── */
.stButton > button {
    background: #4338CA !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 12px 24px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    font-family: 'DM Sans', sans-serif !important;
    letter-spacing: 0.2px !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 12px rgba(67,56,202,0.25) !important;
}
.stButton > button:hover {
    background: #3730A3 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(67,56,202,0.35) !important;
}
.stButton > button:active {
    transform: translateY(0px) !important;
}

/* ── Metric Cards ── */
[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 1px solid #EEF2FF !important;
    border-radius: 14px !important;
    padding: 1.25rem !important;
    border-left: 4px solid #4338CA !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(67,56,202,0.1) !important;
}
[data-testid="stMetricLabel"] {
    font-size: 12px !important;
    color: #64748B !important;
    font-weight: 500 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 28px !important;
    font-weight: 600 !important;
    color: #1E293B !important;
}

/* ── Info / Success / Warning boxes ── */
[data-testid="stInfo"] {
    background: #F8FAFF !important;
    border: 1px solid #E0E7FF !important;
    border-radius: 14px !important;
    color: #1E293B !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}
[data-testid="stInfo"]:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 24px rgba(67,56,202,0.08) !important;
}
[data-testid="stSuccess"] {
    background: #F0FDF4 !important;
    border: 1px solid #BBF7D0 !important;
    border-radius: 14px !important;
    color: #166534 !important;
}
[data-testid="stWarning"] {
    background: #FFFBEB !important;
    border: 1px solid #FDE68A !important;
    border-radius: 14px !important;
    color: #92400E !important;
}

/* ── Divider ── */
hr {
    border: none !important;
    border-top: 1px solid #EEF2FF !important;
    margin: 1.5rem 0 !important;
}

/* ── Dataframe ── */
[data-testid="stDataFrame"] {
    border-radius: 14px !important;
    overflow: hidden !important;
    border: 1px solid #EEF2FF !important;
}

/* ── Spinner ── */
.stSpinner > div {
    border-top-color: #4338CA !important;
}

/* ── Download Button ── */
.stDownloadButton > button {
    background: #FFFFFF !important;
    color: #4338CA !important;
    border: 1.5px solid #4338CA !important;
    border-radius: 10px !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
}
.stDownloadButton > button:hover {
    background: #EEF2FF !important;
    transform: translateY(-1px) !important;
}

/* ── Plotly Charts ── */
.js-plotly-plot {
    border-radius: 14px !important;
    overflow: hidden !important;
    border: 1px solid #EEF2FF !important;
}

/* ── Progress Bar ── */
.stProgress > div > div {
    background: #4338CA !important;
    border-radius: 10px !important;
}

/* ── Text Area ── */
.stTextArea textarea {
    border: 1.5px solid #E2E8F0 !important;
    border-radius: 10px !important;
    font-size: 14px !important;
    background: #FFFFFF !important;
    color: #1E293B !important;
    transition: all 0.2s ease !important;
}
.stTextArea textarea:focus {
    border-color: #4338CA !important;
    box-shadow: 0 0 0 3px rgba(67,56,202,0.1) !important;
}
</style>
""", unsafe_allow_html=True)
# ── Page Config ──
st.set_page_config(
    page_title="AI Marketing Suite",
    page_icon="🤖",
    layout="wide"
)

# ── Sidebar ──
st.sidebar.title("🤖 AI Marketing Suite")
st.sidebar.markdown("**by Siddharth Ganesh**")
st.sidebar.divider()

page = st.sidebar.radio("Navigate", [
    "🏠 Home",
    "🤖 AI Content Generator",
    "🔍 SEO Keyword Analyzer",
    "📊 Social Media Dashboard",
    "🧪 A/B Testing Simulator"
])

st.sidebar.divider()
st.sidebar.markdown("Built with Python + Gemini AI")
st.sidebar.markdown("[GitHub](https://github.com/sidji-g98)")

# ── Home Page ──
if page == "🏠 Home":
    st.title("🤖 AI Marketing Suite")
    st.subheader("by Siddharth Ganesh")
    st.divider()
    st.markdown("""
    ### Welcome! 👋
    This is a collection of AI-powered digital marketing tools
    built using Python and Google Gemini AI.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.info("**🤖 AI Content Generator**\n\nGenerate Instagram captions, LinkedIn posts, email copy and more in seconds.")
        st.info("**🔍 SEO Keyword Analyzer**\n\nAnalyze keyword performance and get AI-powered content suggestions.")
    with col2:
        st.info("**📊 Social Media Dashboard**\n\nVisualize engagement metrics and get AI weekly performance summaries.")
        st.info("**🧪 A/B Testing Simulator**\n\nCompare two marketing variants and get AI-powered winner predictions.")
    st.divider()
    st.success("👈 Select a tool from the sidebar to get started!")

# ── Module 1 ──
elif page == "🤖 AI Content Generator":
    from google import genai
    import time
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    def generate_content(brand_name, niche, tone, audience, content_type):
        prompt = f"""
        You are a digital marketing expert.
        Brand: {brand_name} | Niche: {niche}
        Tone: {tone} | Audience: {audience}
        Generate: {content_type}
        Be concise, creative, and on-brand.
        """
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash", contents=prompt)
                return response.text
            except Exception as e:
                if "429" in str(e):
                    time.sleep(30)
                else:
                    raise e
        return "Error generating content."

    st.title("🤖 AI Content Generator")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        brand_name = st.text_input("Brand Name", placeholder="e.g. EcoWear")
        niche = st.text_input("Niche / Industry", placeholder="e.g. Sustainable Fashion")
    with col2:
        tone = st.selectbox("Tone of Voice", ["Friendly", "Professional", "Witty", "Inspirational"])
        audience = st.text_input("Target Audience", placeholder="e.g. Millennials")
    content_type = st.multiselect("What do you want to generate?", [
        "3 Instagram captions with hashtags",
        "1 LinkedIn post",
        "Email newsletter intro",
        "Blog post outline",
        "3 Google Ad headline variants"
    ])
    if st.button("✨ Generate Content", use_container_width=True):
        if brand_name and niche and audience and content_type:
            for item in content_type:
                st.markdown(f"### {item}")
                with st.spinner(f"Generating {item}..."):
                    result = generate_content(brand_name, niche, tone, audience, item)
                st.write(result)
                st.divider()
        else:
            st.warning("Please fill in all fields!")

# ── Module 2 ──
elif page == "🔍 SEO Keyword Analyzer":
    from google import genai
    import pandas as pd
    import plotly.express as px
    import ast
    import time
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    def get_mock_data(niche):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Generate 10 realistic SEO keywords for: {niche}. Return ONLY a Python list like: ['keyword 1', 'keyword 2']. Nothing else.")
            keywords = ast.literal_eval(response.text.strip())
        except:
            keywords = ["keyword 1","keyword 2","keyword 3","keyword 4","keyword 5",
                       "keyword 6","keyword 7","keyword 8","keyword 9","keyword 10"]
        return pd.DataFrame({
            "Keyword": keywords[:10],
            "Clicks": [320,280,210,190,175,160,145,130,120,110],
            "Impressions": [4200,3800,3100,2900,2600,2400,2100,1900,1800,1600],
            "CTR": [7.6,7.4,6.8,6.5,6.7,6.7,6.9,6.8,6.7,6.9],
            "Position": [3.2,3.8,4.1,4.5,4.3,4.6,4.8,5.1,5.3,5.5]
        })

    def get_ai_suggestions(keywords):
        prompt = f"""You are an SEO expert. Based on these keywords: {', '.join(keywords)}
        Provide: 5 Blog titles, 3 Meta descriptions, 3 Content gaps, 2 Long-tail keywords."""
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash", contents=prompt)
                return response.text
            except Exception as e:
                if "429" in str(e):
                    time.sleep(30)
                else:
                    raise e
        return "Error generating suggestions."

    st.title("🔍 SEO Keyword Analyzer")
    st.divider()
    website = st.text_input("Enter your website/niche", placeholder="e.g. sustainable fashion blog")
    if st.button("🔍 Analyze Keywords", use_container_width=True):
        if website:
            df = get_mock_data(website)
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Clicks", f"{df['Clicks'].sum():,}")
            col2.metric("Total Impressions", f"{df['Impressions'].sum():,}")
            col3.metric("Avg CTR", f"{df['CTR'].mean():.1f}%")
            col4.metric("Avg Position", f"{df['Position'].mean():.1f}")
            fig = px.bar(df.head(8), x="Keyword", y="Clicks", color="CTR",
                        color_continuous_scale="Blues")
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df, use_container_width=True)
            st.divider()
            st.markdown("### AI Content Suggestions")
            with st.spinner("Generating suggestions..."):
                suggestions = get_ai_suggestions(df["Keyword"].tolist())
            st.write(suggestions)
        else:
            st.warning("Please enter your website or niche!")

# ── Module 3 ──
elif page == "📊 Social Media Dashboard":
    from google import genai
    import pandas as pd
    import plotly.express as px
    import time
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    def get_mock_social_data():
        return pd.DataFrame({
            "Date": pd.date_range(start="2026-04-01", periods=30, freq="D"),
            "Platform": ["Instagram"]*10 + ["LinkedIn"]*10 + ["Twitter"]*10,
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

    st.title("📊 Social Media Dashboard")
    st.divider()
    platform = st.selectbox("Select Platform",
                             ["All Platforms","Instagram","LinkedIn","Twitter"])
    if st.button("📊 Generate Dashboard", use_container_width=True):
        df = get_mock_social_data()
        df["Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]
        df["Engagement_Rate"] = (df["Engagement"] / df["Reach"] * 100).round(2)
        filtered_df = df if platform == "All Platforms" else df[df["Platform"] == platform]
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Likes", f"{filtered_df['Likes'].sum():,}")
        col2.metric("Total Reach", f"{filtered_df['Reach'].sum():,}")
        col3.metric("Avg Engagement Rate", f"{filtered_df['Engagement_Rate'].mean():.1f}%")
        col4.metric("Total Posts", len(filtered_df))
        fig1 = px.line(filtered_df, x="Date", y="Engagement_Rate",
                       color="Platform" if platform == "All Platforms" else None,
                       title="Daily Engagement Rate (%)")
        st.plotly_chart(fig1, use_container_width=True)
        post_perf = filtered_df.groupby("Post_Type")["Engagement_Rate"].mean().reset_index()
        fig2 = px.bar(post_perf, x="Post_Type", y="Engagement_Rate",
                      color="Engagement_Rate", color_continuous_scale="Greens")
        st.plotly_chart(fig2, use_container_width=True)
        st.divider()
        st.markdown("### AI Weekly Summary")
        metrics = f"Platform: {platform}, Likes: {filtered_df['Likes'].sum()}, Reach: {filtered_df['Reach'].sum()}, Avg Engagement: {filtered_df['Engagement_Rate'].mean():.1f}%"
        with st.spinner("Generating summary..."):
            for attempt in range(3):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=f"You are a social media expert. Write a weekly performance summary and 3 recommendations based on: {metrics}")
                    st.write(response.text)
                    break
                except Exception as e:
                    if "429" in str(e):
                        time.sleep(30)
                    else:
                        raise e

# ── Module 4 ──
elif page == "🧪 A/B Testing Simulator":
    from google import genai
    import plotly.graph_objects as go
    import time
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    def analyze_variant(text, content_type):
        prompt = f"""Analyze this {content_type}: "{text}"
        Score out of 10 for each:
        CLARITY: X/10
        EMOTIONAL_APPEAL: X/10
        URGENCY: X/10
        CTA_STRENGTH: X/10
        RELEVANCE: X/10
        OVERALL: X/10
        STRENGTHS: strength1 | strength2
        WEAKNESSES: weakness1 | weakness2
        SUGGESTION: suggestion here"""
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash", contents=prompt)
                return response.text
            except Exception as e:
                if "429" in str(e):
                    time.sleep(30)
                else:
                    raise e
        return "Error analyzing."

    def parse_scores(text):
        scores = {}
        for line in text.split('\n'):
            for metric in ["CLARITY","EMOTIONAL_APPEAL","URGENCY","CTA_STRENGTH","RELEVANCE","OVERALL"]:
                if line.startswith(metric):
                    try:
                        scores[metric] = float(line.split(":")[1].strip().split("/")[0])
                    except:
                        scores[metric] = 0
        return scores

    st.title("🧪 A/B Testing Simulator")
    st.divider()
    content_type = st.selectbox("What are you testing?", [
        "Email Subject Line","Ad Headline","Call to Action Button",
        "Social Media Caption","Landing Page Headline"])
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Variant A**")
        variant_a = st.text_area("Version A", placeholder="e.g. Get 50% off today only!", height=100)
    with col2:
        st.markdown("**Variant B**")
        variant_b = st.text_area("Version B", placeholder="e.g. Limited time: Half price ends tonight!", height=100)

    if st.button("🧪 Run A/B Test", use_container_width=True):
        if variant_a and variant_b:
            col1, col2 = st.columns(2)
            with col1:
                with st.spinner("Analyzing Variant A..."):
                    analysis_a = analyze_variant(variant_a, content_type)
                scores_a = parse_scores(analysis_a)
            with col2:
                with st.spinner("Analyzing Variant B..."):
                    analysis_b = analyze_variant(variant_b, content_type)
                scores_b = parse_scores(analysis_b)
            categories = ["Clarity","Emotional Appeal","Urgency","CTA Strength","Relevance"]
            keys = ["CLARITY","EMOTIONAL_APPEAL","URGENCY","CTA_STRENGTH","RELEVANCE"]
            values_a = [scores_a.get(k, 0) for k in keys]
            values_b = [scores_b.get(k, 0) for k in keys]
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(r=values_a+[values_a[0]],
                theta=categories+[categories[0]], fill='toself',
                name='Variant A', line_color='blue'))
            fig.add_trace(go.Scatterpolar(r=values_b+[values_b[0]],
                theta=categories+[categories[0]], fill='toself',
                name='Variant B', line_color='red'))
            fig.update_layout(polar=dict(radialaxis=dict(range=[0,10])))
            st.plotly_chart(fig, use_container_width=True)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Variant A**")
                st.metric("Overall Score", f"{scores_a.get('OVERALL',0)}/10")
            with col2:
                st.markdown("**Variant B**")
                st.metric("Overall Score", f"{scores_b.get('OVERALL',0)}/10")
            overall_a = scores