import datetime
import openai
import os
import requests

# Connect to OpenAI API.
openai.api_key = os.getenv("OPENAI_API_KEY")
# ask user for input
user_input = input("Enter your image prompt: ")


# This is the image generator function V1.
def image_gen(request, size='512x512'):
    # Send the user input to the OpenAI image API
    response = openai.Image.create(
        prompt=f"{request}",
        n=1,
        size=f"{size}"
    )
    # Store the output of the API call to this variable
    image_url = response['data'][0]['url']

    # This calls the "requests" library to download the file
    # that is at the URL returned by OpenAI img API
    response = requests.get(image_url)

    # The call to the request library returns a status code indicating
    # success or failure. This if statement downloads the file if the
    # request was a success, and shows an error if there's a failure.
    if response.status_code == 200:
        # Get the first five characters of the request.
        request_firstfive = request[:5]
        # Get the current time.
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M")
        # Set the output filename to the first five characters _ the current time.
        filename = request_firstfive + "_" + current_time
        # Write the image to the file.
        with open(f"{filename}.png", "wb") as file:
            file.write(response.content)
        print("Image downloaded successfully.")
    else:
        print("Failed to download image.")


# Call the 'Image' Gen Function as a Test.
image_gen(user_input)
