#!/usr/bin/env python3

import gradio as gr
from taibun import Converter, to_simplified, to_traditional

# List of example texts
# source: https://github.com/andreihar/taibun
examples = [
    ("先生講，學生恬恬聽。", "Tailo", "south", "mark", "none"),
    ("我欲用箸食魚", "POJ", "north", "number", "auto"),
    ("生日快樂", "Zhuyin", "south", "strip", "exc_last"),
    ("太空朋友，恁好！恁食飽未？", "Pingyim", "north", "mark", "incl_last"),
    ("這是台灣囡仔", "Tongiong", "south", "number", "none"),
]


def convert_text(text, system="Tailo", dialect="south", format="mark", sandhi="none"):
    # Create a converter object with selected options
    converter = Converter(system=system, dialect=dialect, format=format, sandhi=sandhi)
    # Convert the text using the specified transliteration system
    converted_text = converter.get(text)
    # Convert to simplified Chinese characters
    simplified_text = to_simplified(text)
    # Convert to traditional Chinese characters
    traditional_text = to_traditional(text)
    # Return the tuple containing all conversion results
    return converted_text, simplified_text, traditional_text


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
    outputs=[
        gr.Textbox(label="Converted Text"),
        gr.Textbox(label="Simplified Chinese"),
        gr.Textbox(label="Traditional Chinese"),
    ],
    title="Hokkien Transliteration Converter",
    description="Convert Hokkien text between various transliteration systems using the <a href='https://github.com/andreihar/taibun' target='_blank'>taibun</a> package. Made by <a href='https://teddysc.me/blog/introducing/hokkien-converter'>Teddy</a>.<br/><img src='https://github.com/cli/cli/assets/45612704/84eaa125-43c8-4b52-a3e6-329c7d59c8ff' />",
    examples=[list(x) for x in examples],
)

# Launch the app
interface.launch(share=True)
