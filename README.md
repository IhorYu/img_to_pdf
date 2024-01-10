## Overview
The "img_to_pdf" is a Django-based web application that converts images to a PDF file. It supports various image formats like PNG, JPG, JPEG, and HEIC.

## Features
- **Image Upload**: Users can upload multiple images in supported formats.
- **HEIC to PNG Conversion**: Automatically converts HEIC images to PNG format.
- **Image Resizing**: Resizes images to a predefined dimension.
- **PDF Conversion**: Combines uploaded images into a single PDF.
- **File Download**: Users can download the generated PDF.

## Usage
### Uploading Images
- Access the web interface.
- Upload images in the supported formats.

### Downloading PDF
- After conversion, a download option is available for the generated PDF.

## Error Handling
- Validates file extensions.
- Handles file-not-found errors.

## Dependencies
- Django
- Pillow
- pillow_heif

Ensure these dependencies are installed for the application to function correctly.

## Setup and Installation
For setup, follow standard Django application deployment procedures. 
