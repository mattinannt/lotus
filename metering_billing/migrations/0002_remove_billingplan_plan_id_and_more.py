# Generated by Django 4.0.5 on 2022-09-02 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="billingplan",
            name="plan_id",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="billing_id",
        ),
        migrations.RemoveField(
            model_name="plancomponent",
            name="billing_plan",
        ),
        migrations.AddField(
            model_name="billingplan",
            name="components",
            field=models.ManyToManyField(to="metering_billing.plancomponent"),
        ),
    ]