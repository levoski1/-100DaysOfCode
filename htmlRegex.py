#!/usr/bin/python3

import re

url = '''
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample Webpage</title>
</head>
<body>
    <h1>Welcome to Sample Webpage</h1>
    <p>This is a sample webpage with some <a href="https://www.example.com">external link</a>.</p>
    <ul>
        <li><a href="page1.html">Page 1</a></li>
        <li><a href="page2.html">Page 2</a></li>
        <li><a href="page3.html">Page 3</a></li>
    </ul>
    <a href="mailto:info@example.com">Contact Us</a>
</body>
</html>
"""
'''

pattern = re.compile(r'(?:<a\s+)href="(.+)"(?:>.+</a>)')
matches = pattern.findall(url)


for match in matches:
    print(match)
