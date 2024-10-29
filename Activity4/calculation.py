# Importing packages
import google.generativeai as genai

# Replace with your API KEY
GOOGLE_API_KEY = "YOUR-API-KEY"
genai.configure(api_key=GOOGLE_API_KEY)

"""
CREATE REAMINING FUNCTIONS (subtract, multiply, divide)
"""

# FUNCTION ADD
def add(a: float, b: float):
    """returns a + b."""
    return a + b

# FUNCTION SUBSRACT

# FUNCTION MULTIPLY

# FUNCTION DIVIDE

# Our functions are tools for our gemini model. The model will call our functions when necessary.
# ADD REMAINING FUNCTIONS (subtract, multiply, divide) [add, substract...
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", tools=[add]
)

# You can uncomment the following print and see what's inside the `model` variable
# print(model)

# Enabling automatic function calling, otherwise we have to write the program to determine which function to call, how to call etc.
# Sometimes we have to write our own logic for function calling, in those cases we don't use this.
chat = model.start_chat(enable_automatic_function_calling=True)

# ADD YOUR PROMPT
# For Example: 1 apple costs 2 dollars, I bought 5 apples, what's the total cost?
# The output of the chat.send_message() will be stored in response varibale (LHS)

# Instead of directly typing prompt in the program (a.ka. hard coding) try to get it from the user
# refer this: https://www.w3schools.com/python/ref_func_input.asp
response = chat.send_message(
    "YOUR-PROMPT"
)

print(response.text)

# To see how actually function call works uncomment the following
# There is a nice shortcut for that, select the code block, hold CTRL+/ (forward slash) together, you can use the same to comment as well!
# for content in chat.history:
#     print(content.role, "->", [type(part).to_dict(part) for part in content.parts])
#     print("-" * 80)