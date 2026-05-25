import streamlit as st
import os

GEMINI_API_KEY = (
    st.secrets.get("GEMINI_API_KEY") 
    or os.environ.get("GEMINI_API_KEY") 
    or ""
)
# ── Custom CSS ──
st.markdown("""
<style>
/* ── Progress Bar Text ── */
    .stProgress > div > div > div > div {
        color: #1E293B !important;
    }
    [data-testid="stProgressBar"] {
        background: #EEF2FF !important;
    }
    .stProgress p {
        color: #1E293B !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        margin-bottom: 4px !important;
    }
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
    client = genai.Client(api_key=GEMINI_API_KEY)

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
    import time
    client = genai.Client(api_key=GEMINI_API_KEY)

    def get_full_seo_analysis(niche):
        prompt = f"""You are an SEO expert specializing in "{niche}".

Generate a complete SEO analysis with these exact sections:

KEYWORDS:
List 10 real specific keywords for "{niche}" separated by commas on one line.

BLOG TITLES:
1. [Real title using actual keywords]
2. [Real title using actual keywords]
3. [Real title using actual keywords]
4. [Real title using actual keywords]
5. [Real title using actual keywords]

META DESCRIPTIONS:
1. [Real 150-character meta description]
2. [Real 150-character meta description]
3. [Real 150-character meta description]

CONTENT GAPS:
1. [Specific topic not covered well online]
2. [Specific topic not covered well online]
3. [Specific topic not covered well online]

LONG-TAIL KEYWORDS:
1. [Specific long-tail keyword phrase]
2. [Specific long-tail keyword phrase]

Use ONLY real keywords related to "{niche}". Never use placeholder text."""
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash", contents=prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

    st.title("🔍 SEO Keyword Analyzer")
    st.divider()
    website = st.text_input("Enter your website/niche",
                             placeholder="e.g. sustainable fashion blog")

    if st.button("🔍 Analyze Keywords", use_container_width=True):
        if website:
            with st.spinner("Generating full SEO analysis..."):
                full_analysis = get_full_seo_analysis(website)

            if "Error" not in full_analysis:
                try:
                    keywords_section = full_analysis.split("KEYWORDS:")[1].split("BLOG TITLES:")[0].strip()
                    keywords = [k.strip() for k in keywords_section.replace("\n", ",").split(",") if k.strip()][:10]
                except:
                    keywords = ["keyword " + str(i) for i in range(1, 11)]

                if len(keywords) < 10:
                    keywords += ["keyword " + str(i) for i in range(len(keywords)+1, 11)]

                df = pd.DataFrame({
                    "Keyword": keywords[:10],
                    "Clicks": [320,280,210,190,175,160,145,130,120,110],
                    "Impressions": [4200,3800,3100,2900,2600,2400,2100,1900,1800,1600],
                    "CTR": [7.6,7.4,6.8,6.5,6.7,6.7,6.9,6.8,6.7,6.9],
                    "Position": [3.2,3.8,4.1,4.5,4.3,4.6,4.8,5.1,5.3,5.5]
                })

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
                st.write(full_analysis)
            else:
                st.error(full_analysis)
        else:
            st.warning("Please enter your website or niche!")

# ── Module 3 ──
elif page == "📊 Social Media Dashboard":
    from google import genai
    import pandas as pd
    import plotly.express as px
    import time
    import io
    client = genai.Client(api_key=GEMINI_API_KEY)

    st.title("📊 Social Media Dashboard")
    st.divider()

    # ── Input Method ──
    st.markdown("### How do you want to add your data?")
    input_method = st.radio("", [
        "📊 Use sample data (demo)",
        "✏️ Enter my own metrics manually",
        "📁 Upload my CSV file"
    ], horizontal=True)

    df = None

    # ── Option 1: Sample Data ──
    if input_method == "📊 Use sample data (demo)":
        platform_filter = st.selectbox("Select Platform",
                         ["All Platforms","Instagram","LinkedIn","Twitter"])
        df = pd.DataFrame({
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
        if platform_filter != "All Platforms":
            df = df[df["Platform"] == platform_filter]

    # ── Option 2: Manual Entry ──
    elif input_method == "✏️ Enter my own metrics manually":
        st.markdown("### Enter Your Social Media Metrics")
        brand = st.text_input("Brand / Account Name", placeholder="e.g. EcoWear India")
        platform_filter = st.selectbox("Platform", ["Instagram","LinkedIn","Twitter","Facebook"])
        col1, col2 = st.columns(2)
        with col1:
            total_likes = st.number_input("Total Likes (this week)", min_value=0, value=500)
            total_comments = st.number_input("Total Comments", min_value=0, value=80)
            total_shares = st.number_input("Total Shares", min_value=0, value=45)
        with col2:
            total_reach = st.number_input("Total Reach", min_value=0, value=8000)
            total_posts = st.number_input("Number of Posts", min_value=1, value=7)
            best_post_type = st.selectbox("Best Performing Post Type",
                ["Reel", "Carousel", "Image", "Video", "Story",
                 "Article", "Poll", "Thread"])

        if st.button("📊 Generate Dashboard", use_container_width=True):
            engagement = total_likes + total_comments + total_shares
            engagement_rate = round((engagement / total_reach * 100), 2) if total_reach > 0 else 0

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Likes", f"{total_likes:,}")
            col2.metric("Total Reach", f"{total_reach:,}")
            col3.metric("Engagement Rate", f"{engagement_rate}%")
            col4.metric("Total Posts", total_posts)

            fig = px.bar(
                x=["Likes", "Comments", "Shares"],
                y=[total_likes, total_comments, total_shares],
                color=["Likes", "Comments", "Shares"],
                color_discrete_sequence=["#4338CA", "#818CF8", "#C7D2FE"],
                title="Engagement Breakdown"
            )
            st.plotly_chart(fig, use_container_width=True)

            st.divider()
            st.markdown("### AI Weekly Summary")
            metrics = f"""
            Brand: {brand}
            Platform: {platform_filter}
            Total Likes: {total_likes}
            Total Comments: {total_comments}
            Total Shares: {total_shares}
            Total Reach: {total_reach}
            Engagement Rate: {engagement_rate}%
            Best Post Type: {best_post_type}
            Total Posts: {total_posts}
            """
            with st.spinner("Generating AI summary..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=f"""You are a social media expert.
                        Write a friendly weekly performance summary and
                        3 specific actionable recommendations based on: {metrics}""")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

        st.stop()

    # ── Option 3: CSV Upload ──
    elif input_method == "📁 Upload my CSV file":
        st.markdown("### Upload Your Data")
        st.info("CSV must have columns: Date, Platform, Likes, Comments, Shares, Reach, Post_Type")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        platform_filter = "All Platforms"

        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.success(f"Loaded {len(df)} rows of data!")
            platform_options = ["All Platforms"] + df["Platform"].unique().tolist()
            platform_filter = st.selectbox("Filter by Platform", platform_options)
            if platform_filter != "All Platforms":
                df = df[df["Platform"] == platform_filter]
        else:
            st.warning("Please upload a CSV file to continue.")
            st.stop()

    # ── Dashboard (for Sample + CSV) ──
    if df is not None and input_method != "✏️ Enter my own metrics manually":
        df["Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]
        df["Engagement_Rate"] = (df["Engagement"] / df["Reach"] * 100).round(2)

        if st.button("📊 Generate Dashboard", use_container_width=True):

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Likes", f"{df['Likes'].sum():,}")
            col2.metric("Total Reach", f"{df['Reach'].sum():,}")
            col3.metric("Avg Engagement Rate",
                        f"{df['Engagement_Rate'].mean():.1f}%")
            col4.metric("Total Posts", len(df))

            st.divider()

            fig1 = px.line(df, x="Date", y="Engagement_Rate",
                           color="Platform" if "Platform" in df.columns else None,
                           title="Engagement Rate Over Time",
                           color_discrete_sequence=["#4338CA","#818CF8","#C7D2FE"])
            st.plotly_chart(fig1, use_container_width=True)

            if "Post_Type" in df.columns:
                post_perf = df.groupby("Post_Type")["Engagement_Rate"].mean().reset_index()
                fig2 = px.bar(post_perf, x="Post_Type", y="Engagement_Rate",
                              color="Engagement_Rate",
                              color_continuous_scale="Blues",
                              title="Avg Engagement Rate by Post Type")
                st.plotly_chart(fig2, use_container_width=True)

            if "Platform" in df.columns:
                plat_perf = df.groupby("Platform")[["Likes","Comments","Shares"]].sum().reset_index()
                fig3 = px.bar(plat_perf, x="Platform",
                              y=["Likes","Comments","Shares"],
                              title="Total Engagement by Platform",
                              barmode="group",
                              color_discrete_sequence=["#4338CA","#818CF8","#C7D2FE"])
                st.plotly_chart(fig3, use_container_width=True)

            st.divider()
            st.markdown("### AI Weekly Summary")
            metrics = f"""
            Total Likes: {df['Likes'].sum()}
            Total Reach: {df['Reach'].sum()}
            Avg Engagement Rate: {df['Engagement_Rate'].mean():.1f}%
            Best Post Type: {df.groupby('Post_Type')['Engagement_Rate'].mean().idxmax() if 'Post_Type' in df.columns else 'N/A'}
            Total Posts: {len(df)}
            """
            with st.spinner("Generating AI summary..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=f"""You are a social media expert.
                        Write a weekly performance summary and
                        3 actionable recommendations based on: {metrics}""")
                    st.write(response.text)
                except Exception as e:
                    if "429" in str(e):
                        time.sleep(30)
                        try:
                            response = client.models.generate_content(
                                model="gemini-2.5-flash",
                                contents=f"Social media summary for: {metrics}")
                            st.write(response.text)
                        except:
                            st.warning("Rate limit hit. Please try again in 1 minute.")
                    else:
                        st.error(f"Error: {str(e)}")

            st.download_button(
                label="📥 Download Report",
                data=df.to_csv(index=False),
                file_name="social_media_report.csv",
                mime="text/csv"
            )

# ── Module 4 ──
elif page == "🧪 A/B Testing Simulator":
    from google import genai
    import plotly.graph_objects as go
    import plotly.express as px
    import time
    client = genai.Client(api_key=GEMINI_API_KEY)

    def analyze_variants(variant_a, variant_b, content_type, industry,
                         target_market, audience_age, campaign_goal):
        prompt = f"""You are a world-class conversion rate optimization expert.

Compare these two {content_type} variants for a {industry} brand:

VARIANT A: "{variant_a}"
VARIANT B: "{variant_b}"

Context:
- Target Market: {target_market}
- Audience Age Group: {audience_age}
- Campaign Goal: {campaign_goal}
- Industry: {industry}

Score EACH variant out of 10 for ALL these factors:

VARIANT_A_CLARITY: X/10
VARIANT_A_EMOTIONAL_APPEAL: X/10
VARIANT_A_URGENCY: X/10
VARIANT_A_CTA_STRENGTH: X/10
VARIANT_A_RELEVANCE: X/10
VARIANT_A_CULTURAL_FIT: X/10
VARIANT_A_OVERALL: X/10

VARIANT_B_CLARITY: X/10
VARIANT_B_EMOTIONAL_APPEAL: X/10
VARIANT_B_URGENCY: X/10
VARIANT_B_CTA_STRENGTH: X/10
VARIANT_B_RELEVANCE: X/10
VARIANT_B_CULTURAL_FIT: X/10
VARIANT_B_OVERALL: X/10

WINNER: [A or B]
WIN_REASON: [2 sentences explaining why]

VARIANT_A_STRENGTHS: strength1 | strength2
VARIANT_A_WEAKNESSES: weakness1 | weakness2
VARIANT_A_IMPROVEMENT: one specific improvement

VARIANT_B_STRENGTHS: strength1 | strength2
VARIANT_B_WEAKNESSES: weakness1 | weakness2
VARIANT_B_IMPROVEMENT: one specific improvement

RECOMMENDATION: [3-4 sentences of actionable next steps]
PLATFORM_BEST_FOR_A: [best platform for variant A]
PLATFORM_BEST_FOR_B: [best platform for variant B]"""

        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash", contents=prompt)
                return response.text
            except Exception as e:
                if "429" in str(e):
                    time.sleep(30)
                else:
                    return f"Error: {str(e)}"
        return "Error: Max retries reached."

    def parse_scores(text, prefix):
        scores = {}
        metrics = ["CLARITY","EMOTIONAL_APPEAL","URGENCY",
                   "CTA_STRENGTH","RELEVANCE","CULTURAL_FIT","OVERALL"]
        lines = text.split('\n')
        for line in lines:
            clean = line.strip().replace("**","").replace("*","")
            for metric in metrics:
                key = f"{prefix}_{metric}"
                if clean.startswith(key + ":"):
                    try:
                        score = float(clean.split(":")[1].strip().split("/")[0])
                        scores[metric] = score
                    except:
                        pass
        return scores

    def extract_field(text, field):
        for line in text.split('\n'):
            clean = line.strip().replace("**","").replace("*","")
            if clean.startswith(field + ":"):
               parts = clean.split(":", 1)
               if len(parts) >= 2:
                    return parts[1].strip()
        return ""
    
  
    # ── UI ──
    st.title("🧪 A/B Testing Simulator")
    st.markdown("*Compare any two marketing variants with AI-powered analysis*")
    st.divider()

    # ── Context Settings ──
    st.markdown("### Campaign Context")
    col1, col2 = st.columns(2)
    with col1:
        industry = st.selectbox("Industry", [
            "E-commerce / Retail",
            "Food & Beverage",
            "Fashion & Apparel",
            "Technology / SaaS",
            "Healthcare & Wellness",
            "Education & EdTech",
            "Finance & Banking",
            "Travel & Hospitality",
            "Real Estate",
            "Beauty & Personal Care",
            "Fitness & Sports",
            "Entertainment & Media"
        ])
        target_market = st.selectbox("Target Market", [
            "India — Tier 1 Cities",
            "India — Tier 2 & 3 Cities",
            "India — Pan India",
            "United States",
            "United Kingdom",
            "Southeast Asia",
            "Middle East",
            "Europe",
            "Global / International"
        ])
    with col2:
        audience_age = st.selectbox("Target Age Group", [
            "Gen Z (18–24)",
            "Millennials (25–34)",
            "Young Professionals (25–40)",
            "Adults (35–50)",
            "Senior Adults (50+)",
            "All Ages"
        ])
        campaign_goal = st.selectbox("Campaign Goal", [
            "Drive Sales / Conversions",
            "Build Brand Awareness",
            "Increase Engagement",
            "Generate Leads",
            "Customer Retention",
            "App Downloads",
            "Website Traffic",
            "Event Registration"
        ])

    st.divider()

    # ── Content Type ──
    st.markdown("### What Are You Testing?")
    content_type = st.selectbox("Content Type", [
        "Email Subject Line",
        "Ad Headline",
        "Call to Action Button",
        "Social Media Caption",
        "Landing Page Headline",
        "Push Notification",
        "SMS Message",
        "WhatsApp Message",
        "Product Description",
        "Google Ad Copy",
        "YouTube Ad Script (first 5 seconds)",
        "Instagram Bio"
    ])

    st.divider()

    # ── Variants ──
    st.markdown("### Enter Your Two Variants")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🅐 Variant A**")
        variant_a = st.text_area("Version A",
            placeholder="e.g. Get 50% off today only!",
            height=120)
    with col2:
        st.markdown("**🅑 Variant B**")
        variant_b = st.text_area("Version B",
            placeholder="e.g. Limited time: Half price ends tonight!",
            height=120)

    st.divider()

    if st.button("🧪 Run A/B Test", use_container_width=True):
        if variant_a and variant_b:
            with st.spinner("Analyzing both variants with AI..."):
                analysis = analyze_variants(
                    variant_a, variant_b, content_type,
                    industry, target_market, audience_age, campaign_goal
                )

            if "Error" not in analysis:
                with st.expander("🔍 Raw AI Response (debug)"):
                    st.text(analysis)
                scores_a = parse_scores(analysis, "VARIANT_A")
                scores_b = parse_scores(analysis, "VARIANT_B")
                winner = extract_field(analysis, "WINNER")
                win_reason = extract_field(analysis, "WIN_REASON")
                recommendation = extract_field(analysis, "RECOMMENDATION")
                platform_a = extract_field(analysis, "PLATFORM_BEST_FOR_A")
                platform_b = extract_field(analysis, "PLATFORM_BEST_FOR_B")

                # ── Winner Banner ──
                st.divider()
                if "A" in winner:
                    st.success(f"🏆 **Variant A Wins!** — {win_reason}")
                elif "B" in winner:
                    st.success(f"🏆 **Variant B Wins!** — {win_reason}")
                else:
                    st.info("🤝 It's a tie! Both variants are equally strong.")

                # ── Score Cards ──
                st.divider()
                st.markdown("### Score Comparison")

                metrics_labels = {
                    "CLARITY": "Clarity",
                    "EMOTIONAL_APPEAL": "Emotional Appeal",
                    "URGENCY": "Urgency",
                    "CTA_STRENGTH": "CTA Strength",
                    "RELEVANCE": "Relevance",
                    "CULTURAL_FIT": "Cultural Fit",
                    "OVERALL": "Overall"
                }

                table_html = """
                <table style="width:100%; border-collapse:collapse; font-family:'DM Sans',sans-serif;">
                    <thead>
                        <tr style="background:#4338CA; color:white;">
                            <th style="padding:12px 16px; text-align:left; border-radius:8px 0 0 0;">Metric</th>
                            <th style="padding:12px 16px; text-align:center;">🅐 Variant A</th>
                            <th style="padding:12px 16px; text-align:center; border-radius:0 8px 0 0;">🅑 Variant B</th>
                        </tr>
                    </thead>
                    <tbody>
                """

                for i, (key, label) in enumerate(metrics_labels.items()):
                    score_a = scores_a.get(key, 0)
                    score_b = scores_b.get(key, 0)
                    bg = "#F8FAFF" if i % 2 == 0 else "#FFFFFF"

                    if key == "OVERALL":
                        row_style = "font-weight:600; background:#EEF2FF;"
                    else:
                        row_style = f"background:{bg};"

                    if score_a > score_b:
                        color_a = "#166534"
                        color_b = "#991B1B"
                        icon_a = "✅"
                        icon_b = ""
                    elif score_b > score_a:
                        color_a = "#991B1B"
                        color_b = "#166534"
                        icon_a = ""
                        icon_b = "✅"
                    else:
                        color_a = color_b = "#1E293B"
                        icon_a = icon_b = "="

                    table_html += f"""
                        <tr style="{row_style}">
                            <td style="padding:10px 16px; color:#475569; border-bottom:1px solid #EEF2FF;">{label}</td>
                            <td style="padding:10px 16px; text-align:center; color:{color_a}; border-bottom:1px solid #EEF2FF;">
                                {icon_a} <strong>{score_a}/10</strong>
                            </td>
                            <td style="padding:10px 16px; text-align:center; color:{color_b}; border-bottom:1px solid #EEF2FF;">
                                {icon_b} <strong>{score_b}/10</strong>
                            </td>
                        </tr>
                    """

                table_html += "</tbody></table>"
                st.markdown(table_html, unsafe_allow_html=True)
                

                # ── Radar Chart ──
                st.divider()
                st.markdown("### Visual Comparison")
                categories = ["Clarity", "Emotional Appeal", "Urgency",
                              "CTA Strength", "Relevance", "Cultural Fit"]
                keys = ["CLARITY","EMOTIONAL_APPEAL","URGENCY",
                        "CTA_STRENGTH","RELEVANCE","CULTURAL_FIT"]
                values_a = [scores_a.get(k, 0) for k in keys]
                values_b = [scores_b.get(k, 0) for k in keys]

                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(
                    r=values_a + [values_a[0]],
                    theta=categories + [categories[0]],
                    fill='toself', name='Variant A',
                    line_color='#4338CA',
                    fillcolor='rgba(67,56,202,0.15)'))
                fig.add_trace(go.Scatterpolar(
                    r=values_b + [values_b[0]],
                    theta=categories + [categories[0]],
                    fill='toself', name='Variant B',
                    line_color='#EC4899',
                    fillcolor='rgba(236,72,153,0.15)'))
                fig.update_layout(
                    polar=dict(radialaxis=dict(range=[0,10])),
                    showlegend=True,
                    height=450
                )
                st.plotly_chart(fig, use_container_width=True)

                # ── Bar Chart Comparison ──
                comparison_df = {
                    "Metric": categories * 2,
                    "Score": values_a + values_b,
                    "Variant": ["Variant A"] * 6 + ["Variant B"] * 6
                }
                fig2 = px.bar(comparison_df, x="Metric", y="Score",
                              color="Variant", barmode="group",
                              color_discrete_sequence=["#4338CA","#EC4899"],
                              title="Side-by-Side Score Breakdown")
                st.plotly_chart(fig2, use_container_width=True)

                # ── Detailed Analysis ──
                st.divider()
                st.markdown("### Detailed Analysis")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**🅐 Variant A**")
                    strengths_a = extract_field(analysis, "VARIANT_A_STRENGTHS")
                    weaknesses_a = extract_field(analysis, "VARIANT_A_WEAKNESSES")
                    improvement_a = extract_field(analysis, "VARIANT_A_IMPROVEMENT")
                    if strengths_a:
                        st.success(f"✅ **Strengths:** {strengths_a}")
                    if weaknesses_a:
                        st.warning(f"⚠️ **Weaknesses:** {weaknesses_a}")
                    if improvement_a:
                        st.info(f"💡 **Improvement:** {improvement_a}")
                    if platform_a:
                        st.markdown(f"📱 **Best Platform:** {platform_a}")
                with col2:
                    st.markdown("**🅑 Variant B**")
                    strengths_b = extract_field(analysis, "VARIANT_B_STRENGTHS")
                    weaknesses_b = extract_field(analysis, "VARIANT_B_WEAKNESSES")
                    improvement_b = extract_field(analysis, "VARIANT_B_IMPROVEMENT")
                    if strengths_b:
                        st.success(f"✅ **Strengths:** {strengths_b}")
                    if weaknesses_b:
                        st.warning(f"⚠️ **Weaknesses:** {weaknesses_b}")
                    if improvement_b:
                        st.info(f"💡 **Improvement:** {improvement_b}")
                    if platform_b:
                        st.markdown(f"📱 **Best Platform:** {platform_b}")

                # ── Recommendation ──
                if recommendation:
                    st.divider()
                    st.markdown("### AI Recommendation")
                    st.info(f"🎯 {recommendation}")

            else:
                st.error(analysis)
        else:
            st.warning("Please enter both variants!")
