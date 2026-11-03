# Utiliza a imagem oficial leve do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala dependências essenciais do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instala o Django via pip
RUN pip install --no-cache-dir django

# Copia todo o código do projeto para dentro do container
COPY . /app/

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando para iniciar o servidor web dentro do container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]