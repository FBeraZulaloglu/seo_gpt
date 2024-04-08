import streamlit as st
import requests
from openai import OpenAI

# Function to make API requests to GPT Assistants API
def generate_text(prompt, api_key):
    url = "https://api.openai.com/v1/assistant/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "text-davinci-002",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that creates SEO optimized content."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, json=data, headers=headers)
    print(response)
    return response.json()["choices"][0]["message"]["content"]

def send_chat_completion_request(messages,api_key):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=messages,
        temperature=0,
        max_tokens=1000,
    )
    return response.choices[0].message.content
# Streamlit UI
def main():
    st.title("SEO GPT4 Assistant")
    st.write("This tool helps you generate SEO-friendly content using GPT-4.")

    # Input field for user to enter prompt
    prompt = st.text_area("Enter your prompt here:")

    # API key input field
    api_key = st.text_input("Enter your GPT Assistants API key:")

    if st.button("Generate Content"):
        if not prompt:
            st.warning("Please enter a prompt.")
        elif not api_key:
            st.warning("Please enter your GPT Assistants API key.")
        else:
            # Generate content using GPT Assistants API
            try:
                messages = [
                    {"role": "system", "content": "You are a helpful assistant that creates SEO optimized content."},
                    {"role": "user", "content": prompt}
                ]
                generated_text = send_chat_completion_request(messages,api_key)
                #generated_text = generate_text(prompt, api_key)
                st.success("Content generated successfully!")
                st.write("Generated Content:")
                st.write(generated_text)
            except Exception as e:
                st.error(f"Error generating content: {str(e)}")

if __name__ == "__main__":
    main()
