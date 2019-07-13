import sys
import os
import json
import datetime
import eml_parser
from bs4 import BeautifulSoup

def json_serial(obj):
    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial

def tokenize(text):
    return text.split(' ')

def parse_content(content):
    cleantext = BeautifulSoup(content, "lxml").text
    terms = tokenize(cleantext)
    print(' '.join(terms))

def main(args):
    for root, dirs, files in os.walk("./data"):
        path = root.split(os.sep)
        for file in files:
            f_ext = file.split('.')[-1]
            f_path = root + os.sep + file;
            if f_ext == "eml":
                with open(f_path, 'rb') as fh:
                    raw_email = fh.read()
                    parsed_eml = eml_parser.eml_parser.decode_email_b(raw_email, True)
                    #print(json.dumps(parsed_eml, default=json_serial))
                    if "body" in parsed_eml:
                        for e_body in parsed_eml["body"]:
                            parse_content(e_body["content"])


main(sys.argv)
