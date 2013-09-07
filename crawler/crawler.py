import json
import urllib2
from urllib import urlencode

#url http://www.google.com/search?oe=utf8&ie=utf8&source=uds&start=0&hl=en&q=consoliate
def showsome(searchfor,depth):
        query = urlencode({'q': searchfor})
        for i in range(depth):
            try:
                url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s&rsz=8&start=%s&key{AIzaSyDXSvxLx2cSAaKmZLw5ISrPuhqJmT701_I}' % (query,i)
                req = urllib2.Request(url)
                req.add_header('User-agent', 'Mozilla 3.10')
                search_response = urllib2.urlopen(req)
                search_results = search_response.read()
                results = json.loads(search_results)
                data = results['responseData']
                print 'Total results: %s' % data['cursor']['estimatedResultCount']
                hits = data['results']
                print 'Top %d hits:' % len(hits)
                print 'For more results, see %s' % data['cursor']['moreResultsUrl']
                for h in hits: 
                    if "consoliate" in h['url']:
                        print "Crawling... " + h['url']
                        urllib2.urlopen(h['url'])
                        pass
            except Exception,e:
                print e
                break

showsome('consoliate',50)
