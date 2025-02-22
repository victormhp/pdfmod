from typing import Optional

import typer

from pdfmod import __app__, __version__

app = typer.Typer(no_args_is_help=True)


def _version_callback(value: bool) -> None:
	if value:
		typer.echo(f"{__app__} v{__version__}")
		raise typer.Exit()


@app.callback()
def main(
	version: Optional[bool] = typer.Option(
		None,
		"--version",
		"-v",
		help="Show the application's version and exit.",
		callback=_version_callback,
		is_eager=True,
	),
) -> None:
	return
