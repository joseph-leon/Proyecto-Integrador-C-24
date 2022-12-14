from django.db import models

class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    usuario_nombre = models.CharField(max_length=20, verbose_name="Nombre Usuario")
    usuario_correo = models.EmailField(max_length=40, verbose_name="Correo Usuario")
    usuario_clave = models.CharField(max_length=40, verbose_name="Clave Usuario")

    def __str__(self):
        return self.usuario_nombre

#titulo del proyecto no_uv en home
class Titulo(models.Model):
    titulo_id = models.AutoField(primary_key=True)
    titulo_proyecto = models.CharField(max_length=10, verbose_name="Titulo Proyecto")

    def __str__(self):
        return self.titulo_proyecto

class Eslogan(models.Model):
    eslogan_id = models.AutoField(primary_key=True)
    eslogan_proyecto = models.CharField(max_length=100, verbose_name="Eslogan Proyecto")

    def __str__(self):
        return self.eslogan_proyecto

class Parrafoobjetivos(models.Model):
    parrafoobjetivos_id = models.AutoField(primary_key=True)
    parrafoobjetivos_contenido = models.CharField(max_length=255, verbose_name="Parrafo Objetivos")

    def __str__(self):
        return self.parrafoobjetivos_contenido

class Subobjetivo1(models.Model):
    subobjetivo1_id = models.AutoField(primary_key=True)
    subobjetivo1_contenido = models.CharField(max_length=255, verbose_name="Sub Objetivo 1")

    def __str__(self):
        return self.subobjetivo1_contenido

class Subobjetivo2(models.Model):
    subobjetivo2_id = models.AutoField(primary_key=True)
    subobjetivo2_contenido = models.CharField(max_length=255, verbose_name="Sub Objetivo 2")

    def __str__(self):
        return self.subobjetivo2_contenido

class Tec1(models.Model):
    tec1_id = models.AutoField(primary_key=True)
    tec1_contenido = models.CharField(max_length=255, verbose_name="Tecnologia 1")

    def __str__(self):
        return self.tec1_contenido

class Tec2(models.Model):
    tec2_id = models.AutoField(primary_key=True)
    tec2_contenido = models.CharField(max_length=255, verbose_name="Tecnologia 2")

    def __str__(self):
        return self.tec2_contenido

class Tec3(models.Model):
    tec3_id = models.AutoField(primary_key=True)
    tec3_contenido = models.CharField(max_length=255, verbose_name="Tecnologia 3")

    def __str__(self):
        return self.tec3_contenido

class Tec4(models.Model):
    tec4_id = models.AutoField(primary_key=True)
    tec4_contenido = models.CharField(max_length=255, verbose_name="Tecnologia 4")

    def __str__(self):
        return self.tec4_contenido

class Contacto(models.Model):
    contacto_id = models.AutoField(primary_key=True)
    contacto_nombres = models.CharField(max_length=20, verbose_name="Nombres Contacto")
    contacto_correo = models.EmailField(max_length=40, verbose_name="Correo Contacto")
    contacto_tema = models.CharField(max_length=100, verbose_name="Tema Contacto")
    contacto_mensaje = models.CharField(max_length=255, verbose_name="Mensaje Contacto")

    def __str__(self):
        return self.contacto_nombres