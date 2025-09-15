import argparse
from pdf2image import convert_from_path
from PIL import Image
import os

def pdf_to_jpg(pdf_path, output_dir):
    """
    Convert PDF to JPG images, one per page.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image.save(os.path.join(output_dir, f"page_{i+1}.jpg"), "JPEG")
    print(f"Converted {len(images)} pages to JPG in {output_dir}")

def jpg_to_pdf(jpg_paths, output_pdf):
    """
    Convert JPG images to a single PDF.
    """
    images = [Image.open(jpg).convert('RGB') for jpg in jpg_paths]
    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"Converted {len(images)} JPGs to PDF: {output_pdf}")
    else:
        print("No JPG files provided.")

def main():
    parser = argparse.ArgumentParser(description="Convert PDF to JPG or JPG to PDF")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # PDF to JPG subcommand
    pdf_parser = subparsers.add_parser('pdf2jpg', help='Convert PDF to JPG')
    pdf_parser.add_argument('pdf', help='Path to PDF file')
    pdf_parser.add_argument('output_dir', help='Output directory for JPG files')

    # JPG to PDF subcommand
    jpg_parser = subparsers.add_parser('jpg2pdf', help='Convert JPG to PDF')
    jpg_parser.add_argument('jpgs', nargs='+', help='Paths to JPG files')
    jpg_parser.add_argument('output_pdf', help='Output PDF file path')

    args = parser.parse_args()

    if args.command == 'pdf2jpg':
        pdf_to_jpg(args.pdf, args.output_dir)
    elif args.command == 'jpg2pdf':
        jpg_to_pdf(args.jpgs, args.output_pdf)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
