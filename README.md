# 📄 PDF Outline Extractor – Adobe "Connecting the Dots" Challenge (Round 1A)

This project is built for **Round 1A** of the Adobe India Hackathon 2025 – *"Connecting the Dots Challenge"*. The goal is to reimagine the humble PDF as an intelligent, structured experience by extracting title and heading-level outlines from raw PDFs.

---

## 🚀 What It Does

This solution:
- Accepts a `.pdf` file (up to 50 pages)
- Extracts:
  - Title (largest font on first page)
  - Headings with hierarchy: **H1**, **H2**, **H3**
  - Page numbers for each heading
- Outputs a clean `.json` file in the required format

### ✅ Sample Output Format:
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
