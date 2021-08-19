

# DevOps course 2021 - lab 1

> This repository stores code for lab 1 of DevOps course in Innopolis University.


## Built With

- Python3
- Flask
- Docker

## Docker part

You can easily build docker image by:
```bash
docker build -t moscow_time_now .
```

Also, you can check your dockerfile with _hadolint_ linter but before it [install](https://github.com/hadolint/hadolint) this tool.
```bash
hadolint <dockerfile>
```


## Getting Started


### Prerequisites
* Docker 

### Setup
* Clone project
# Build image 
```bash
docker build -t moscow_time_now .
```

You also may specify argumetns to the image:
```bash
docker build --build-arg DEBUG=${True/False} -t moscow_time_now .
```
`DEBUG` by default is `True`

 ### Run container 
 ```bash
 docker run --rm -it -p 5000:5000 moscow_time_now
 ```

### Usage
Open `http://localhost:5000/` if you did not provide custom port

### Tests
To run tests locally:
```bash
pytest tests/
```



## Authors

👤 **Danil Usmanov**

- GitHub: [@usmanov-danil](https://github.com/usmanov-danil)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- Innopolis University
- B18-SB-01 group 
- Colonel Sanders

## 📝 License

This project is [MIT](./MIT.md) licensed.