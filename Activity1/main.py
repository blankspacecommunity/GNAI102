# Import necessary modules
import os  # Provides tools to interact with the operating system (e.g., to run terminal commands)
import sys  # Helps in handling system-level operations and exceptions

p = print  # Assign the 'print' function to a shorter variable name for convenience 

# We attempt to import the 'google.generativeai' library.
# This library allows us to interact with Google's generative AI models, including conversational models like Gemini.
# Note: If 'google.generativeai' isn't installed, the program will try to install it for you.
try:
    import google.generativeai as genai
except ImportError:
    # If the library isn't installed, install it with pip
    # What is pip? 🤔
    # pip is a package manager for Python that allows us to install and manage external libraries, like 'google-generativeai'
    # Here, we use pip to install the 'google-generativeai' library so our program can use Google's AI models.
    print("Installing required library 'google-generativeai'...")
    os.system(f'{sys.executable} -m pip install google-generativeai')

    # After installation, attempt to import the library again
    try:
        import google.generativeai as genai
    except ImportError:
        # If the library still cannot be imported, prompt the user to install it manually
        print("Failed to install 'google-generativeai'. Please install it manually by running:")
        print(f"{sys.executable} -m pip install google-generativeai")
        sys.exit(1)  # Exit the program if installation fails

# CLI setup for the chatbot using the Gemini model
# CLI stands for Command-Line Interface, a text-based way of interacting with a program
# The Gemini model is a conversational model from Google designed for fast and interactive dialogue generation.

# To use the Gemini model, you need to configure your personal API key.
# This key is required to access Google's generative AI services. You can obtain an API key here:
# https://aistudio.google.com/app/apikey
api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key
if api_key == 'YOUR_API_KEY':
    print("Please replace 'YOUR_API_KEY' with your actual API key.")
    sys.exit(1)  # Exit the program if the API key isn't provided

# Now, configure the generative AI client with the API key
genai.configure(api_key=api_key)

# Initialize the Gemini model using 'gemini-1.5-flash', a fast conversational model optimized for real-time chat
try:
    model = genai.GenerativeModel('models/gemini-1.5-flash')  # Creates a model instance for the chatbot
    chat = model.start_chat()  # Starts a new chat session, keeping track of the conversation flow
except Exception as e:
    print(f"Error initializing model: {e}")
    sys.exit(1)  # Exit if there's an issue with model setup

# Begin a conversation loop
print("Welcome to the Gemini CLI Chatbot! Type 'exit' to end the conversation.")
while True:
    try:
        # Prompt the user for input
        # 🤔 What function should you use here to allow the user to type a message?
        # Hint: Look up the below link to find it out.
        # Documentation: https://www.w3schools.com/python/ref_func_input.asp
        user_input = 'YOUR_PROMPT_HERE'  # Replace this placeholder to capture the user's input

        # Ensure the input is not empty
        if not user_input:
            print("Input cannot be empty. Please type a message.")
            continue

        # Exit condition
        if user_input.lower() == 'exit':  # If the user types 'exit', end the chat loop
            print("Ending chat. Goodbye!")
            break

        # Send the user's message to the Gemini model to get a response
        response = chat.send_message(user_input)
        if response:
            print("Gemini:", response.text)  # Display the response text from the Gemini model
        else:
            print("Gemini: (No response received)")
    except Exception as e:
        print(f"Error during chat: {e}")  # Print any errors that occur during chat
