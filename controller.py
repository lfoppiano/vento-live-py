import codecs
import pickle
import json

from bottle import route, get, post, run, request, static_file
from twython import Twython

analyzerFileName = "analyzer.bin"

APP_KEY = 'eZiVzssOUBEAEH1gpUTRojJC0'
APP_SECRET = 'YudBmN1zk5Hnd8BKnHX8fdvKqGu469hUlsG9ElwboLwq884srM'
OAUTH_TOKEN = '706953-Wx7sfvtz7XZiAm46gfOhcdVHTDJEBlLc70h9E856WbS'
OAUTH_TOKEN_SECRET = 'IngBWD7nAN7hp3RHeZxiTRc3l3NukFLYehrIigBNXfIqs'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def restore(filename):
    f = open(filename, 'rb')
    loaded = pickle.load(f)
    f.close()
    return loaded


analyzer = restore(analyzerFileName)


@get('/classification/twitter')
def classifyTweets():
    params = dict()

    lang = request.query.lang if request.query.lang else 'en'
    result_type = 'recent'
    count = 2000
    query = request.query.query if request.query.query else ""

    # twits = twitter.search(q="france")
    twits = twitter.search(q=query, count=count, result_type=result_type, lang="en")
    results = ([{'text': twit['text'], 'score': analyzer.classify(twit['text'])} for twit in twits['statuses']])

    return json.dumps(results)


@post('/classification/text')
def classifyText():
    text = request.forms.get("text")
    return "Text: '" + text + "' . score: " + analyzer.classify(text)


@route('/vento-live/<filepath:path>')
def webStatic(filepath):
    return static_file(filepath, root='./vento-live')


def loadFile(filename):
    print("Loading", filename)
    with codecs.open(filename, 'rb') as storage_file:
        # The protocol=2 parameter is for python2 compatibility
        pickle.load()


run(host='localhost', port=8080, debug=True)
