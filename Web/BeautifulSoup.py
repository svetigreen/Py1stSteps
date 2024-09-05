from urllib.request import urlopen
from bs4 import BeautifulSoup
import gzip
from io import BytesIO

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

soup = BeautifulSoup(text, 'html.parser')
jobs = set()

for job in soup.body.section('h2'):
    print('{}'.format(job))
    jobs.add('{} ({})'.format(job.a.string, job.a['href']))

print('\n'.join(sorted(jobs, key=str.lower)))

