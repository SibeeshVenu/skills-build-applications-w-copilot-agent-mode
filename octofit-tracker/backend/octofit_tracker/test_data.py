# Test data for populating the octofit_db database

from datetime import timedelta

test_users = [
    {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
    {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]

test_teams = [
    {"name": "Blue Team"},
    {"name": "Gold Team"},
]

test_activities = [
    {"username": "thundergod", "activity_type": "Cycling", "duration": timedelta(hours=1)},
    {"username": "metalgeek", "activity_type": "Crossfit", "duration": timedelta(hours=2)},
    {"username": "zerocool", "activity_type": "Running", "duration": timedelta(hours=1, minutes=30)},
    {"username": "crashoverride", "activity_type": "Strength", "duration": timedelta(minutes=30)},
    {"username": "sleeptoken", "activity_type": "Swimming", "duration": timedelta(hours=1, minutes=15)},
]

test_leaderboard = [
    {"username": "thundergod", "score": 100},
    {"username": "metalgeek", "score": 90},
    {"username": "zerocool", "score": 95},
    {"username": "crashoverride", "score": 85},
    {"username": "sleeptoken", "score": 80},
]

test_workouts = [
    {"name": "Cycling Training", "description": "Training for a road cycling event"},
    {"name": "Crossfit", "description": "Training for a crossfit competition"},
    {"name": "Running Training", "description": "Training for a marathon"},
    {"name": "Strength Training", "description": "Training for strength"},
    {"name": "Swimming Training", "description": "Training for a swimming competition"},
]
