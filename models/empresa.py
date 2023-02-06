from odoo import fields, models

class empresa (models.Model):
    _name = "gestionfcts.empresa"
    _description = "Empresas que ofertan prácticas"

    name = fields.Char("Nombre", required=True)
    contact_employee = fields.Char("Persona de contacto", required=True)
    tlf_contact = fields.Char("Teléfono de contacto")
    email = fields.Char("Correo electrónico")
    address = fields.Char("Dirección")
    city = fields.Char("Localidad")
    dual = fields.Selection([('0', 'No'), ('1', 'Sí')], "FP Dual", default='0', required=True)
    erasmus = fields.Selection([('0', 'No'), ('1', 'Sí')], "Erasmus", default='0', required=True)
    vacancy = fields.Char("Plazas")
    agreement = fields.Selection([('0', 'No'), ('1', 'Sí')], "Convenio", default='0', required=True)
    tasks = fields.Char("Tareas a realizar")
    attachments = fields.Char("Observaciones")

    alumno_id = fields.One2many("gestionfcts.alumno", "empresa_id", "Alumnos")