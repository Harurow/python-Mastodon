#!/usr/local/bin/python3

import getpass

import requests
from mastodon import Mastodon

url = "https://mstdn.jp"
app_name = input('app name: ')

# mstdn.jp User-Agentを指定しないと403エラーとなる
sess = requests.Session()
sess.headers.update({"User-Agent": f"{app_name}/v0"})

# Mastodonのアプリ登録を行ないます。
Mastodon.create_app(app_name,
                    api_base_url=url,
                    to_file=".client-id.secret",
                    session=sess
                    )
print('succeeded.')

print('** login **')
email = input('e-mail: ')
password = getpass.getpass('password: ')

mastodon = Mastodon(
    client_id=".client-id.secret",
    api_base_url=url,
    session=sess)

mastodon.log_in(
    email,
    password,
    to_file=".access-token.secret")

print('succeeded.')

print('fin.')
