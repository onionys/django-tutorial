

    > git config --global user.email <your email>
    input your email
    > git config --global user.name <your name or id>
    input your name

## push to github...

要先設定好帳號和使用者名稱，註冊好github 帳號。

到github 上面建一個 repo ，用GUI介面。

把電腦上的專案push上去。

專案位置:https://github.com/onionys/django-tutorial.git

    > git remote add origin https://github.com/onionys/django-tutorial.git

上面那個origin好像是自行幫遠端repo取的名字。

可以有多個 remote repo ? 怎麼設定?


### push 到多個repo

到遠方建立一個新的repo....假設該位置是 https://github.com/onionys/django-test.git

在local 的專案之中，多加一個遠方的設定如下:

    > git remote add test2 https://github.com/onionys/django-test.git

test2 是你自已取的名字，通常該專案在你電腦中的第一個版本的名字會是 "origin"

    > git push test2 master

    test2 是遠端倉庫的名字

    master 是branch的名字。

## Fork 
