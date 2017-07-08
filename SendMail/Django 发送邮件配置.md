# Django 使用 QQ / 新浪邮箱发送邮件配置

### 环境：
- python 2.7 or 3.5
- django 1.9 or 1.10

## 先说 QQ 邮箱：

**第一步，首先需要一个 QQ 邮箱授权码：**
进入QQ 邮箱点击设置

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1430985-002819268fa04553.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

** 第二步，开启服务，并且生成授权码**


![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1430985-306c32b9c08adc6e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

** 第三步， setting.py 配置**
```python
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'xxx@qq.com' # 你的 QQ 账号
EMAIL_HOST_PASSWORD = '刚刚复制的授权码（不是你的 QQ 密码！！！）'
EMAIL_USE_TLS = True # 这里必须是 True，否则发送不成功
EMAIL_FROM = 'xxx@qq.com' # 你的 QQ 账号
```
EMAIL_HOST_USER  和 EMAIL_USE_TLS 最好保持一致

** 第四步，发送邮箱的逻辑**
```python
from django.core.mail import send_mail

email_title = '邮件标题'
email_body = '邮件内容'
email = 'xxx@xxx.com'  #对方的邮箱
send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

if send_status:
    # 发送成功
```

参考 [腾讯 QQ 邮箱](https://kf.qq.com/faq/120322fu63YV130422nqIrqu.html)

---


## 新浪邮箱就比较简单了

![新浪邮箱](http://upload-images.jianshu.io/upload_images/1430985-c08b44394f1bf3e3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
开启服务

```python
EMAIL_HOST = "smtp.sina.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "xxx@sina.com" # 你的邮箱账号
EMAIL_HOST_PASSWORD = "xxxx" # 你的邮箱密码
EMAIL_USE_TLS = False # 这里是 False
EMAIL_FROM = "xxx@sina.com"  # 你的邮箱账号
```

---
以上两种方法亲测都能成功发送邮件，如果帮到了您，请点赞 ：)


如果对您有帮助，请点击喜欢，谢谢~
