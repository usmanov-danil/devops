

# DevOps course 2021 - Pythoon app
![main](https://github.com/usmanov-danil/devops/actions/workflows/docker-image.yml/badge.svg?branch=main)

> This repository stores code for lab 1 of DevOps course in Innopolis University.


This repository consist of flask web app that shows current Moscow time.


## Built With

- Python3
- Flask
- Docker

## Docker part
### Docker Hub image is `usmanovdanil/devops_lab_1`


You can easily build docker image by:
```bash
docker build -t moscow_time_now .
```

Also, you can check your dockerfile with _hadolint_ linter but before it [install](https://github.com/hadolint/hadolint) this tool.
```bash
hadolint <dockerfile>
```

## CI/CD
### Github Actions
Workflow is specified in the [docker-image.yml](.github/workflows/docker-image.yml).

#### Jobs:
* test stage:
Runs unit tests
* build stage:
Builds docker image and push it to the [dockerhub](https://hub.docker.com/repository/docker/usmanovdanil/devops_lab_1)

## Getting Started


### Prerequisites
* Docker 

### Setup
* Clone project
### Build image 
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

### Unit tests
1. Create virtual environment
2. make `pip install -r requierments.txt`
3. Run tests ```pytest tests/```


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
