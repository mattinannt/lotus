# Generated by Django 4.0.5 on 2022-11-10 23:51

from django.db import migrations


def migrate_jsonfields_to_fk(apps, schema_editor):
    Invoice = apps.get_model("metering_billing", "Invoice")
    Organization = apps.get_model("metering_billing", "Organization")
    Subscription = apps.get_model("metering_billing", "Subscription")
    Customer = apps.get_model("metering_billing", "Customer")

    invoice_org_dict = {}
    invoice_customer_dict = {}
    invoice_sub_dict = {}
    for invoice in Invoice.objects.all():
        try:
            invoice_org = invoice.old_organization["company_name"]
        except:
            invoice_org = None
        try:
            invoice_customer = invoice.old_customer["customer_id"]
        except:
            invoice_customer = None
        try:
            invoice_sub = invoice.old_subscription["subscription_id"]
        except:
            invoice_sub = None

        if invoice_org:
            if invoice_org in invoice_org_dict:
                invoice_org_object = invoice_org_dict[invoice_org]
            else:
                try:
                    invoice_org_object = Organization.objects.get(
                        company_name=invoice_org
                    )
                except Organization.DoesNotExist:
                    invoice_org_object = None
                invoice_org_dict[invoice_org] = invoice_org_object
            invoice.organization = invoice_org_object

        if invoice_customer:
            if invoice_customer in invoice_customer_dict:
                invoice_customer_object = invoice_customer_dict[invoice_customer]
            else:
                try:
                    invoice_customer_object = Customer.objects.get(
                        organization=invoice_org_object, customer_id=invoice_customer
                    )
                except:
                    invoice_customer_object = None
                invoice_customer_dict[invoice_customer] = invoice_customer_object
            invoice.customer = invoice_customer_object

        if invoice_sub:
            if invoice_sub in invoice_sub_dict:
                invoice_sub_object = invoice_sub_dict[invoice_sub]
            else:
                try:
                    invoice_sub_object = Subscription.objects.get(
                        organization=invoice_org_object, subscription_id=invoice_sub
                    )
                except:
                    invoice_sub_object = None
                invoice_sub_dict[invoice_sub] = invoice_sub_object
            invoice.subscription = invoice_sub_object

        invoice.save()


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0069_historicalinvoice_customer_and_more"),
    ]

    operations = [
        migrations.RunPython(migrate_jsonfields_to_fk),
    ]
