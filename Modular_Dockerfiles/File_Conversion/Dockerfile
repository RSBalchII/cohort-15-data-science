FROM python:3.12-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory
WORKDIR /notebooks

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libreoffice \
    pandoc \
    html2text \
    texlive-xetex \
    texlive-fonts-recommended \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install wheel
RUN python -m pip install --upgrade pip wheel setuptools

# Install Python dependencies
RUN pip install --no-cache-dir \
    pypandoc \
    nbconvert \
    notebook \
    jupyter-sql \
    js2py \
    regex \
    soundfile

# Set the default command to run when starting the container
CMD ["bash"]
