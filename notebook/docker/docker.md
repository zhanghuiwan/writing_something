# docker

推荐网址：https://yeasy.gitbook.io/docker_practice





## 常用命令



```bash

# 列出已经下载的镜像
docker image ls

docker ps

```



```bash
# 容器操作

# 输出一个 “Hello World”，之后终止容器
docker run ubuntu:18.04 /bin/echo 'Hello world'

# 交互模式
# -t 选项让Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上， -i 则让容器的标准输入保持打开
docker run -t -i ubuntu:18.04 /bin/bash
docker run -it ubuntu:18.04 /bin/sh

# 守护态运行（后台运行），添加-d参数。输出不会显示在前台（下面的 -c 是传递给 /bin/sh 的选项，它的作用是告诉 sh 执行后面的字符串作为命令。）
docker run -d ubuntu:18.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"

# 列出 container 的信息，查看container的logs
docker container ls
docker container ls -a
docker container logs [container ID or NAMES]

# 终止
docker container stop
容器中只有一个应用时，使用exit命令或者Ctrl+d退出该应用，容器也会终止
docker container start
docker container restart

# 进入容器
ocker exec -it [container ID or NAMES] /bin/bash


# 删除容器
# 删除一个终止状态的容器
docker container rm [container ID or NAMES]
# 删除一个运行状态的容器
docker container  -f rm [container ID or NAMES]
# 删除所有终止状态的容器
docker container prune
```



```bash
# 挂载卷和挂载主机目录
# 卷相当于时docker所共有的，由docker来管理，镜像或者容器被删除时，也不会影响到卷；挂载目录就是挂载主机的目录

# 创建卷
docker volume create my-vol
docker volume ls

# 查看指定卷的信息
docker volume inspect my-vol

# 创建一个名为 web 的容器，并加载一个 数据卷 到容器的 /usr/share/nginx/html 目录
docker run -d -P \
    --name web \
    # -v my-vol:/usr/share/nginx/html \
    --mount source=my-vol,target=/usr/share/nginx/html \
    nginx:alpine

# 查看容器的具体信息，数据卷 信息在 "Mounts" Key 下面
docker inspect web

"Mounts": [
    {
        "Type": "volume",
        "Name": "my-vol",
        "Source": "/var/lib/docker/volumes/my-vol/_data",
        "Destination": "/usr/share/nginx/html",
        "Driver": "local",
        "Mode": "",
        "RW": true,
        "Propagation": ""
    }
],

# 删除数据卷
$ docker volume rm my-vol


# 挂载主机目录，加载主机的 /src/webapp 目录到容器的 /usr/share/nginx/html目录

docker run --mount type=bind,source=/host/directory,target=/container/directory other_options image_name

$ docker run -d -P \
    --name web \
    # -v /src/webapp:/usr/share/nginx/html \
    --mount type=bind,source=/src/webapp,target=/usr/share/nginx/html \
    nginx:alpine

$ docker inspect web
"Mounts": [
    {
        "Type": "bind",
        "Source": "/src/webapp",
        "Destination": "/usr/share/nginx/html",
        "Mode": "",
        "RW": true,
        "Propagation": "rprivate"
    }
],

# 一个小应用，将histoty挂载到容器，则能共享history
$ docker run --rm -it \
   # -v $HOME/.bash_history:/root/.bash_history \
   --mount type=bind,source=$HOME/.bash_history,target=/root/.bash_history \
   ubuntu:18.04 \
   bash

root@2affd44b4667:/# history
1  ls
2  diskutil list
```





