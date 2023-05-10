# mujocoの環境構築

gymをいれたら、次にmujocoを入れます。

ざっくりとした違いは、gymは2Dで、mujocoは3Dです。

## 1. mujocoダウンロード

↓こちらのリンクにアクセスします。

https://github.com/deepmind/mujoco/releases/tag/2.1.0

「mujoco210-windows-x86_64.zip」をダウンロード&解凍します。(どこでもいい)

## 2. .mujocoフォルダの作成

C:\Users\{自分のユーザーネーム}

に「.mujoco」フォルダを作成します。

### 作ったのに.mujocoファイルが見えないとき

隠しフォルダを見える用に設定します。

## 3. mujoco210フォルダの作成

今作った .mujoco フォルダの中に「mujoco210」フォルダを作成します。

## 4. mujoco210フォルダにダウンロードしたファイルをコピー

ダウンロードしたファイルの中身をmujoco210フォルダの中にコピーします。

## 5. mujocoのライセンスキーの取得

このままではmujocoファイルにはロックが掛かっているので使えません。

そのためアクセスキーをダウンロードします。

↓こちらのリンクにアクセスします。

https://www.roboti.us/license.html

「Activation Key」をクリックしてアクセスキーをダウンロードします。

## 6. mujoco-pyのpip install

pip install mujoco-py==2.1.2.14

## 一旦テストプログラムを動かしてみる

ほぼ100%エラーが出るが一旦動かしてみる。

(パソコンでアプリのビルドとかしたことある人とかなら1発でいけるかもしれないから)

~~~
import gym
import time

def main():

    env=gym.make("Ant-v3")
    env.reset()
    for _ in range(100):
        s,_,_,_,=env.step(env.action_space.sample())
        env.render()
        time.sleep(0.05)
    env.close()

if __name__=="__main__":
    main()
~~~

上手くいくと、4脚のアリがバタバタする動画がでる。


# エラーの解消

## Visual C ++ がないとき

↓こちらのリンクをクリックします。

https://visualstudio.microsoft.com/ja/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&passive=false&cid=2030

自動でダウンロードされます。

ダウンロードが完了したら vs_community_XXXXXXXXXXXX.exeをクリックしてインストールします。

そこそこ時間がかかるのでしばらく待ちましょう。