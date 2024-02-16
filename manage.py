"""Django's command-line utility for administrative tasks."""

import os

import sys

import os
import sys
from django.core.management import execute_from_command_line

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_config.settings')
    sys.path.append('/home/ubuntu/ccs-kaist/')
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

