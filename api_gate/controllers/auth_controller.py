from odoo import http
from odoo.http import request, Response
import json

class AuthController(http.Controller):
    @http.route('/web/session/authenticationtype', type='json', auth="none")
    def authenticate(self, db, login, password, base_location=None):
        request.session.authenticate(db, login, password)
        user = request.env.user
        if user:
            result = request.env['ir.http'].session_info()
            result['tipe_user'] = user.tipe_user
            return result
        return False