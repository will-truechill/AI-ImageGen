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

    Clone the repository to your local machine.
    Set the OPENAI_API_KEY environment variable to your OpenAI API key.
    Install the requests library using pip: pip install requests
    Install the OpenAI library using pip: pip install openai

Usage

To use this program, simply run the image_gen() function with a user-provided prompt as the argument. The function will generate an image based on the prompt and save it as a PNG file in the same directory as the python file with a filename based on the first five characters of the prompt and the current time.

Please refer to the OpenAI API Documentation for information on modifying the request settings.
https://platform.openai.com/docs/introduction