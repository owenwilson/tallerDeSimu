# Taller de simulacion Inventarios

### Requirements

- python 3
- pip install requirements.txt
- docker
- nginx

### docker file

```sh
docker build -t tallerdesimu:latest .
```

```sh
docker run --rm --name simulacioninventarios -p 5000:5000 -d tallerdesimu:latest
```

### docker compose

- **Develompent enviroment**

```sh
docker-compose -f docker-compose.dev.yml up -d
```

- **Producction enviroment**

```sh
docker-compose up -d
```

### Contributions

Created by [owenwilson](https://github.com/owenwilson/tallerDeSimu)
