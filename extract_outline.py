# extract_outline.py
import os
import fitz  # PyMuPDF
import json

def extract_headings_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    blocks = []

    for page_num, page in enumerate(doc, start=1):
        for block in page.get_text("dict")["blocks"]:
            if "lines" in block:
                for line in block["lines"]:
                    line_text = ""
                    font_size = 0
                    for span in line["spans"]:
                        line_text += span["text"]
                        font_size = max(font_size, span["size"])
                    if line_text.strip():
                        blocks.append({
                            "text": line_text.strip(),
                            "font_size": font_size,
                            "page": page_num
                        })

    sorted_blocks = sorted(blocks, key=lambda x: -x["font_size"])
    title = sorted_blocks[0]["text"]
    font_sizes = sorted(set(b["font_size"] for b in blocks), reverse=True)
    h1, h2, h3 = (font_sizes + [0, 0, 0])[:3]

    outline = []
    for b in blocks:
        level = None
        if b["font_size"] == h1:
            level = "H1"
        elif b["font_size"] == h2:
            level = "H2"
        elif b["font_size"] == h3:
            level = "H3"
        if level:
            outline.append({
                "level": level,
                "text": b["text"],
                "page": b["page"]
            })

    return {
        "title": title,
        "outline": outline
    }

def main():
    input_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    print(f"Looking for PDFs in {input_dir}")
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            print(f"Processing file: {filename}")
            pdf_path = os.path.join(input_dir, filename)
            result = extract_headings_from_pdf(pdf_path)
            json_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            with open(json_path, "w") as f:
                json.dump(result, f, indent=2)
            print(f"Saved output to {json_path}")

if __name__ == "__main__":
    main()