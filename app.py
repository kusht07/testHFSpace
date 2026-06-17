import gradio as gr

def respond(message, history):
    return "You said, " + message + "!"

gr.ChatInterface(respond).launch()