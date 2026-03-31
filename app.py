import gradio as gr
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount current directory as static
app.mount("/", StaticFiles(directory=".", html=True), name="static")

with gr.Blocks() as demo:
    gr.HTML("<iframe src='/' width='100%' height='1000px'></iframe>")

app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)