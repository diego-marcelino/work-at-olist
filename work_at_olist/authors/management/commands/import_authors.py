from datetime import datetime

from django.core.management.base import BaseCommand

from work_at_olist.authors.models import Author


class Command(BaseCommand):
    """Comand for handle authors csv file."""

    def add_arguments(self, parser):
        """Add arguments for command."""
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        """Handle command call."""
        file_path = options.get('file_path', '')
        try:
            start_time = datetime.now()
            self._handle_authors_file(file_path)
            elapsed = datetime.now() - start_time
            self.stdout.write('Time spent: ' + str(elapsed))
        except FileNotFoundError:
            message = self.style.ERROR('Invalid file path')
            self.stdout.write(message)

    def _handle_authors_file(self, file_path):
        """Handle authors csv file."""
        with open(file_path) as authors_file:
            next(authors_file)  # discard header line
            while author := authors_file.readline():
                self._create_author(author.strip())

    def _create_author(self, author_name):
        """Create author instance."""
        author = Author.objects.create(name=author_name)
        author.save()
