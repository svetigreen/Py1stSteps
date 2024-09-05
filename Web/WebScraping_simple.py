from urllib.request import urlopen
import re
import gzip
from io import BytesIO

p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')

# Open the URL and read the headers and content
response = urlopen('http://python.org/jobs')

# Check if the content is compressed
if response.info().get('Content-Encoding') == 'gzip':
    # Decompress the response content
    buf = BytesIO(response.read())
    f = gzip.GzipFile(fileobj=buf)
    text = f.read().decode('utf-8')
else:
    # Decode the content as plain utf-8
    text = response.read().decode('utf-8')

# Find and print job URLs and names
for url, name in p.findall(text):
    print('{} ({})'.format(name, url))
