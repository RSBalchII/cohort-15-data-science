FROM python:3.9-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ARG DEBIAN_FRONTEND=noninteractive

# Set the working directory
WORKDIR /notebooks

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    git \
    build-essential \
    libssl3 \
    libgl1-mesa-glx \
    libqt5gui5 \
    libnotify4 \
    libnss3 \
    xdg-utils \
    x11-apps \
    xvfb \
    libatspi2.0-0 \
    libdrm2 \
    libgbm1 \
    libxcb-dri3-0 \
    libxcb-present0 \
    libxcb-sync1 \
    libxcb-xfixes0 \
    libxcb-xinerama0 \
    libxcb-randr0 \
    libxcb-shape0 \
    libxcb-render-util0 \
    libxcb-cursor0 \
    libxcb-composite0 \
    libxcb-damage0 \
    libxcb-dpms0 \
    libxcb-glx0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-render0 \
    libxcb-res0 \
    libxcb-util1 \
    libxcb-xkb1 \
    libffi-dev \
    pandoc \
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-full \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install wheel
RUN python -m pip install --upgrade pip wheel setuptools

# Copy requirements.txt from python directory
COPY python_reqs/requirements.txt .

# Install JupyterLab and dependencies
RUN pip install -r requirements.txt
# Copy .bash_it directory into the container
COPY .bash_it /root/.bash_it

# Set up bash-it
RUN /bin/bash -c "source /root/.bash_it/bash_it.sh && bash-it install --silent"

# Set the default command to run when starting the container
# Set the default command to run when starting the container
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]
