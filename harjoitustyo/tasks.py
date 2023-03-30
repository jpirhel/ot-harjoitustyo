from invoke import task

import shutil

pty = False  # must be false on Windows

if shutil.which("python") is not None:
    python_executable = "python"
else:
    python_executable = "python3"


@task
def start(ctx):
    ctx.run(f"{python_executable} run.py", pty=pty)


@task
def pyflakes(ctx):
    ctx.run("pyflakes .", pty=pty)


@task
def test(ctx):
    ctx.run(f"{python_executable} -m pytest harjoitustyo/", pty=pty)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=pty)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=pty)
