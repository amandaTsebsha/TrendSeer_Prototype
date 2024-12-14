#!/usr/bin/env python

import os
import sys
from django.core.management import execute_from_command_line

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trendseer.settings')
    try:
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable?"
            ) from exc
        raise

if __name__ == '__main__':
    main()
