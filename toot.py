#!/usr/local/bin/python3

from mastodon import Mastodon
import requests

url = "https://mstdn.jp"

# mstdn.jp User-Agentを指定しないと403エラーとなる
sess = requests.Session()
sess.headers.update({"User-Agent": "bot/v0"})

mastodon = Mastodon(
    client_id=".client-id.secret",
    access_token=".access-token.secret",
    api_base_url=url,
    session=sess)

mastodon.toot("Pythonからトゥート")
