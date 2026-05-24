from google import genai
import os
import time

# Connect to Gemini
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

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

    # Try up to 3 times if quota is hit
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text

        except Exception as e:
            if "429" in str(e):
                print(f"Rate limit hit. Waiting 30 seconds... (attempt {attempt+1}/3)")
                time.sleep(30)
            else:
                raise e

    return "Error: Could not generate content after 3 attempts."

# Test it
result = generate_content(
    brand_name="EcoWear",
    niche="Sustainable Fashion",
    tone="Friendly and inspiring",
    audience="Millennials who care about the environment",
    content_type="3 Instagram captions with hashtags"
)

print(result)