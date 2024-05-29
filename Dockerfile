# Usa a imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos e instala as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta que a aplicação vai rodar
EXPOSE 5000

# Define o ambiente FLASK_APP
ENV FLASK_APP=app

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
