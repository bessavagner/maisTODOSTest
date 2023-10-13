# maisTODOSTest
Python test to maisTODOS

## Requisitos

- Python (versão 3.8)
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-RESTful
- Flask-JWT-Extended
- Outras dependências (verifique o arquivo `requirements.txt`)
- Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina. Você pode baixá-los em [Docker](https://www.docker.com/get-started).

## Instalação

1. Clone este repositório para o seu ambiente de desenvolvimento.

```shell
git clone https://github.com/Luansantosdevpy/maisTODOSTest.git

2. Navegue até o diretório do projeto.
cd maisTODOSTest

3. Crie um ambiente virtual (recomendado).
python -m venv venv

4. Ative o ambiente virtual.
  - No Windows:
venv\Scripts\activate

  - No macOS e Linux:
source venv/bin/activate

5. Instale as dependências do projeto.
pip install -r requirements.txt

6. Execute as migrações do banco de dados.
flask db init
flask db migrate
flask db upgrade

7. Inicie o aplicativo.
flask run

## Via Docker

1. Crie um arquivo .env na raiz do projeto para configurar as variáveis de ambiente necessárias,como no env.sample.

2. Inicie os contêineres:
docker-compose up
Isso iniciará o aplicativo Flask e o banco de dados PostgreSQL em contêineres separados.

3. Acesse o aplicativo em seu navegador em http://localhost:5000.

## Uso
Registre-se ou faça login para começar a usar o sistema.
Crie, edite, exclua e visualize cartões de crédito.

Por Luan Santos


