import gzip as gz
import json 
with gz.open("pubmed_2022_tiny.jsonl.gz") as text:
    text = text.read()
    text = text.decode("utf-8")
    text = json.loads(text)
    print(type(text))
    #f = open("exemplo.txt", "x")
    #f.write(str(text))
    #f.close()
    