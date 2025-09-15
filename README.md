# PDF to JPG and JPG to PDF Converter

A simple Python CLI application to convert PDF files to JPG images and JPG images to PDF files.

## Requirements

- Python 3.x
- Poppler (for pdf2image on Windows, download from https://blog.alivate.com.au/poppler-windows/ and add to PATH)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/dagmarinsancendekia/PDF-to-JPG.git
   cd PDF-to-JPG
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

You can run the application using Python directly or use the provided `run.bat` for easier execution on Windows.

### Convert PDF to JPG
```
python main.py pdf2jpg path/to/file.pdf output/directory
```
or
```
run.bat pdf2jpg path/to/file.pdf output/directory
```

This will create JPG images for each page in the output directory.

### Convert JPG to PDF
```
python main.py jpg2pdf path/to/image1.jpg path/to/image2.jpg output.pdf
```
or
```
run.bat jpg2pdf path/to/image1.jpg path/to/image2.jpg output.pdf
```

This will combine the JPG images into a single PDF file.

## License

MIT
