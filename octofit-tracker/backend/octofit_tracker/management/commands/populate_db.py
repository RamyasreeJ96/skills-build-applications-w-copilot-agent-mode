from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel')
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team='Marvel')
        batman = User.objects.create(name='Batman', email='batman@dc.com', team='DC')
        superman = User.objects.create(name='Superman', email='superman@dc.com', team='DC')

        # Create activities
        Activity.objects.create(user='Iron Man', type='Running', duration=30, date='2026-02-23')
        Activity.objects.create(user='Batman', type='Cycling', duration=45, date='2026-02-23')

        # Create workouts
        Workout.objects.create(name='Chest workout', description='Chest routine for Iron Man', difficulty='Hard')
        Workout.objects.create(name='Leg workout', description='Leg routine for Superman', difficulty='Medium')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
