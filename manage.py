import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Не вдалося імпортувати Django. Переконайтесь, що Django встановлено і доступно у вашому середовищі."
        )

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
