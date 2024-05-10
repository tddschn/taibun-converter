import gradio as gr
from taibun import Converter  # Assuming the taibun package provides a Converter class

def convert_text(text, system, dialect, format, sandhi):
    # Create a converter object with selected options
    converter = Converter(system=system, dialect=dialect, format=format, sandhi=sandhi)
    # Return the converted text
    return converter.get(text)

# Define the interface
interface = gr.Interface(
    fn=convert_text,
    inputs=[
        gr.Textbox(label="Enter Taiwanese Hokkien text"),
        gr.Dropdown(choices=["Tailo", "POJ", "Zhuyin", "TLPA", "Pingyim", "Tongiong", "IPA"], label="System"),
        gr.Dropdown(choices=["south", "north"], label="Dialect"),
        gr.Dropdown(choices=["mark", "number", "strip"], label="Tone Format"),
        gr.Dropdown(choices=["none", "auto", "exc_last", "incl_last"], label="Tone Sandhi"),
    ],
    outputs=[gr.Textbox(label="Converted Text")],
    title="Taiwanese Hokkien Transliteration Converter",
    description="Convert Taiwanese Hokkien text between various transliteration systems using the Taibun package."
)

# Launch the app
interface.launch()
