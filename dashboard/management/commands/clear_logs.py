"""
Django management command to clear log data while preserving user accounts
Usage: python manage.py clear_logs
"""
from django.core.management.base import BaseCommand
from dashboard.models import LogEntry, Anomaly
from authentication.models import AdminUser

class Command(BaseCommand):
    help = 'Clear all LogEntry and Anomaly records while preserving user accounts'

    def add_arguments(self, parser):
        parser.add_argument(
            '--yes',
            action='store_true',
            help='Skip confirmation prompt',
        )

    def handle(self, *args, **options):
        # Count records
        log_count = LogEntry.objects.count()
        anomaly_count = Anomaly.objects.count()
        user_count = AdminUser.objects.count()
        
        self.stdout.write(self.style.WARNING('📊 Current Database Status:'))
        self.stdout.write(f'  - LogEntry records: {log_count}')
        self.stdout.write(f'  - Anomaly records: {anomaly_count}')
        self.stdout.write(f'  - User accounts: {user_count} (will be preserved)')
        self.stdout.write('')
        
        if log_count == 0 and anomaly_count == 0:
            self.stdout.write(self.style.SUCCESS('✅ Database is already clean!'))
            return
        
        # Confirmation
        if not options['yes']:
            self.stdout.write(self.style.WARNING('⚠️  This will DELETE all log and anomaly records!'))
            confirm = input('Are you sure you want to continue? (yes/no): ')
            if confirm.lower() != 'yes':
                self.stdout.write(self.style.ERROR('❌ Operation cancelled'))
                return
        
        # Delete records
        self.stdout.write('🗑️  Deleting records...')
        
        deleted_anomalies = Anomaly.objects.all().delete()[0]
        deleted_logs = LogEntry.objects.all().delete()[0]
        
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('✅ Database cleared successfully!'))
        self.stdout.write(f'  - Deleted {deleted_logs} LogEntry records')
        self.stdout.write(f'  - Deleted {deleted_anomalies} Anomaly records')
        self.stdout.write(f'  - Preserved {user_count} user account(s)')
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('🎯 Ready for fresh demo data!'))
