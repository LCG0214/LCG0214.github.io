import os
import qiniu

# 获取环境变量中的 Access Key 和 Secret Key
access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')
# 创建 Auth 对象
auth = qiniu.Auth(access_key, secret_key)
# 创建 CDN 管理对象
cdn_manager = qiniu.CdnManager(auth)
# 要刷新的 URL 列表
urls = [
    'https://www.lcgui.cn'
]
# 刷新缓存
response, info = cdn_manager.refresh_urls(urls)
# 打印结果
resp_code = response.get('code')
if resp_code == 200:
    print('刷新成功')
else:
    print('刷新失败')
# print(info)
