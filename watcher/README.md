# swatchを使ったログイン監視設定
監視した結果を指定のURLにpostする。
適当にtargetの内容書き換えてansible-playbookでインストール。

```
# cd playbook
# vi target
# ansible-playbook -i target setup.yml
```
