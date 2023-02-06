from odoo import fields, models
from odoo import api
import re


class alumno(models.Model):
    _name = "gestionfcts.alumno"
    _description = "Alumnos disponibles para prácticas de empresa"

    name = fields.Char("Nombre", required=True)
    last_name = fields.Char("Apellidos", required=True)
    birth_date = fields.Date("Fecha de nacimiento")
    photography = fields.Binary("Foto")
    first_year = fields.Integer("Primer año de estudios", required=True)
    academic_year = fields.Char("Año académico", compute="_value_year", store=True)
    email = fields.Char("Correo electrónico")
    tlf = fields.Char("Teléfono")
    vocational_training = fields.Selection(
        [('0', 'DAM'), ('1', 'DAW'), ('2', 'ASIR'), ('3', 'SMR'), ('4', 'IC'), ('5', 'IO')],
        "Ciclo Formativo", default='0', required=True)
    work_period = fields.Selection([('0', 'Marzo'), ('1', 'Septiembre')], "Periodo de prácticas",
                                   default='0', required=True)
    dual = fields.Selection([('0', 'No'), ('1', 'Sí')], "FP Dual", default='0', required=True)
    erasmus = fields.Selection([('0', 'No'), ('1', 'Sí')], "Erasmus", default='0', required=True)

    empresa_id = fields.Many2one("gestionfcts.empresa", "Empresa", required=True, ondelete="cascade")


@api.depends('first_year', 'academic_year')
def _value_year(self):
    for record in self:
        record.academic_year = "Curso " + str(record.first_year) + "/" + str(record.first_year + 1)


# -*- coding: utf-8# CREACION DE LA CLASE FICHAS ALUMNOS PARA IMPRIMIR TODAS LAS FICHAS DE LOS ALUMNOS# -*-
class Fichas_Alumnos_Report(models.AbstractModel):
    _name = 'report.gestionfcts.report_imprimir_fichas'
    _descripcion = 'modelo abstracto para imprimir todas las fichas de alumnos'


# METODO PARA DEVOLVER TODOS LOS ALUMNOS

def _get_report_values(self, docids=None, data=None):
    docids = self.env["gestionfcts.alumno"].search([]).ids
    docs = self.env['gestionfcts.alumno'].search([])
    print(data)
    return {'doc_ids': docids, 'doc_model': self.env['gestionfcts.alumno'], 'docs': docs, 'data': data, }
