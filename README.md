# Gerenciador de Recursos

Projeto para simular um gerenciador de recursos.

## Tech
 - Django
 - PostgresSQL
 - Docker

## Features

- Usuarios comuns e Usuarios Administrador
- CRUD dos recursos
- Alocação dos recursos por usuario para um certo Periodo

## Installation

Projeto está utilizando Docker, para iniciar siga os passos abaixos.

Realize o git clone

```sh
git clone https://github.com/MauroTony/Gerenciador-de-Recursos.git
```
Realizando o Build do docker
```sh
cd .\Gerenciador-de-Recursos\
docker-compose build 
```
Iniciando o Docker
```sh
docker-compose up -d
```
Realizando as migration
```sh
docker-compose exec web python manage.py migrate --noinput 
```
Criando usuario administrador com username "admin"
```sh
docker-compose exec web python manage.py createsuperuser --username=admin
```
Neste ponto a aplicação já deve estar rodando, acesse http://127.0.0.1:8000.

Se após acessar o link acima a pagina retornar conforme o print abaixo, então está funcionando e pode seguir para a documentação para consumir os endpoints:
![image](https://user-images.githubusercontent.com/57079165/187264038-d398b264-7433-4d92-a217-ca19863467dd.png)



Desligando Servidor
```sh
docker-compose down
```



Documentação da API do projeto encontra-se no link abaixo:
https://documenter.getpostman.com/view/19154738/VUxLvoAX#46442eb8-74a3-4488-b4ab-ec236bc19deb

Collection do Postman para teste das requisões:
[Mesha.postman_collection.zip](https://github.com/MauroTony/Gerenciador-de-Recursos/files/9446541/Mesha.postman_collection.zip)
