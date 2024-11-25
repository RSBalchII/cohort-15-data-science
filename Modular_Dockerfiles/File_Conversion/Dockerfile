FROM jupyter/scipy-notebook:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory
WORKDIR /

# Install conda packages
RUN conda install --quiet --yes \
    -c conda-forge \
    textblob \
    nltk \
    ipykernel \
    plotly \
    beautifulsoup4 \
    pillow \
    sqlalchemy==1.4.46 \
    google-cloud-bigquery \
    google-auth-oauthlib \
    google-auth-httplib2 \
    google-api-python-client \
    keras \
    torchvision \
    torchaudio \
    librosa \
    pydub \
    youtube-dl \
    tqdm \
    ipywidgets \
    widgetsnbextension \
    ipympl \
    xgboost \
    JupyterLab \
    jupyterlab-git \
    dask \
    dask[dataframe] \
    pyarrow==15.0.0 \
    obspy

# Clean up conda cache
RUN conda clean --all -f -y

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools wheel

# Install packages that are not available through conda using pip
RUN pip install --no-cache-dir \
    tensorflow \
    torch \
    opencv-python \
    ffmpeg-python

# Set the default command to run when starting the container
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8889", "--no-browser", "--allow-root"]

