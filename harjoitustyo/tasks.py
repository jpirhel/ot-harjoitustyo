from invoke import task

import shutil

pty = False  # must be false on Windows

if shutil.which("python") is not None:
    python_executable = "python"
else:
    python_executable = "python3"


@task
def import_data_from_web(ctx):
    ctx.run(f"{python_executable} run.py --import-data-from-web")


@task
def start(ctx):
    ctx.run(f"{python_executable} run.py", pty=pty)


@task
def pyflakes(ctx):
    ctx.run("pyflakes .", pty=pty)


@task
def pylint(ctx):
    ctx.run("pylint harjoitustyo/", pty=pty)


@task
def autopep8(ctx):
    ctx.run("autopep8 --in-place --recursive harjoitustyo/", pty=pty)


@task(autopep8)
def format(ctx):
    pass


@task(pre=[pyflakes, pylint])
def quality(ctx):
    pass


@task
def test(ctx):
    ctx.run(f"{python_executable} -m pytest harjoitustyo/", pty=pty)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=pty)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=pty)
