FROM python:3.9-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    tesseract-ocr \
    tesseract-ocr-por \
    && rm -rf /var/lib/apt/lists/*

# Copiar requisitos e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fonte
COPY . .

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:99

# Definir label para identificação
LABEL automation_type=conferencia

CMD ["python", "-m", "modules.containers.conferencia_container"]
