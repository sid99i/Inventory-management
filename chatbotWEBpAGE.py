from flask import Flask, request, render_template, redirect, url_for
import openai
import gradio as gr

openai.api_key = "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"
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
prompt = "type here.."

def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history

block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>ChatBot</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route('/chatbot/')
def chatbot():
    block.launch(debug=True)
    return

if __name__ == '__main__':
    app.run(debug=True)
