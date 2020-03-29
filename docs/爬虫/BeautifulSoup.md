### BeautifulSoup类

> BeautifulSoup类对应一个HTML/XML文档的全部内容

```python
soup = BeautifulSoup('<html>data</html>', 'html.parser')
soup2 = BeautifulSoup(open('d://demo.html'), 'html.parser')
```

#### BeautifulSoup的解析器

| 解析器 | 使用方法 | condition |
| ------ |--------|----------|
|bs4的HTML解析器| BeautifulSoup(mk,'html.parser')|安装bs4库|
|lxml的HTML解析器| BeautifulSoup(mk,'lxml')| pip install lxml|
|lxml的XML解析器 |BeautifulSoup(mk,'xml') |pip install lxml
|html5lib的解析器 |BeautifulSoup(mk,'html5lib')| pip install html5lib

#### BeautifulSoup类的基本元素

> &lt;p class=“title”> … &lt;/p>

| 基本元素 | 说明 |
|---------|------|
|Tag |标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾|
|Name |标签的名字， <p>…</p>的名字是'p'，格式： <tag>.name|
|Attributes |标签的属性，字典形式组织，格式： <tag>.attrs|
|NavigableString |标签内非属性字符串， <>…</>中字符串，格式： <tag>.string|
|Comment |标签内字符串的注释部分，一种特殊的Comment类型|

##### Tag

* 任何存在于HTML语法中的标签都可以用soup.<tag>访问获得
* 当HTML文档中存在多个相同<tag>对应内容时， soup.<tag>返回第一个

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo, 'html.parser')
print(soup.title)
print(soup.a)
```

##### Tag的名字,Name

* 标签的名字， &lt;p&gt;…&lt;/p&gt;的名字是'p'，格式： <tag>.name
* 每个<tag>都有自己的名字，通过<tag>.name获取，字符串类型

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo, 'html.parser')
soup.a.name
soup.a.parent.name
```

##### Tag的attrs（属性）

* 一个<tag>可以有0或多个属性，字典类型

```python
tag = soup.a
tag.attrs
tag.attrs['class']
tag.attrs['href']
>>print(type(tag.attrs))
<class 'dict'>
>>type(tag)
<class 'bs4.element.Tag'>
```

##### Tag的NavigableString

* NavigableString可以跨越多个层次

```python
soup.a
soup.a.string
soup.p
soup.p.string
type(soup.p.string)
<class 'bs4.element.NavigableString'>
```

##### Tag的Comment

* Comment是一种特殊类型

```python
newsoup = BeautifulSoup('<b><!--This is a comment!--></b><p>This is not a comment!!</p>', 'html.parser')
>>print(newsoup.b.string)
'This is a comment!'
>>print(type(newsoup.b.string))
<class 'bs4.element.Comment'>
>>newsoup.p.string
'This is not a comment!!'
>>print(type(newsoup.p.string))
<class 'bs4.element.NavigableString'>
```

```shell
标签 <tag> -> <p class=“title”>…</p>
名称 .name 属性 .attrs 	非属性字符串/注释.string
```

### 基于bs4库的HTML内容遍历方法

> <>…</>构成了所属关系，形成了标签的树形结构

#### 标签树的遍历

* 上行遍历: 从标签树的下面往上面遍历
* 下行遍历: 从标签树的上面往上面遍历
* 平行遍历：在标签树的平行节点上遍历

##### 标签树的下行遍历

* BeautifulSoup类型是标签树的根节点

|属性 | 说明|
|-----|-----|
|.contents |子节点的列表，是列表类型,将<tag>所有儿子节点存入列表|
|.children |子节点的迭代类型，与.contents类似，用于循环遍历儿子节点|
|.descendants| 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历|

* The last two are iteration type.

```python
soup = BeautifulSoup(demo, 'html.parser')
soup.head
soup.head.contents
soup.body.contents
len(soup.body.contents)
soup.body.contents[1]
```

> 遍历儿子节点

```python
for child in soup.body.children:
    print(child)
```

> 遍历子孙节点

```python
for child in soup.body.descendants:
    print(child)
```

#### 标签树的上行遍历

|属性 | 说明|
|-----|-----|
|.parent|节点的父亲标签|
|.parents |节点先辈标签的迭代类型，用于循环遍历先辈节点|

```python
soup = BeautifulSoup(demo, 'html.parser')
>>soup.title.parent
<head><title>This is a python demo page</title></head>
>>soup.html.parent
整个html网页
soup.parent
```

* 遍历所有先辈节点，包括soup本身，所以要区别判断

```python
soup = BeautifulSoup(demo, 'html.parser')
for parent in soup.a.parents:
	if parent is None:
		print(parent)
	else:
		print(parent.name)
```

#### 标签树的平行遍历

|属性 | 说明|
|-----|-----|
|.next_sibling | 返回按照HTML文本顺序的下一个平行节点标签|
|.previous_sibling |返回按照HTML文本顺序的上一个平行节点标签|
|.next_siblings |迭代类型，返回按照HTML文本顺序的后续所有平行节点标签|
|.previous_siblings |迭代类型，返回按照HTML文本顺序的前续所有平行节点标签|

* The last two are iteration type.
* 平行遍历发生在同一个父节点下的各节点间

```python
>>soup = BeautifulSoup(demo, 'html.parser')
>>soup.a.next_sibling
and
>>soup.a.next_sibling.next_sibling
>>soup.a.previous_sibling.previous_sibling
>>soup.a.parent
```

* 遍历后续节点

```python
for sibling in soup.a.next_sibling:
	print(sibling)
```

* 遍历前序节点

```python
for sibling in soup.a.previous_sibling:
	print(sibling)
```

#### prettify output

* .prettify()为HTML文本<>及其内容增加更加'\n'
* .prettify()可用于标签，方法： <tag>.prettify()

```python
soup.prettify()
soup.a.prettify()
```

#### Encoding

> bs4库将任何HTML输入都变成utf‐8编码,Python 3.x默认支持编码是utf‐8,解析无障碍

```python
soup = BeautifulSoup('<p>中文</p>', 'html.parser')
soup.p.string
print(soup.p.prettify())
```

#### 基于bs4库的html内容查找方法

> 返回一个列表类型，存储查找的结果

* name : 对标签名称的检索字符串
* attrs: 对标签属性值的检索字符串，可标注属性检索
* recursive: 是否对子孙全部检索，默认True
* string: <>…</>中字符串区域的检索字符串

```python
<>.find_all(name, attrs, recursive, string, **kwargs)
```

* <tag>(..) 等价于 <tag>.find_all(..)
* soup(..) 等价于 soup.find_all(..)

##### 扩展方法

|方法 |说明|
|-----|----|
|<>.find() |搜索且只返回一个结果，同.find_all()参数|
|<>.find_parents() |在先辈节点中搜索，返回列表类型，同.find_all()参数|
|<>.find_parent() |在先辈节点中返回一个结果，同.find()参数|
|<>.find_next_siblings() |在后续平行节点中搜索，返回列表类型，同.find_all()参数|
|<>.find_next_sibling() |在后续平行节点中返回一个结果，同.find()参数|
|<>.find_previous_siblings() |在前序平行节点中搜索，返回列表类型，同.find_all()参数|
|<>.find_previous_sibling() |在前序平行节点中返回一个结果，同.find()参数|