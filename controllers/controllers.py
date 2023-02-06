# -*- coding: utf-8 -*-
# from odoo import http

from odoo import http
import json
from odoo.http import Response


class Gestionfcts_Controller(http.Controller):

    @http.route('/api/gestionfcts', auth='public', method=['GET'], csrf=False)
    def index(self, **kw):
        return "LO HAS CONSEGUIDO. TE FUNCIONA LA API"


    @http.route('/api/gestionfcts/alumnos', auth='public', method=['GET'], csrf=False)
    def get_peliculas(self, **kw):
        try:
            alumnos = http.request.env['gestionfcts.alumno'].sudo().search_read([], ['name'])
            resultado = json.dumps(alumnos, ensure_ascii=False).encode('utf-8')
            return Response(resultado, content_type='application/json;charset=utf-8',
                        status=200)
        except Exception as e:
            resultado = json.dumps({'error': str(e)})
            return Response(resultado, content_type='application/json;charset=utf-8', status=505)

