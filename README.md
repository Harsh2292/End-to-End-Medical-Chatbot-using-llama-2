# End-to-End-Medical-Chatbot-using-llama-2
*** first create virtual enviroment

-- $ python -m venv mchatbot

*** Activate the enviroment

-- $ source mchatbot/Scripts/activate

*** Run pip install requirements.txt

*** download llama model using following command it may take 20 mins or more

## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin

$ curl -L -o llama-2-7b-chat.ggmlv3.q4_0.bin https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_0.bin && echo "Download complete: llama-2-7b-chat.ggmlv3.q4_0.bin saved to $(pwd)"

*** Run a test file from test folder to check if the model is working or not. for the first time model may take 40 - 50 sec to give responce.

*** 
