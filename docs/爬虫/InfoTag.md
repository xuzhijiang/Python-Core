#### 信息标记的3中形式

* XML(Internet上的信息交互与传递)
* JSON (JavsScript Object Notation)移动应用云端和节点的信息通信，无注释
* YAML (YAML Ain’t Markup Language)各类系统的配置文件，有注释易读

#### XML

```xml
<person>
<firstName>Tian</firstName>
<lastName>Song</lastName>
<address>
<streetAddr>中关村南大街5号</streetAddr>
<city>北京市</city>
<zipcode>100081</zipcode>
</address>
<prof>Computer System</prof><prof>Security</prof>
</person>
```

#### JSON

> 有类型key:value

```json
“key” : “value”
“key” : [“value1”, “value2”]
“key” : {“subkey” : “subvalue”}
```

```json
{
“firstName” : “Tian” ,
“lastName” : “Song” ,
“address” : {
“streetAddr” : “中关村南大街5号” ,
“city” : “北京市” ,
“zipcode” : “100081”
} ,
“prof” : [ “Computer System” , “Security” ]
}
```

##### YAML

* 无类型键值对 key:value

* key只能是字符串

###### 缩进表达所属关系

```yaml
name :
    newName : City
    oldName : Town
```

```yaml
firstName : Tian
lastName : Song
address :
streetAddr : 中关村南大街5号
city : 北京市
zipcode : 100081
prof :
‐Computer System
‐Security
```

###### ‐表达并列关系
name :
‐City
‐Big Town

##### |表达整块数据 #表示注释
text: |, #学校介绍

```yaml
key : value
key : #Comment
‐value1
‐value2
key :
	subkey : subvalue
```
