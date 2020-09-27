# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actors(models.Model):
    actor = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'actors'
        verbose_name = 'actor'
        verbose_name_plural = 'actors'


class Countries(models.Model):
    country = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'countries'
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.country


class Directors(models.Model):
    director = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'directors'
        verbose_name = 'director'
        verbose_name_plural = 'directors'


class Films(models.Model):
    name = models.CharField(max_length=80)
    time = models.CharField(max_length=20, blank=True, null=True)
    kinopoisk_id = models.CharField(max_length=30, blank=True, null=True)
    kinopoisk = models.FloatField(blank=True, null=True)
    imdb = models.FloatField(blank=True, null=True)
    id_years = models.ForeignKey('Years', models.DO_NOTHING, db_column='id_years', blank=True, null=True)
    id_genres = models.ForeignKey('Genres', models.DO_NOTHING, db_column='id_genres', blank=True, null=True)
    id_types = models.ForeignKey('Types', models.DO_NOTHING, db_column='id_types', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'films'
        verbose_name = 'film'
        verbose_name_plural = 'films'


class FilmsActors(models.Model):
    film = models.OneToOneField(Films, models.DO_NOTHING, primary_key=True)
    actor = models.ForeignKey(Actors, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'films_actors'
        unique_together = (('film', 'actor'),)
        verbose_name = 'films_actors'
        verbose_name_plural = 'films_actors'


class FilmsCountries(models.Model):
    film = models.OneToOneField(Films, models.DO_NOTHING, primary_key=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'films_countries'
        unique_together = (('film', 'country'),)
        verbose_name = 'films_countries'
        verbose_name_plural = 'films_countries'


class FilmsDirectors(models.Model):
    film = models.OneToOneField(Films, models.DO_NOTHING, primary_key=True)
    director = models.ForeignKey(Directors, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'films_directors'
        unique_together = (('film', 'director'),)
        verbose_name = 'films_directors'
        verbose_name_plural = 'films_directors'


class Genres(models.Model):
    genre = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'genres'
        verbose_name = 'genre'
        verbose_name_plural = 'genres'


class Types(models.Model):
    type = models.TextField()  # This field type is a guess.
    season = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'
        verbose_name = 'type'
        verbose_name_plural = 'types'


class Years(models.Model):
    year = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'years'
        verbose_name = 'year'
        verbose_name_plural = 'years'
