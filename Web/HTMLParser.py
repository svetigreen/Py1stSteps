from urllib.request import urlopen
from html.parser import HTMLParser
import gzip
from io import BytesIO


def isjob(url):
    try:
        a, b, c, d = url.split('/')
    except ValueError:
        return False
    return a == d == '' and b == 'jobs' and c.isdigit()


class Scraper(HTMLParser):
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        url = attrs.get('href', '')
        if tag == 'a' and isjob(url):
            self.url = url
            self.in_link = True
            self.chunks = []

    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self.in_link:
            print('{} ({})'.format(''.join(self.chunks), self.url))
            self.in_link = False


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

parser = Scraper()
parser.feed(text)
parser.close()
