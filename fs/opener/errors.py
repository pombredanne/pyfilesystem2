# coding: utf-8
"""Errors raised when attempting to open a filesystem.
"""

class ParseError(ValueError):
    """Attempt to parse an invalid FS URL.
    """


class OpenerError(Exception):
    """Base exception for opener related errors.
    """


class UnsupportedProtocol(OpenerError):
    """No opener found for the given protocol.
    """


class EntryPointError(OpenerError):
    """An entry point could not be loaded.
    """


class NotWriteable(OpenerError):
    """A writable FS could not be created.
    """
