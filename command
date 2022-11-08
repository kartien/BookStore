ver tablas 
\l 
salir 
\q 
entrar en la base 
psql  psql -U kartien -d library
ver datos de base 
\d
consultas
select * from auth_user;

Relaciones 
cuando de es de uno a uno OneToOneField requiere on_delete = models.CASCADE
cuandode es es uno a muchos es ForeignKey requiere on_delete = models.CASCADE
cuando es de nuchos a muchos es ManyToManyField no requiere on_delete = models.CASCADE