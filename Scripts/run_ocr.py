import requests
import base64

# Read the input PDF file as binary data
with open('input.pdf', 'rb') as file:
    pdf_data = file.read()

# Encode the PDF data as base64
encoded_pdf = base64.b64encode(pdf_data).decode('utf-8')

# Define the API endpoint URL
url = 'https://api.example.com/convert'

# Define the request payload
payload = {
    'api_key': 'YOUR_API_KEY',
    'secret_key': 'YOUR_SECRET_KEY',
    'input_file': encoded_pdf,
}

# Make a POST request to the API endpoint
response = requests.post(url, json=payload)

# Check if the API call was successful
if response.status_code == 200:
    # Retrieve the converted searchable PDF data
    converted_pdf = response.json()['output_file']

    # Decode the PDF data from base64
    decoded_pdf = base64.b64decode(converted_pdf)

    # Save the output PDF file
    with open('output.pdf', 'wb') as output_file:
        output_file.write(decoded_pdf)
else:
    # Handle the API error
    print(f'API error: {response.status_code} - {response.text}')
