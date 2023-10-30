import click

tasks = []

@click.group()
def cli():
    """Simple To-Do List CLI application."""
    pass

@cli.command()
def list_tasks():
    """List all tasks."""
    if not tasks:
        click.echo("No tasks to display.")
    else:
        for i, task in enumerate(tasks, start=1):
            click.echo(f"{i}. {task}")

@cli.command()
@click.argument("task")
def add_task(task):
    """Add a new task."""
    tasks.append(task)
    click.echo(f"Task '{task}' added.")

@cli.command()
@click.argument("task_num", type=int)
def complete_task(task_num):
    """Mark a task as completed."""
    if 1 <= task_num <= len(tasks):
        completed_task = tasks.pop(task_num - 1)
        click.echo(f"Task '{completed_task}' marked as completed.")
    else:
        click.echo("Invalid task number.")

if __name__ == "__main__":
    cli()
