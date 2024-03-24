import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=gemini_api_key)

generation_config = {
"temperature": 0.9,
"top_p": 1,
"top_k": 1,
"max_output_tokens": 2048,
}

safety_settings = [
{
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
},
{
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
},
{
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
},
{
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
},
]

statement = "sucking the venom out of someone who is bitten by a snake is the best solution to save him"

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                            generation_config=generation_config,
                            safety_settings=safety_settings)
history = []
prompts = [
    f'"{statement}" just answer me with True or False nothing more (without a point in the end )',
    "can you provide me with a corrected statement within a paragraph that doesnt exceed 3 lines",
    "can you give me a link that contains an article explaining the previous medical statement, provide me with only the link nothing more, i want it exactly in the format of https:// ... and nothing more"
    ]
output = {'status': "False", 'correct_statement': "", 'source': ""}

index = 0
for key in output.keys():
    if output['status'] == "False":
        convo = model.start_chat(history=history)
        convo.send_message(prompts[index])
        respond = convo.last.text
        history.append({'role':'user','parts':prompts[index]})
        history.append({'role':'model','parts':respond})
    else:
        respond = "n/a"
    output[key] = respond
    index += 1

print(output)