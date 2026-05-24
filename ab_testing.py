from google import genai
import streamlit as st
import plotly.graph_objects as go
import time
import os

client = genai.Client(api_key=st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY"))

def analyze_variant(variant_name, text, content_type):
    prompt = f"""
    You are a conversion rate optimization expert.
    Analyze this {content_type}: "{text}"

    Score it out of 10 for each of these factors:
    1. Clarity (how easy to understand)
    2. Emotional Appeal (how it makes people feel)
    3. Urgency (does it make people act now)
    4. Call to Action strength (does it tell people what to do)
    5. Relevance (how well it connects with the audience)

    Then give:
    - Overall Score (average of above)
    - 2 Strengths
    - 2 Weaknesses
    - 1 Suggested improvement

    Format your response as:
    CLARITY: X/10
    EMOTIONAL_APPEAL: X/10
    URGENCY: X/10
    CTA_STRENGTH: X/10
    RELEVANCE: X/10
    OVERALL: X/10
    STRENGTHS: strength1 | strength2
    WEAKNESSES: weakness1 | weakness2
    SUGGESTION: your suggestion here
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
    return "Error analyzing variant."

def parse_scores(analysis_text):
    scores = {}
    for line in analysis_text.split('\n'):
        for metric in ["CLARITY", "EMOTIONAL_APPEAL", "URGENCY", 
                       "CTA_STRENGTH", "RELEVANCE", "OVERALL"]:
            if line.startswith(metric):
                try:
                    score = float(line.split(":")[1].strip().split("/")[0])
                    scores[metric] = score
                except:
                    scores[metric] = 0
    return scores

# ── UI ──
st.set_page_config(page_title="A/B Testing Simulator", page_icon="🧪")
st.title("🧪 A/B Testing Simulator")
st.subheader("by Siddharth Ganesh")
st.divider()

content_type = st.selectbox("What are you testing?", [
    "Email Subject Line",
    "Ad Headline",
    "Call to Action Button",
    "Social Media Caption",
    "Landing Page Headline"
])

st.markdown("### Enter Your Two Variants")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Variant A**")
    variant_a = st.text_area("Version A", 
                              placeholder="e.g. Get 50% off today only!",
                              height=100)
with col2:
    st.markdown("**Variant B**")
    variant_b = st.text_area("Version B", 
                              placeholder="e.g. Limited time: Half price ends tonight!",
                              height=100)

st.divider()

if st.button("🧪 Run A/B Test", use_container_width=True):
    if variant_a and variant_b:

        col1, col2 = st.columns(2)

        with col1:
            with st.spinner("Analyzing Variant A..."):
                analysis_a = analyze_variant("A", variant_a, content_type)
            scores_a = parse_scores(analysis_a)

        with col2:
            with st.spinner("Analyzing Variant B..."):
                analysis_b = analyze_variant("B", variant_b, content_type)
            scores_b = parse_scores(analysis_b)

        # ── Radar Chart ──
        st.divider()
        st.markdown("### Head-to-Head Comparison")

        categories = ["Clarity", "Emotional Appeal", "Urgency", 
                      "CTA Strength", "Relevance"]
        keys = ["CLARITY", "EMOTIONAL_APPEAL", "URGENCY", 
                "CTA_STRENGTH", "RELEVANCE"]

        values_a = [scores_a.get(k, 0) for k in keys]
        values_b = [scores_b.get(k, 0) for k in keys]

        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values_a + [values_a[0]],
            theta=categories + [categories[0]],
            fill='toself',
            name='Variant A',
            line_color='blue'
        ))
        fig.add_trace(go.Scatterpolar(
            r=values_b + [values_b[0]],
            theta=categories + [categories[0]],
            fill='toself',
            name='Variant B',
            line_color='red'
        ))
        fig.update_layout(polar=dict(radialaxis=dict(range=[0, 10])))
        st.plotly_chart(fig, use_container_width=True)

        # ── Score Cards ──
        st.markdown("### Scores")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Variant A**")
            st.metric("Overall Score", f"{scores_a.get('OVERALL', 0)}/10")
            for k, cat in zip(keys[:5], categories):
                st.progress(scores_a.get(k, 0)/10, 
                           text=f"{cat}: {scores_a.get(k, 0)}/10")

        with col2:
            st.markdown("**Variant B**")
            st.metric("Overall Score", f"{scores_b.get('OVERALL', 0)}/10")
            for k, cat in zip(keys[:5], categories):
                st.progress(scores_b.get(k, 0)/10, 
                           text=f"{cat}: {scores_b.get(k, 0)}/10")

        # ── Winner ──
        st.divider()
        overall_a = scores_a.get('OVERALL', 0)
        overall_b = scores_b.get('OVERALL', 0)

        if overall_a > overall_b:
            st.success(f"🏆 **Variant A wins** with a score of {overall_a}/10 vs {overall_b}/10!")
        elif overall_b > overall_a:
            st.success(f"🏆 **Variant B wins** with a score of {overall_b}/10 vs {overall_a}/10!")
        else:
            st.info("🤝 It's a tie! Both variants scored equally.")

        # ── Detailed Analysis ──
        st.divider()
        st.markdown("### Detailed Analysis")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Variant A Analysis**")
            st.write(analysis_a)
        with col2:
            st.markdown("**Variant B Analysis**")
            st.write(analysis_b)

    else:
        st.warning("Please enter both variants!")