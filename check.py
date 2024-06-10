import re

# Sample HTML content
html_content = """
<html>
<head><title>Test Page</title></head>
<body>
    <a href="https://example.com/page1">Page 1</a>
    <a href="https://example.com/page2">Page 2</a>
    <a href="https://example.com/page3">Page 3</a>
</body>
</html>
"""

# Regex pattern to match <a> tags with href attributes and capture the URLs
pattern = r'(?:<a\s+)href="(.+)"(?:>.+</a>)'

# Find all URLs in the HTML content
urls = re.findall(pattern, html_content)

# Print the extracted URLs
for url in urls:
    print(url)
