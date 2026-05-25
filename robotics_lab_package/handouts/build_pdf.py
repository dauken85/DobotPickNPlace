"""Combine all session handouts into a single PDF via Edge headless print."""
import subprocess, sys, os, markdown

HANDOUTS_DIR = os.path.dirname(__file__)
OUTPUT_HTML  = os.path.join(HANDOUTS_DIR, "_all_sessions_combined.html")
OUTPUT_PDF   = os.path.join(HANDOUTS_DIR, "student_handouts_all_sessions.pdf")
EDGE         = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

SESSION_FILES = [
    "student_handout_session_1.md",
    "student_handout_session_2.md",
    "student_handout_session_3.md",
    "student_handout_session_4.md",
    "student_handout_session_5.md",
    "student_handout_session_6.md",
    "student_handout_session_7.md",
    "student_handout_session_8.md",
]

CSS = """
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  font-size: 14px;
  line-height: 1.6;
  color: #24292e;
  max-width: 900px;
  margin: 0 auto;
  padding: 40px;
}
h1 { font-size: 2em; border-bottom: 1px solid #eaecef; padding-bottom: .3em; margin-top: 1.5em; }
h2 { font-size: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: .3em; margin-top: 1.2em; }
h3 { font-size: 1.25em; margin-top: 1em; }
code {
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 85%;
  background: #f6f8fa;
  border-radius: 3px;
  padding: .2em .4em;
}
pre {
  background: #f6f8fa;
  border-radius: 6px;
  padding: 16px;
  overflow: auto;
  line-height: 1.45;
}
pre code { background: none; padding: 0; font-size: 100%; }
blockquote {
  color: #6a737d;
  border-left: .25em solid #dfe2e5;
  padding: 0 1em;
  margin: 0;
}
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th, td { border: 1px solid #dfe2e5; padding: 6px 13px; }
th { background: #f6f8fa; font-weight: 600; }
tr:nth-child(even) td { background: #f6f8fa; }
hr { border: none; border-top: 1px solid #eaecef; margin: 24px 0; }
ul, ol { padding-left: 2em; }
li { margin: .25em 0; }

/* Each session starts on a new page */
.session { page-break-before: always; }
.session:first-child { page-break-before: auto; }

@media print {
  body { padding: 0; max-width: 100%; }
  .session { page-break-before: always; }
  .session:first-child { page-break-before: auto; }
}
"""

md = markdown.Markdown(extensions=["fenced_code", "tables", "nl2br"])

parts = []
for i, fname in enumerate(SESSION_FILES):
    path = os.path.join(HANDOUTS_DIR, fname)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    md.reset()
    html = md.convert(text)
    cls = "session" if i > 0 else "session"
    parts.append(f'<div class="session">{html}</div>')

body = "\n".join(parts)
full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Student Handouts — All Sessions</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"HTML written: {OUTPUT_HTML}")

result = subprocess.run(
    [EDGE, "--headless", "--disable-gpu", f"--print-to-pdf={OUTPUT_PDF}",
     "--print-to-pdf-no-header", OUTPUT_HTML],
    capture_output=True, text=True, timeout=60
)

if result.returncode == 0 and os.path.exists(OUTPUT_PDF):
    size = os.path.getsize(OUTPUT_PDF)
    print(f"PDF written: {OUTPUT_PDF}  ({size:,} bytes)")
else:
    print("Edge stdout:", result.stdout)
    print("Edge stderr:", result.stderr)
    sys.exit(1)
