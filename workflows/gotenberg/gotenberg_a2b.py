import os
import requests
from pathlib import Path

GOTENBERG_URL = "http://localhost:3000/forms/libreoffice/convert"

INPUT_FOLDER = r""
OUTPUT_FOLDER = r""

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

SUPPORTED_EXTENSIONS = {".doc", ".docx"}

def convert_to_pdfa(file_path: Path, output_dir: str):
    output_path = Path(output_dir) / (file_path.stem + ".pdf")

    with open(file_path, "rb") as f:
        response = requests.post(
            GOTENBERG_URL,
            files={"files": (file_path.name, f, "application/octet-stream")},
            data={"pdfa": "PDF/A-2b"},  # ← fixed
        )

    if response.status_code == 200:
        output_path.write_bytes(response.content)
        print(f"✓ Converted: {file_path.name} → {output_path.name}")
    else:
        print(f"✗ Failed:    {file_path.name} (HTTP {response.status_code})")
        print(f"  Details:   {response.text}")

def main():
    input_path = Path(INPUT_FOLDER)
    files = [f for f in input_path.iterdir() if f.suffix.lower() in SUPPORTED_EXTENSIONS]

    if not files:
        print("No DOC/DOCX files found in the input folder.")
        return

    print(f"Found {len(files)} file(s) to convert...\n")
    for file in files:
        convert_to_pdfa(file, OUTPUT_FOLDER)

    print("\nDone!")

if __name__ == "__main__":
    main()