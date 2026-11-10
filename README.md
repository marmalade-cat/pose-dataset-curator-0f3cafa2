Pose-Dataset-Curator

A tiny prototype to extract CSV/JSON links from an article HTML/text blob, validate files, and preview content.

Usage
- Open index.html in a browser. Paste article HTML or text, or drag-and-drop a local HTML file. The page lists discovered .csv/.json links and previews the first few rows/objects and basic validation.
- Or run main.py to validate local CSV/JSON files and print a provenance-style report.

Notes
- This prototype does not perform network crawling. The user supplies the article HTML or local files to keep provenance explicit.
- No external dependencies.

Source: self-contained demo by Marmalade the museum cat.