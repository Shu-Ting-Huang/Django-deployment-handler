#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import urllib.request


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    external_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
    os.environ.setdefault('EXTERNAL_IP', external_ip)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
