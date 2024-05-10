import gradio as gr
from taibun import Converter  # Assuming the taibun package provides a Converter class


def convert_text(text, system="Tailo", dialect="south", format="mark", sandhi="none"):
    # Create a converter object with selected options
    converter = Converter(system=system, dialect=dialect, format=format, sandhi=sandhi)
    # Return the converted text
    return converter.get(text)


# Define the interface
interface = gr.Interface(
    fn=convert_text,
    inputs=[
        gr.Textbox(label="Enter Hokkien text", placeholder="Type Hokkien text here..."),
        gr.Dropdown(
            choices=["Tailo", "POJ", "Zhuyin", "TLPA", "Pingyim", "Tongiong", "IPA"],
            label="System",
            value="Tailo",
        ),
        gr.Dropdown(choices=["south", "north"], label="Dialect", value="south"),
        gr.Dropdown(
            choices=["mark", "number", "strip"], label="Tone Format", value="mark"
        ),
        gr.Dropdown(
            choices=["none", "auto", "exc_last", "incl_last"],
            label="Tone Sandhi",
            value="none",
        ),
    ],
    outputs=[gr.Textbox(label="Converted Text")],
    title="Hokkien Transliteration Converter",
    description="Convert Hokkien text between various transliteration systems using the <a href='https://github.com/andreihar/taibun' target='_blank'>taibun</a> package.",
)

# Launch the app
interface.launch()
