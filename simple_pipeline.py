import kfp
from kfp import dsl

@dsl.component
def generate_text_op() -> str:
    return "Hello, Kubeflow Pipelines!"

@dsl.component
def print_text_op(message: str):
    print(message)

@dsl.pipeline(
    name="Simple Pipeline",
    description="A pipeline to test basic setup"
)
def simple_pipeline():
    message = generate_text_op()
    print_text_op(message=message.output)

if __name__ == "__main__":
    from kfp import compiler

    compiler.Compiler().compile(
        pipeline_func=simple_pipeline,
        package_path="simple_pipeline.yaml"
    )
