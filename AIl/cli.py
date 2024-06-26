import typer
import uvicorn

from .app import app
from .config import settings

cli = typer.Typer(name="AIl API")


@cli.command()
def run(
    port: int = settings.server.port,
    host: str = settings.server.host,
    log_level: str = settings.server.log_level,
    reload: bool = settings.server.reload,
):  # pragma: no cover
    """Run the API server."""
    uvicorn.run(
        "AIl.app:app",
        host=host,
        port=port,
        log_level=log_level,
        reload=reload,
    )


@cli.command()
def shell():  # pragma: no cover
    """Opens an interactive shell with objects auto imported"""
    _vars = {
        "app": app,
        "settings": settings,
    }
    typer.echo(f"Auto imports: {list(_vars.keys())}")
    try:
        from IPython import start_ipython

        start_ipython(argv=[], user_ns=_vars)
    except ImportError:
        import code

        code.InteractiveConsole(_vars).interact()
