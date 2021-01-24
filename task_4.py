import hashlib
from uuid import uuid4
salt = uuid4().hex
cache_dict = dict()

def cache_page(url):
    if int(len(cache_dict)) == 0:
        key = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        cache_dict[key] = url
    else:
        n=0 # Флаг-костыль. Извините, мозг спит, что придумал в первом часу ночи))
        for i in (cache_dict.values()):
            if i == url:
                print("Данный адрес есть в кеше")
                n=1
                break
        if n==0:
            key = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
            cache_dict[key]=url

cache_page("yandex.ru")
cache_page("google.com")
cache_page("yandex.ru")