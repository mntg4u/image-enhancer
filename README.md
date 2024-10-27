# Image Enhancer

A powerful web application built with Flask that enhances images using an external API. Users can upload images, which are processed to enhance their quality and then downloaded back to their devices.

## Features

- **User-Friendly Interface**: Simple and intuitive form for image uploads.
- **Image Enhancement**: Utilizes an external API to enhance the quality of images.
- **Supports Multiple Formats**: Works with JPEG and PNG image formats.
- **Efficient Processing**: Handles image processing asynchronously, providing quick feedback to users.
- **Customizable UI**: Easily modify the look and feel using CSS.

## Technologies Used

- **Backend**: Flask
- **External API**: Remini API for image enhancement
- **Frontend**: HTML, CSS
- **Data Format**: JSON for API communication
- **Deployment**: Heroku or Replit (for web hosting)

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/mntg4u/image-enhancer.git
cd image-enhancer

Install Dependencies
Create a virtual environment and install the required packages:

bash
Copy code
# Create a virtual environment
python -m venv venv
# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt```

<h1>Usage </h1>
<h3>Running the Application</h3>
Start the Flask server:

bash
Copy code
python app.py
Open your browser and navigate to http://127.0.0.1:5000/.

Upload an image using the provided form.

Download the enhanced image once the processing is complete
