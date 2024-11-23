#!/usr/bin/env python
import os
import sys

import django.core.management


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    django.core.management.execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
