# Generated by Django 4.0.6 on 2022-07-27 10:41

from django.db import migrations, models
import django.db.models.deletion


def create_tickers_and_history(apps, schema_editor):
    Ticker = apps.get_model('tickers', 'Ticker')
    TickerHistory = apps.get_model('tickers', 'TickerHistory')
    for i in range(100):
        if i < 10:
            name_index = '0{0}'.format(i)
        else:
            name_index = '{0}'.format(i)
        ticker = Ticker.objects.create(
            name='ticker_{0}'.format(name_index)
        )
        TickerHistory.objects.create(ticker_id=ticker.id, value=0)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='TickerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickers.ticker')),
            ],
        ),
        migrations.RunPython(create_tickers_and_history),
    ]
