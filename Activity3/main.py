# Import the 'os' module for interacting with the operating system
import os
import time  # Import the 'time' module to handle time-related operations

# First, attempt to import the necessary libraries
try:
    import google.generativeai as genai
    import streamlit as st
except ImportError:
    # In case the library isn't installed, we can use 'pip' to install it
    # Check out this line: "pip3 install google-generativeai" – it may come in handy if things are missing!
    os.system("pip3 install google-generativeai streamlit")
    import google.generativeai as genai

# Activity: Creating a simple web-based chatbot with the Gemini model and Streamlit

# Tip: Configure generative AI with your own API key
# Explore -> https://aistudio.google.com/app/apikey to get an API key
# Replace 'YOUR_API_KEY' below once you have it
genai.configure(api_key="YOUR_API_KEY")  # Don't forget to fill this in!

# Choose the generative model to use. Here, we use the 'gemini-1.5-flash' model.
# Note: It's all in the name! What comes after 'gemini'?
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Start a new chat session using the model to keep the conversation context
chat = model.start_chat()

# Streamlit App Title with Custom Styling
# Fun challenge: Try changing color and title to customize the app further!
st.markdown(
    "<h3 style='text-align: center; color: #4CAF50;'>Gemini Vision Pro</h3>",
    unsafe_allow_html=True,
)

# App Header to guide users on interacting with the app
st.header("Interact with Gemini Pro Vision")

# Create an input field for entering a prompt or a question about an image
# Psst! What's hiding under "Prompt"? Look for its hidden hints when running the app
media_prompt = st.text_input(
    "Interact with the Image/Video", placeholder="Prompt", label_visibility="visible"
)

# Let users upload images (PNG, JPG, JPEG, WEBP)
uploaded_file = st.file_uploader(
    "Choose an Image/Video",
    accept_multiple_files=False,
    type=["png", "jpg", "jpeg", "webp", "mp4", "mkv", "avi"],
)

# Display the uploaded image if one is provided
if uploaded_file is not None:
    st.image(uploaded_file, use_column_width=True)

    # Add a hint of style to the image display!
    st.markdown(
        """
            <style>
                    img {
                        border-radius: 50px;  # Adds rounded corners to the image
                        border: 1px solid #4CAF50;  # Adds a border around the image
                    }
            </style>
            """,
        unsafe_allow_html=True,
    )

# Button to get AI response
if st.button("GET RESPONSE", use_container_width=True):
    if uploaded_file is not None:
        if media_prompt != "":
            # Write the file locally with its original name (useful if it’s ever needed)
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Upload and get AI-generated content. Tip: Fill in if missing!
            # Fill in -> response = model.generate_content([...])
            # What is model.generate_content?
            # This function processes the uploaded file and prompt to generate a response from the AI model.
            file = genai.upload_file(
                uploaded_file.name
            )  # Ensure to upload the file first

            while file.state.name == "PROCESSING":
                time.sleep(0.5)
                myfile = genai.get_file(myfile.name)
            # Wait for the file to be processed

            response = model.generate_content(
                [file, media_prompt or "Describe the media content"]
            )

            # Ensure the response is fully available before displaying
            response.resolve()

            # Display the AI's response (look for the "Response" hint!)
            st.write(":red[Response]")  # Highlights the response section
            st.markdown(response.text)  # Displays the generated text from the AI

        else:
            st.write("")
            st.header(":red[Please Provide a prompt]")  # Warning for empty prompt
    else:
        st.write("")
        st.header(":yellow[Please Provide an image]")  # Warning for missing image
