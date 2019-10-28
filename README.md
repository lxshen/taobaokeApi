# taobaokeApi

Python淘宝客接口支持 

* 所有环境 
```
python3  requests
```
* 安装 
```
    pip instatll lx_taobaoke
```

* 使用方法
```
# -*-coding: utf-8 -*-
from lx_taobaoke import ToaBaoKeApi

app_tions = [
    # 第一个
    {
        'appkey': 23565473,
        'secret': '781bec497f0a825ddfa4be2f91654318'
    },
    # 第二个
]
# 佣金授权码信息，可添加多个，随机使用
commission_tions =  [
    {
        'adzone_id': '80502883',
        'site_id': '24092591',
        'session': '700001007331678779fc503b567d7ff4afef59135766e1001f5ceb5c8ec9eed7d9e88ba2891351154',
    },
]
"""
item_id : 淘宝ID
activity_id： 优惠券ID
"""
taobaoke = ToaBaoKeApi(app_tions, commission_tions)
# 获取优惠券信息
result = taobaoke.get_coupon_api(item_id=589351083986, activity_id="287beee1c8eb4432a36aecfdf4ed3e7a")
# 获取佣金信息
# result = taobaoke.get_commission_api(item_id=589351083986)
# 获取商品类别信息
# result = taobaoke.get_category_api(item_id=560376846858)
print(result)
```