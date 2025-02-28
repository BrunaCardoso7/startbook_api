FROM python

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo requirements.txt
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia todo o conteúdo do projeto
COPY . .

# Define o PYTHONPATH para incluir o diretório startbooks
ENV PYTHONPATH=/app/startbooks

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["daphne", "startbooks.asgi:application", "--port", "8000", "--bind", "0.0.0.0"]