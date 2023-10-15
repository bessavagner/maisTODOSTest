# maisTODOSTest
Python test to maisTODOS


## Stack utilizada

**Back-end:** Python, Flask

**Database** Postgres

**Docker** Dockerfile, docker-compose

## Requisitos

- Python (versão 3.8)
- pip
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-RESTful
- Flask-JWT-Extended
- Outras dependências (verifique o arquivo `requirements.txt`)
- Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina. Você pode baixá-los em [Docker](https://www.docker.com/get-started). (Opcional)

## Instalação

1. Clone este repositório para o seu ambiente de desenvolvimento.

```shell
git clone https://github.com/Luansantosdevpy/maisTODOSTest.git
```

2. Navegue até o diretório do projeto.
```shell
cd maisTODOSTest
```

3. Crie um ambiente virtual (recomendado).
```shell
python -m venv venv
```

4. Ative o ambiente virtual.

  - No Windows:
```shell
venv\Scripts\activate
```


  - No macOS e Linux:
```shell
source venv/bin/activate
```

5. Instale as dependências do projeto.
```shell
pip install -r requirements.txt
```

6. Execute as migrações do banco de dados.
```shell
flask db init
flask db migrate
flask db upgrade
```

7. Inicie o aplicativo.
```shell
flask run
```

## Via Docker

1. Crie um arquivo .env na raiz do projeto para configurar as variáveis de ambiente necessárias, como no env.sample.
```shell
cp .env.sample .env
```

2. Inicie os contêineres:
```shell
docker-compose up
```
Isso iniciará o aplicativo Flask e o banco de dados PostgreSQL em contêineres separados.

3. Acesse o aplicativo em seu cliente REST em http://localhost:5000. (Collection do Insomnia [aqui](/collection/todos.json))

## Uso
Registre-se ou faça login para começar a usar o sistema.
É necessário usar o token fornecido no login, para poder criar um cartão de crédito.
Crie, edite, exclua e visualize cartões de crédito.



## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env
Esteja a vontade para criar os valores de acordo com o que preferir

`DB_POSTGRES_USER`

`DB_POSTGRES_PASSWORD`

`DB_POSTGRES_HOST`

`DB_POSTGRES_PORT`

`DB_POSTGRES_NAME`

`DATABASE_URL=postgresql://user:password@host/name`
## Documentação

[Documentação Swagger](http://localhost:5000/api/docs)


## Demonstração

Insira um gif ou um link de alguma demonstração


## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  coverage run -m unittest tests/unit/path_a_ser_testado
```

Para visualizar o retorno dos testes, rode o segunte comando

```bash
  coverage report
```


## Aprendizados

Consegui extrair bastante conhecimento acerca de autenticação e autorização fazendo esse teste.

Também pude ter mais contato diretamente com o Flask, visto que tinha utilizado apenas de forma superficial.


## Melhorias

Poderia, caso o projeto ganhasse uma extensão maior, utilizar arquitetura limpa para ele.

Faria a criação de um front-end.

Melhoraria as validações realizadas nos métodos de cartão de crédito, para ganhar mais segurança nisso.

Faria uma refatoração no retorno do número do cartão, visto que está trazendo todo um hash feito para deixar ele criptografado na base.


## Autores

- [@luansantosdevpy](https://www.github.com/luansantosdevpy)


## 🚀 Sobre mim
Eu sou uma pessoa desenvolvedora back-end.


## Licença

[MIT](https://choosealicense.com/licenses/mit/)

