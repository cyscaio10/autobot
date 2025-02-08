# Use uma imagem base do Python
FROM python:3.9-slim

# Instale as dependências do sistema necessárias para o tkinter, opencv e outras bibliotecas
RUN apt-get update && apt-get install -y \
    python3-tk \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Comando para iniciar o programa
CMD ["python", "main.py"]