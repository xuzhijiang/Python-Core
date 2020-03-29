#### Requests lib的7个主要方法

* requests.request(method, url, **kwargs)  构造一个请求，支撑以下各方法的基础方法
* requests.get() 获取HTML网页的主要方法，对应于HTTP的GET
* requests.head() 获取HTML网页头信息的方法，对应于HTTP的HEAD,获得该资源的头部信息
* requests.post() 向HTML网页提交POST请求的方法，对应于HTTP的POST,请求向URL位置的资源后附加新的数据
* requests.put() 向HTML网页提交PUT请求的方法，对应于HTTP的PUT,覆盖原URL位置的资源
* requests.patch() 向HTML网页提交局部修改请求，对应于HTTP的PATCH,局部更新URL位置的资源，即改变该处资源的部分内容
* requests.delete() 向HTML页面提交删除请求，对应于HTTP的DELETE,请求删除URL位置存储的资源

#### Response对象的属性

* r.status_code HTTP请求的返回状态， 200表示连接成功， 404表示失败
* r.text HTTP响应内容的字符串形式，即， url对应的页面内容
* r.encoding 从HTTP header中猜测的响应内容编码方式(不靠谱),如果header中不存在charset，则认为编码为ISO‐8859‐1
r.text根据r.encoding显示网页内容,所以这个猜测不靠谱
* r.apparent_encoding 从内容中分析出的响应内容编码方式（备选编码方式,比较靠谱）
* r.content HTTP响应内容的二进制形式

#### requests库的异常

* requests.ConnectionError 网络连接错误异常，如DNS查询失败、拒绝连接等
* requests.HTTPError HTTP错误异常
* requests.URLRequired URL缺失异常
* requests.TooManyRedirects 超过最大重定向次数，产生重定向异常
* requests.ConnectTimeout 连接远程服务器超时异常
* requests.Timeout 请求URL超时，产生超时异常
* r.raise_for_status() 如果不是200，产生异常 requests.HTTPError

#### PUT和PATCH的区别

    假设URL位置有一组数据UserInfo，包括UserID、 UserName等20个字段

* 需求：用户修改了UserName，其他不变
* 采用PATCH，仅向URL提交UserName的局部更新请求
* 采用PUT，必须将所有20个字段一并提交到URL，未提交字段被删除
* PATCH的最主要好处：节省网络带宽

##### Requests库的POST方法

> 向URL POST一个字典自动编码为form（表单）,

```python
payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.post('http://httpbin.org/post', data = payload)
>>> print(r.text)
{ ...
"form": {
"key2": "value2",
"key1": "value1"
}
```

> 向URL POST一个字符串自动编码为data

```python
 r = requests.post('http://httpbin.org/post', data = 'ABC')
>>> print(r.text)
{ ...
"data": "ABC"
"form": {},
}
```

##### Requests库的PUT方法

> 和post方法类似，只不过把data数据覆盖了

```python
payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.put('http://httpbin.org/put', data = payload)
>>> print(r.text)
{ ...
"form": {
"key2": "value2",
"key1": "value1"
},
}
```

##### Requests库的request方法

> requests.request(method, url, **kwargs),
其中**kwargs: 控制访问的参数，均为可选项

###### params


> params : 字典或字节序列，作为参数增加到url中

```python
kv = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.request('GET', 'http://python123.io/ws', params=kv)
>>> print(r.url)
http://python123.io/ws?key1=value1&key2=value2
```

###### data

> 字典、字节序列或文件对象，作为Request的内容

```python
kv = {'key1': 'value1', 'key2': 'value2'}
r = requests.request('POST', url, data=kv)
body = '主体内容'
r = requests.request('POST', url, data=body)
```

###### json

>  JSON格式的数据，作为Request的内容

```python
kv = {'key1': 'value1'}
r = requests.request('POST', url, json=kv)
```

###### headers

> 字典， HTTP定制头,可以模拟任何浏览器

```python
hd = {'user-agent': 'Chrome/10'}
r = requests.request('POST', url, headers=hd)
```

###### cookies

> 字典或CookieJar， Request中的cookie

###### auth

> 元组，支持HTTP认证功能

###### files

> 字典类型，传输文件

```python
fs = {'file': open('data.xls', 'rb')}
r = requests.request('POST', url, files=fs)
```

###### timeout

> 设定超时时间，秒为单位

```python
r = requests.request('GET', url, timeout=30)
```

###### proxies

> 字典类型，设定访问代理服务器，可以增加登录认证

```python
>>>pxs = { 'http': 'http://user:pass@10.10.10.1:1234'
'https': 'https://10.10.10.1:4321' }
>>> r = requests.request('GET', 'http://www.baidu.com', proxies=pxs)
```

###### allow_redirects

> True/False，默认为True，重定向开关

###### stream

> True/False，默认为True，获取内容立即下载开关

###### verify

> True/False，默认为True，认证SSL证书开关

###### cert

> 本地SSL证书路径

##### requests的get方法

> requests.get(url, params=None, **kwargs)

* params : url中的额外参数，字典或字节流格式，可选
* **kwargs: 12个控制访问的参数

##### requests的post方法

> requests.post(url, data=None, json=None, **kwargs)

* url : 拟更新页面的url链接
* data : 字典、字节序列或文件， Request的内容
* json : JSON格式的数据， Request的内容
* **kwargs: 12个控制访问的参数

#### Response

* Response.content: 返回内容的二进制形式