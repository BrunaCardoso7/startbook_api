# StartBooks Library API

API para gerenciar livros e autores de maneira eficiente. Permite o cadastro, listagem, atualização e exclusão de livros e autores.

## 🌍 Url de deploy
🔗 https://startbookslibrary.vercel.app/

## 📜 Rotas da API

### **Autor**
- **GET `/author/`**: Retorna a lista de autores cadastrados.
- **POST `/author/`**: Cria um novo autor.
- **PUT `/author/<uuid:pk>/`**: Atualiza um autores pelo ID.
- **PATCH `/author/<uuid:pk>/`**: Atualiza parcialmente um autores pelo ID.
- **DELETE `/author/<uuid:pk>/`**: Deleta um autores pelo ID.
- 
### **Livro**
- **GET `/book/`**: Retorna a lista de livros cadastrados.
- **POST `/book/`**: Cria um novo livro.
- **GET `/book/<uuid:pk>/`**: Retorna um livro específico pelo ID.
- **PUT `/book/<uuid:pk>/`**: Atualiza um livro pelo ID.
- **PATCH `/book/<uuid:pk>/`**: Atualiza parcialmente um livro pelo ID.
- **DELETE `/book/<uuid:pk>/`**: Deleta um livro pelo ID.

### **Ranking de Autores**
- **GET `/ranking/`**: Retorna os 5 autores com mais de 5 livros publicados.

### **WebSocket**
- **`wss://startbook-api.onrender.com/ws/notifications/`**: Conecta-se ao WebSocket para receber notificações em tempo real sempre que um novo autor for criado.

## 🚀 Tecnologias Utilizadas
- Django
- Django REST Framework
- Sqlite
- channels

## Descrição
Instruções para configurar o ambiente de desenvolvimento da api e executar o projeto em seu sistema.
## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- **Python 3.x**: 
- **pip**:
  **Docker**.
- **Docker Compose**.

## Passos para Executar o Projeto

### 1. Clonar o Repositório

Primeiro, clone o repositório para o seu computador. Abra o terminal e execute o seguinte comando:

```bash
git clone https://github.com/BrunaCardoso7/startbook_api.git
```


### 2. Acessar o Diretório do Projeto

Após clonar o repositório, entre no diretório do projeto:

```bash
cd startbook_api
```



### 3. Construa e Suba os Contêineres com o Docker Compose
  
```bash
docker compose up --build

```




