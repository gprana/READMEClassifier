# chatbot
## 開発環境
### OS
バージョンの確認
```
$ cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.1 LTS"
```
アーキテクチャの確認
```
$ arch
x86_64
```
### Python仮想環境の作成
pyvenvのインストール
```
$ sudo apt install python3-venv
```
仮想環境の作成。chatbotEnvというフォルダに環境が保存される。
```
$ pyvenv chatbotEnv
```
アクティベートの実行
```
$ source chatbotEnv/bin/activate
```
仮想環境から抜ける
```
$ deactivate
```
### 各種ライブラリのインストール
Tkinterのインストール
```
$ sudo apt install -y python3-tk
```
NLTK(Natural Language Tool Kit)のインストール
```
$ sudo pip3 install -U nltk
...
Successfully installed nltk-3.2.1
```
NumPyのインストール
```
$ sudo pip3 install -U numpy
...
Successfully installed numpy-1.11.1
```
Matplotlibのインストール
```
$ sudo pip3 install -U matplotlib
...
Successfully installed cycler-0.10.0 matploglib-1.5.2 pyparsing-2.1.8 python-dateutil-2.5.3 pytz-2016.6.1
```
