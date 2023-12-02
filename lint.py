import asyncio
from pathlib import Path


async def lint_file(file: str):
    """
    Runs isort and black on a python file.
    """
    await asyncio.create_subprocess_shell(f"python -m isort {file} --profile black")
    await asyncio.create_subprocess_shell(f"black {file}")
    print(f"Linted {file}")


async def lint_python_files():
    """
    Looks through the subdirectories of this file's cwd and runs isort and black on them.
    """
    subdirs = [dir for dir in Path.cwd().iterdir() if dir.is_dir()]
    files = set()
    for subdir in subdirs:
        files.update(
            [str(file.resolve()) for file in subdir.iterdir() if file.suffix == ".py"]
        )
    await asyncio.gather(*[asyncio.create_task(lint_file(file)) for file in files])


if __name__ == "__main__":
    asyncio.run(lint_python_files())
