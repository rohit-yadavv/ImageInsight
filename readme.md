# ImageInsight

ImageInsight is a web application that allows users to analyze images and extract insights using Optical Character Recognition (OCR) and basic image segmentation techniques.

## Features

- Upload images for analysis
- Extract text content from images using Tesseract OCR
- Segment visual elements from images

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Tesseract OCR engine

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/ImageInsight.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR:

   - **Windows**:

     - Download the Tesseract installer from the official GitHub repository: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
     - Run the installer and follow the on-screen instructions.
     - After installation, add the Tesseract installation directory to the system PATH:
       - Open Control Panel and go to System > Advanced system settings > Environment Variables.
       - Under System variables, find the Path variable and click Edit.
       - Add the path to the Tesseract installation directory (e.g., `C:\Program Files\Tesseract-OCR`) to the list of paths.
       - Create new Variable with name `TESSDATA_PREFIX` and value `\Tesseract-OCR\tessdata`(e.g., `C:\Program Files\Tesseract-OCR\tessdata`).
       - Click OK to save the changes.

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://localhost:5000`.

3. Upload an image using the provided form.

4. Once the image is uploaded, the application will extract text content and segment visual elements from the image.

5. View the analysis results on the output page.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature`)
6. Create a new Pull Request
