# Generated by Django 4.0.5 on 2023-01-08 00:48

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metering_billing', '0139_alter_organizationsetting_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='externalplanlink',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='feature',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='planversion',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='webhookendpoint',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='customerbalanceadjustment',
            name='amount_paid',
            field=models.DecimalField(decimal_places=10, default=Decimal('0'), max_digits=20),
        ),
        migrations.AddField(
            model_name='customerbalanceadjustment',
            name='amount_paid_currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='metering_billing.pricingunit'),
        ),
        migrations.AddConstraint(
            model_name='externalplanlink',
            constraint=models.UniqueConstraint(fields=('organization', 'source', 'external_plan_id'), name='unique_external_plan_link'),
        ),
        migrations.AddConstraint(
            model_name='feature',
            constraint=models.UniqueConstraint(fields=('organization', 'feature_name'), name='unique_feature'),
        ),
        migrations.AddConstraint(
            model_name='planversion',
            constraint=models.UniqueConstraint(fields=('plan', 'version'), name='unique_plan_version'),
        ),
        migrations.AddConstraint(
            model_name='planversion',
            constraint=models.UniqueConstraint(fields=('organization', 'version_id'), name='unique_version_id'),
        ),
        migrations.AddConstraint(
            model_name='webhookendpoint',
            constraint=models.UniqueConstraint(fields=('organization', 'webhook_url'), name='unique_webhook_url'),
        ),
    ]
