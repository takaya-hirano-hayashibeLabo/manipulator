#Github

## 基本操作

#### 自分のアカウントを登録したとき

~~~
git config --global user.name {githubのユーザーネーム} #ユーザーネームの登録
git config --global user.email {githubのメールアドレス} #ユーザーメールアドレス
~~~

#### githubからレポジトリを取ってくるとき

~~~
git init #ローカルリポジトリの初期化 (まだやってないときだけ)
git pull https://github.com/takaya-hirano-hayashibeLabo/manipulator.git (リモ―トから取ってくる)
~~~

#### ローカルにコードを登録するとき

~~~
git branch {ブランチ名} #ローカルにブランチを作成 (やってないときだけ)
git switch {ブランチ名} #ブランチの切り替え
git add . #ステージにコードを上げる
git commit -m "{コメント}" #ブランチにコードを登録
~~~

#### githubに上げるとき

~~~
git remote origin https://{githubのユーザーネーム}@github.com/takaya-hirano-hayashibeLabo/manipulator.git #リモートの登録 (やってないときだけ)
git push origin {ブランチ名} #リモートにローカルの変更を登録
~~~

## 補足

#### ブランチの確認

~~~
git branch -a
~~~

#### リモートの確認

~~~
git remote -v
~~~

#### リモートのリポジトリを消すとき

~~~
git remote remove origin
~~~