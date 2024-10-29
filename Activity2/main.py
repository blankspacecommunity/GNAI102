# Import necessary modules for system and web interaction
import os  # Provides tools to interact with the operating system

# Attempt to import the 'google.generativeai' and 'streamlit' libraries
# - google.generativeai: enables interaction with Google's generative AI models (e.g., Gemini)
# - streamlit: a Python library for creating simple, interactive web applications
try:
    import google.generativeai as genai
    import streamlit as st
except ImportError:
    # If the libraries aren't installed, use 'pip' to install them
    # 🤔 What is pip? 
    # pip is a package manager for Python that allows us to install external libraries (like google-generativeai and streamlit).
    # Here, it’s used to install the required libraries automatically if they’re missing.
    print("Installing required libraries...")
    os.system('pip3 install google-generativeai streamlit')
    try:
        import google.generativeai as genai
        import streamlit as st
    except ImportError:
        print("Failed to install 'google-generativeai' or 'streamlit'. Please install them manually.")
        sys.exit(1)  # Exit the program if installation fails

# What is Streamlit?
# Streamlit is a Python library for creating web applications from simple Python scripts.
# It’s beginner-friendly and doesn’t require complex setups like other frameworks (e.g., Flask, Django).
# Streamlit Documentation: https://docs.streamlit.io/

# Configure the generative AI client with your API key
# To use the Gemini model, you need an API key from Google. This key allows secure access to Google's generative AI services.
# Go to https://aistudio.google.com/app/apikey to get an API key
api_key = "YOUR_API_KEY"  # Replace 'YOUR_API_KEY' with your actual API key
if api_key == "YOUR_API_KEY":
    print("Please replace 'YOUR_API_KEY' with your actual API key.")
    sys.exit(1)  # Exit if the API key isn’t provided

# Configure the generative AI client
genai.configure(api_key=api_key)

# Set up the Gemini model for chat
# The 'gemini-1.5-flash' model is a fast conversational model designed for real-time interactions
try:
    model = genai.GenerativeModel("models/gemini-1.5-flash")  # Creates an instance of the chatbot model
    chat = model.start_chat()  # Starts a new chat session
except Exception as e:
    print(f"Error initializing model: {e}")
    sys.exit(1)

# Display the title on the web app
# What is markdown? 🤔
# Markdown is a lightweight markup language that adds formatting to text (like bold, italic, links, etc.) for display in web apps.
# More about markdown: https://www.markdownguide.org/basic-syntax/
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>Gemini Pro Chatbot</h1>",
    unsafe_allow_html=True,
)

# Display an introductory header
st.header("Hello! Welcome! What is your question?")  # You can change this header text!

# Add a text input box for users to enter their questions
# 🤔 What should we use here to allow the user to type a question?
# Hint: In Streamlit, use 'st.text_input()' to create an input box
# Documentation: https://docs.streamlit.io/library/api-reference/widgets/st.text_input
prompt = st.text_input(
    "Enter your question please...", placeholder="Question", label_visibility="visible"
)

# Add a submit button for the user to send their question
# When clicked, it sends the prompt to the chatbot and displays the response
if st.button("[SUBMIT]", use_container_width=True):
    if prompt:  # Ensure that the input is not empty
        try:
            # Send the user's message to the chat model and get a response
            response = chat.send_message(prompt)
            
            # Display the model's response
            st.write("")  # Adds a space
            st.header("Response")
            st.write("")  # Adds another space
            st.markdown(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question before clicking submit.")
