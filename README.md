# Taller de simulacion Inventarios

### Requirements

- python 3
- pip install requirements.txt
- docker
- nginx

```sh
docker build -t tallerdesimu:latest .
```

```sh
docker run --rm --name simulacioninventarios -p 5000:5000 -d tallerdesimu:latest
```

### Contributions

Created by [owenwilson](https://github.com/owenwilson/tallerDeSimu)
