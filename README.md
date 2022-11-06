# Pythonつかって Mastodon で toot

## 用途

タイトル通りpythonを利用してMastodonでtootします

## 準備

* pythonが利用できる環境
* `requests`が利用できる環境
* `mastodon.py`が利用できる環境
* MastodonAPI認証情報

### `requests`, `mastodon.py`について

`requests`, `mastodon.py`を利用しているので事前に`pip`または`pip3`でインストールが必要です

```sh
# 例
pip install requests mastodon.py
```

### MastodonAPI認証情報について

Mastodonを外部から利用する場合、認証情報が別途必要です。
必要な認証情報を`gen-secret.py`を実行することでファイルに保存されます。
ファイルは2つあり以下になります。
*このファイル名である必要はありません。今回のスクリプト用です*

* `.client-id.secret`
* `.access-token.secret`

なおこれは`git`の追跡対象外となるように`.gitignore`を設定してあります。

### 注意事項

認証情報は接続するサーバごとに必要になります。
`gen-secret.py`は`http://mstdn.jp`用に作成してありますので必要に応じて変更してください。
