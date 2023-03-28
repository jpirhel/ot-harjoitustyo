from invoke import task

import shutil

if shutil.which("python") is not None:
    python_executable = "python"
else:   
    python_executable = "python3"
    
@task
def start(ctx):
    ctx.run(f"{python_executable} run.py", pty=False)

@task
def pyflakes(ctx):
    ctx.run("pyflakes .", pty=False)
