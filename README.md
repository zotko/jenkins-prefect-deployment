# Deploy Prefect Using Jenkins

## Description

This repository provides a template for deploying Prefect flows using Jenkins and Docker. The setup automates the building, pushing, and deploying of Docker images containing Prefect flows, streamlining continuous integration and delivery workflows.

## Usage

1. **Install Cookiecutter**:
    ```bash
    pip install cookiecutter
    ```

2. **Generate the Project Template**:
    ```bash
    cookiecutter https://github.com/zotko/jenkins-prefect-deployment.git
    ```
    Follow the prompts to customize your project:
    - `project_name`: Name of your project.
    - `flow_name`: Name of your Prefect flow.
    - `pool_name`: Name of your Prefect work pool.


## License

This project is licensed under the MIT License.