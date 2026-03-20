import gradio as gr
import sys
from challenge_instructions import INSTRUCTIONS
from sys_prompt import SYS_PROMPT


def get_Llama():
    from llama_cpp import Llama
    model = "Llama-3.2-3B-Instruct.F16.gguf"
    client = Llama(model_path="./models/Llama-3.2-3B-Instruct.F16.gguf",chat_format="llama-3")
    return client.create_chat_completion,model

def get_openai():
    from openai import OpenAI
    model = "Llama-3.2-3B-Instruct.F16.gguf"
    client = OpenAI(api_key="DummyKey", base_url="http://localhost:8071/v1/")
    return client.chat.completions.create,model

class Bot:
    def __init__(self,chat_completion,model):
        self.chat_completion = chat_completion
        self.model = model
    
    def response(self,messages):
        rsp = self.chat_completion(messages=messages,model=self.model)
        if hasattr(rsp,'choices'):
            return rsp.choices[0].message.content
        else: 
            return rsp.get('choices')[0].get('message').get('content')
        
bot = None


def bot_response(message, msg_list):
    
    if msg_list is None:
        msg_list = [{"role": "system", "content": SYS_PROMPT}]
    
    msg_list.append({"role": "user", "content": message})

    response = bot.response(messages=msg_list)
    
    msg_list.append({"role": "assistant", "content": response})

    return msg_list[1:], "", msg_list


def clear_all():
        return [], "", None

def main():
      
    with gr.Blocks() as demo:
        
        state = gr.State()
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown(INSTRUCTIONS)
        
            with gr.Column(scale=1):
                out = gr.Chatbot(height=600)
                inp = gr.Textbox(placeholder="Can you fool the bot to reveal the flag?",container=False,scale=2)
                submit_btn = gr.Button("Send")
                clear_btn = gr.Button("Clear")
        
        submit_btn.click(
        fn=bot_response,
        inputs=[inp,state],
        outputs=[out,inp , state])

        inp.submit(
        fn=bot_response,
        inputs=[inp,state],
        outputs=[out, inp, state])

        clear_btn.click(
        fn=clear_all,
        inputs=[],
        outputs=[out, inp, state])
    
    demo.launch(theme="ocean",
                server_name="0.0.0.0",
                server_port=8008
                )

if __name__ == "__main__":
    
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        chat_completion,model = get_Llama()
    else:
        chat_completion,model = get_openai()

    bot = Bot(chat_completion,model)
    main()