FROM python:3.9

# Instalação de dependências do sistema (incluindo Firefox e GeckoDriver)
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    tesseract-ocr \
    libxkbcommon-x11-0 \
    libxcb-xinerama0 \
    libgl1-mesa-glx

# Instalação do GeckoDriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz \
    && tar -xvzf geckodriver-v0.30.0-linux64.tar.gz \
    && chmod +x geckodriver \
    && mv geckodriver /usr/local/bin/ \
    && rm geckodriver-v0.30.0-linux64.tar.gz

WORKDIR /app

# Copia todo o código para o container
COPY . .

# Instala as dependências Python (certifique-se de ter um requirements.txt configurado)
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expor porta se a interface ou API necessitar (opcional)
EXPOSE 8080

# Comando de entrada, executa o programa
CMD ["python", "main.py"]