# Generated by Django 5.0 on 2023-12-10 17:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("loan_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="loandetails",
            old_name="name",
            new_name="business_name",
        ),
    ]
