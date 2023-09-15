#Crea el número de estudiantes que tiene más de 30 años

SELECT COUNT(*) AS NumeroDeEstudiantesMayoresDe30
FROM estudiantes
WHERE edad > 30;

#Extrae los estudiantes, que su color preferido no es el amarillo.

SELECT *
FROM estudiantes
WHERE color_preferido <> 'amarillo';

#Extrae los estudiantes,que tienen la edad comprendida entre 50 y 60 años.

SELECT *
FROM estudiantes
WHERE edad BETWEEN 50 AND 60;

#Elimina la tabla estudiantes

DROP TABLE estudiantes;

#Extrae los estudiantes,que no son del 2020-01-10

SELECT *
FROM estudiantes
WHERE fecha_registro <> '2020-01-10';


