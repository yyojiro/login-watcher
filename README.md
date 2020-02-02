# これは何？
sshログイン（のログ）を監視するやつと監視した結果を表示するやつ。

## watcher
swatchで/var/log/secureを監視した結果をHTTPでpostする仕掛け。
そしてこれをセットアップするansible-playbook。

## log_view
監視したログをDBにためて表示するツール。
Flaskとかsqlite使用。
python3で動いてるので、先にpython3をインストールすること、
```commandline
$ pip3 install -r requirements.txt
$ python ./initdb.py
$ python webapp.py
```

# 動作環境
CentOS7、python3.6で動作確認済み。

