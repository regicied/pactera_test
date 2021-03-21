# WeatherGetter api 文档


### API test

- 使用说明: 此api用于检测backend状态

- url: `{host}:{port}/test`

- authentication: False

#### method: get

- parameter: `{host}:{port}/test`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |



- request body: 
```json5
{}
```

- response: 
```json5
{
    "status": true,
}
```


### API weather

- 使用说明: 此api用于获取指定城市的天气情况

- url: `{host}:{port}/weather/{city}`

- authentication: False

#### method: get

- parameter: `{host}:{port}/weather/{city}`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
| city | False |  True| 指定城市的英文名称|


- request body: 
```json5
{}
```

- response: 
```json5
{
  "temperature": 9.8,
  "weather": "Dry/Dawn",
  "wind": 4.3,
  "timestamp": "21-3-2021 07:29:15",
  "city": "Sydney"
}
```
