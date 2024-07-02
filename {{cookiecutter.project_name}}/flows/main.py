import os
from prefect import flow, task

@task
def task1():
    pass

@task
def task2():
    pass

@flow(log_prints=True)
def {{cookiecutter.flow_name}}():
    task1()
    task2()

if __name__ == "__main__":
    {{cookiecutter.flow_name}}()

    # Uncomment the following lines to deploy the flow from Jenkins
    # {{cookiecutter.flow_name}}.deploy(
    #     name="{{cookiecutter.flow_name}}", # Name of the flow 
    #     work_pool_name="{{cookiecutter.pool_name}}", # Name of the pool
    #     image=f"{os.environ["REGISTRY_URL"]}/{os.environ["IMAGE_NAME"]}:{os.environ["IMAGE_TAG"]}",
    #     build=False, # Don't build the image
    #     cron="* * * * *", # Schedule the flow,
    # )
