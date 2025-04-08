from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        print('populate_db command loaded')
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = []
        for user_data in test_users:
            user = User(username=user_data['username'], email=user_data['email'], password=user_data['password'])
            user.save()
            users.append(user)

        # Create teams
        for team_data in test_teams:
            team = Team(name=team_data['name'])
            team.save()

        # Create activities
        for activity_data in test_activities:
            user = User.objects.get(username=activity_data['username'])
            activity = Activity(user=user, activity_type=activity_data['activity_type'], duration=activity_data['duration'])
            activity.save()

        # Create leaderboard entries
        for leaderboard_data in test_leaderboard:
            user = User.objects.get(username=leaderboard_data['username'])
            leaderboard = Leaderboard(user=user, score=leaderboard_data['score'])
            leaderboard.save()

        # Create workouts
        for workout_data in test_workouts:
            workout = Workout(name=workout_data['name'], description=workout_data['description'])
            workout.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
