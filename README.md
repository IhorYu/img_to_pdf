# img_to_pdf: Image to PDF Converter

## Overview
`img_to_pdf` is a Django-based web application that offers a simple yet effective solution for converting various image formats into a single PDF document. It supports formats like PNG, JPG, JPEG, and HEIC, making it a versatile tool for users who need to consolidate images into PDF format.

## Features
- **Multiple Image Upload**: Support for uploading multiple images in various formats.
- **HEIC to PNG Conversion**: Automatic conversion of HEIC images to PNG for compatibility.
- **Image Resizing**: Option to resize images to fit the PDF format better.
- **Single PDF Creation**: Combines all uploaded images into a single, easily downloadable PDF file.
- **User-Friendly Interface**: Simple and intuitive web interface for hassle-free operation.

## Installation
To set up the `img_to_pdf` application on your system, follow these steps:

1. **Clone the Repository**:  
   ```
   git clone https://github.com/IhorYu/img_to_pdf.git
   cd img_to_pdf
   ```

2. **Install Dependencies**:  
   Make sure you have Python and Django installed. Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**:  
   ```
   python manage.py runserver
   ```
   The application will be available at `localhost:8000` in your web browser.

## Usage
1. **Access the Web Interface**: Open your browser and go to `localhost:8000`.
2. **Upload Images**: Click on the upload button and select the images you want to convert to PDF.
3. **Download PDF**: Once the images are uploaded and processed, a download button will appear. Click it to download your PDF.

## Contributing
Contributions to `img_to_pdf` are welcome! If you have suggestions for improvements or encounter any issues, please feel free to submit a pull request or open an issue in the repository.
