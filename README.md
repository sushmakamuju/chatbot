Python 3.11.x is required (any patch version of Python 3.11)


 ##Clone the Repository
 
git clone https://github.com/sushmakamuju/chatbot.git
cd chatbot

##Create & Activate Virtual Environment
python -3.11 -m venv venv
source venv/Scripts/activate

##Install Required Dependencies
pip install -r requirements.txt

##Environment Variables
Create a .env file in the project root and add below api key and model

GROQ_API_KEY=your_groq_api_key_here
MODEL_ID="llama-3.1-8b-instant"

##Run the Chatbot
py chatbot.py
