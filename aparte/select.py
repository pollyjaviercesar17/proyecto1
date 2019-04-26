#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Selects(object):

    # Selector de nacionalidad.
    def nacionali(self):
        return (
            ('', 'Nacionalidad'),
            ('V', 'V'),
            ('E', 'E'),
        )

    def tipo(self):
    	return(
    		('', 'Tipo de Hogar'),
    		('CASA', 'CASA'),
    		('QUINTA','QUINTA'),
			('APARTAMENTO','APARTAMENTO'),
			('RANCHO','RANCHO'),
			('HABITACION','HABITACION'),
    		)


    def tenencias(self):
    	return(
    		('', 'Tipo de Tenencia'),
    		('PROPIA','PROPIA' ),    
			('ALQUILADA','ALQUILADA'),
			('PRESTADA','PRESTADA'),
			('HEREDADA','HEREDADA'),
			('INVASION','INVASION'),
    		)

    def turno(self):
        return(
            ('', 'Turno'),
            ('DIURNO','DIURNO'),
            ('NOCHE','NOCTURNO'),
            )


    def carrera(self):
        return(
            ('','CARRERA'),
            ('PNF INFORMATICA','PNF INFORMATICA'),
            ('PNF AGROALIMENTARIA','PNF AGROALIMENTARIA'),
            ('PNF ELECTRICA','PNF ELECTRICA'),
            ('PNF MECANICA','PNF MECANICA'),
            ('PNF SEGURIDAD ALIMENTARIA','PNF SEGURIDAD ALIMENTARIA'),
            ('PNF ADMINISTRACION','PNF ADMINISTRACION'),
            )

    def trayecto(self):
        return(
            ('','TRAYECTO'),
            ('I','I'),
            ('II','II'),
            ('III','III'),
            ('IV','IV'),

            )

    def semestre(self):
        return(
            ('','SEMESTRE'),
            ('I','I'),
            ('II','II'),
            ('III','III'),
            ('IV','IV'),
            ('V','V'),
            ('VI','VI'),
            ('VII','VII'),
            ('VIII','VIII'),

            )

    def parentesco(self):
        return(
            ('PADRE', 'PADRE'),
            ('MADRE', 'MADRE'),
            ('HERMANO', 'HERMANO'),
            ('HERMANA', 'HERMANA'),
            ('TIO','TIO'),
            ('TIA','TIA'),
            ('ABUELO','ABUELO'),
            ('ABUELA','ABUELA'),
            ('HIJO','HIJO'),
            ('HIJA','HIJA'),            
            )






