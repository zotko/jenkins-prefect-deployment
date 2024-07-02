FROM prefecthq/prefect:2.19.4-python3.12-conda

# Add environment file to the image
COPY environment.yml .

# Install requirements with conda
RUN conda env create -f environment.yml

# Add our flow code to the image
COPY flows /opt/prefect/flows

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "prefect-env", "/bin/bash", "-c"]

# Activate the environment
ENV PATH /opt/conda/envs/myenv/bin:$PATH

# Run our flow script when the container starts
CMD ["python", "flows/main.py"]