# 秀秀的网页

### Run

```bash
docker run -d -v PHOTO_FOLDER:/opt/web/app/static/upload -p 8000:8000 playniuniu/xiuxiu-demo
```

### Nginx 配置

Nginx 反代文件如下所示:

```nginx
server {
    listen 80;
    server_name www.example.com;

    location / {
        proxy_pass http://127.0.0.1:8000/;
        proxy_redirect     off;
        proxy_set_header   Host                 $host;
        proxy_set_header   X-Real-IP            $remote_addr;
        proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto    $scheme;
    }
}
```

### 技术栈

1. 前端使用 [jQuery WeUI](http://jqweui.com/)

2. 后端使用 Flask 和 meinheld

3. 使用 Docker 封装

#### 关于 Flask 的编写说明

1. 更改了 **static_url_path** 的默认路径

2. 使用工厂模式初始化 Flask App

3. 使用 [meinheld](https://github.com/mopemope/meinheld) 来运行 Flask
