# AIStudyBot
A customized Generative AI project for interview preparation

Project Structure
* studyBot_app.py: Main Streamlit application file that handles the UI and interaction.
* models/: Directory where the Llama2 model is stored.
* services/: Custom modules for logging (logging.py) and running services (actions.py).
* README.md: This file.
* requirements_studyBot.txt

How It Works

Backend: The application utilizes the Llama2 model loaded using LlamaCpp to process user input and generate responses. The model is hosted locally for high-performance text generation.

Frontend: The front-end is built using Streamlit, allowing users to interact with the chatbot through a simple text input field.

Session Management: The chat history is stored in st.session_state to maintain a continuous conversation throughout the session.

Save Chat: Users can save the chat history by clicking the "Save" button. The history is saved as a text file in a conversational format.

Logging
The application includes a logging mechanism that tracks user interactions and any potential errors during the model’s response generation. Logs can be saved depending on the LOG_SAVE configuration.

Steps:
1. Clone the Repository:
	https://github.com/moulaskar/AIStudyBot.git
2. cd AIStudyBot 
3. Download the Llama2 Model:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF
	Download the model file (llama-2-7b-chat.Q4_K_S.gguf) from the 	appropriate source and place it in the models/ directory.
4. Create a logs dicrectory
5. Install the requiremets
Pip install -r requirements_studyBot.txt
6. Run the Application:
		streamlit run studyBot_app.py

To-DO
1. Add code to store and retrieve chat history in MySQL database.
2. Provide UI for the same
3. Add Rag to add customized data to be added to the prompt.
4. Provide UI for the same.
