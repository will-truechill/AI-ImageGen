AI Image Generator

This is a simple Python function that uses the OpenAI API to generate images based on user input. The script allows the user to provide a prompt through user input, and generates an image based on that prompt using the OpenAI Image API. The program is currently in version 1.

Dependencies

This program requires the following dependencies:

    Python 3.6 or later
    OpenAI API key
    requests library
    OpenAI library

Installation

To use this program, follow these steps:

    Clone the repository to your local machine or download ai-imagegen.py as this file contains the python function.
    Set the OPENAI_API_KEY environment variable to your OpenAI API key.
    Install the requests library using pip: pip install requests
    Install the OpenAI library using pip: pip install openai

Usage

To use this program, call the image_gen(string, opt[size]) function and pass it a string to use as a prompt for image generation. Size can also be passed as an optional argument to the function, but if the size isn't 256x256, 512x512, or 1024x1024, the OpenAI API will throw an erorr. 

Please refer to the OpenAI API Documentation for information on modifying the request settings.
https://platform.openai.com/docs/introduction
