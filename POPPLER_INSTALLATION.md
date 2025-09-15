# Poppler Installation and Setup on Windows

Follow these steps to download, install, and configure Poppler utilities on Windows for use with pdf2image:

## Step 1: Download Poppler for Windows
- Go to the GitHub releases page: https://github.com/oschwartz10612/poppler-windows/releases
- Download the latest `Release-xx.xx.x-0.zip` file from the "Assets" section.

## Step 2: Extract the Zip File
- Extract the downloaded zip file to a folder on your computer, e.g., `C:\poppler`.

## Step 3: Add Poppler to System PATH
- Open the Start Menu and search for "Environment Variables".
- Click "Edit the system environment variables".
- In the System Properties window, click "Environment Variables".
- Under "System variables", find and select the `Path` variable, then click "Edit".
- Click "New" and add the path to the Poppler `bin` directory, e.g., `C:\poppler\bin`.
- Click OK on all dialogs to save.

## Step 4: Verify Installation
- Open a new Command Prompt window.
- Run the command: `pdfinfo -version`
- You should see the version information of Poppler utilities.

## Step 5: Test PDF to JPG Conversion
- Run your Python script again to convert PDF to JPG.

If you need help with any of these steps, please let me know.
