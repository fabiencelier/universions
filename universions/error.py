"""Module containing all the errors of the package."""

from typing import Optional


class InvalidVersionFormatError(ValueError):
    """Error thrown when the format is invalid."""

    def __init__(
        self,
        version: str,
        message: Optional[str] = None,
        caused_by: Optional[Exception] = None,
    ):
        """Constructor.

        Args:
            version: The invalid version string.
            message: A explicit reason why the version is invalid.
            caused_by: Underlying error thrown.

        """
        full_message = f"Invalid version {version}."
        if message:
            full_message += "\n" + message
        if caused_by is not None:
            super().__init__(full_message, caused_by)
        else:
            super().__init__(full_message)
