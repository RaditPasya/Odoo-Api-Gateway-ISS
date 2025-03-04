from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError
import json



class OpAssignmentAPI(http.Controller):

    @http.route('/api/op_assignment', type='json', auth='user')
    def get_op_assignments(self):
        try:
            # Get the current user
            current_user = request.env.user
            
            # Search for the student record using the current user's name
            student = request.env['op.student'].sudo().search([('name', '=', current_user.name)], limit=1)
            
            # If a student record with the current user's name is found, return access denied
            if student:
                return {'success': False, 'message': 'Access Denied'}

            # Fetch all assignments if no student with the current user's name exists
            assignments = request.env['op.assignment'].sudo().search([])
            data = []
            for assignment in assignments:
                data.append({
                    'name': assignment.grading_assignment_id.name,
                    'issued_date': assignment.grading_assignment_id.issued_date,
                })
                
            return {'success': True, 'data': data}
        except AccessError:
            return {'success': False, 'message': 'Access Denied'}
        except Exception as e:
            return {'success': False, 'message': str(e)}
        
    @http.route('/api/op_assignment/user', type='json', auth='user')
    def get_user_assignments(self):
        try:
            current_user = request.env.user
            student = request.env['op.student'].sudo().search([('partner_id', '=', current_user.partner_id.id)], limit=1)
            if not student:
                return {'success': False, 'message': 'User is not associated with any student record'}

            assignments = request.env['op.assignment'].sudo().search([('allocation_ids', 'in', [student.id])])
            
            data = []
            for assignment in assignments:
                data.append({
                    'name': assignment.grading_assignment_id.name,
                    'issued_date': assignment.grading_assignment_id.issued_date,
                })

            return {'success': True, 'data': data}
        except AccessError:
            return {'success': False, 'message': 'Access Denied'}
        except Exception as e:
            return {'success': False, 'message': str(e)}
