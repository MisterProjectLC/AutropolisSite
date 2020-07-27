from django.db import models

from django.urls import reverse # Used to generate URLs by reversing the URL patterns


class Game(models.Model):
    turno = models.IntegerField(default=1)
    engenhocas = models.IntegerField(default=0)

    def __str__(self):
        return "Autrópolis " + str(self.id)

    class Meta:
        ordering = ['id']
    

class Super(models.Model):
    nome = models.CharField(max_length=100,)

    TEAMS = (
        ('H', 'Heroico'),
        ('N', 'Neutro'),
        ('V', 'Vilanesco'),
    )

    team = models.CharField(
        max_length=1,
        choices=TEAMS,
    )

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
    


class Local(models.Model):
    nome = models.CharField(max_length=100,)
    especial = models.CharField(max_length=200, default='', blank=True)
    overrider = models.CharField(max_length=200, default='', blank=True)
    heroico = models.CharField(max_length=200, default='Nada')
    neutro = models.CharField(max_length=200,)
    vilanesco = models.CharField(max_length=200,)
    visitors = models.ManyToManyField(Super,blank=True)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)

    TERRITORIOS = (
        ('H', 'Heroico'),
        ('N', 'Neutro'),
        ('V', 'Vilanesco'),
    )

    territorio = models.CharField(
        max_length=1,
        choices=TERRITORIOS,
        blank=True,
        default='N',
    )

    def desastre(self):
        if self.especial != '':
            return self.especial

        if self.overrider != '':
            return self.overrider
        
        if self.territorio == 'H':
            return self.heroico
        elif self.territorio == 'N':
            return self.neutro
        else:
            return self.vilanesco

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.nome
        

     
