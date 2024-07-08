from odoo import http
from odoo.http import request, Response
import json
import logging

_logger = logging.getLogger(__name__)



class StudentListController(http.Controller):

    @http.route('/api/student_list', type='http', auth='public', methods=['GET'])
    def student_list(self, **kwargs):
        Student = request.env['op.student']
        students = Student.search([])
        student_data = []
        for student in students:
            student_data.append({
                'name ': student.first_name + student.middle_name + student.last_name
            })
        return Response(json.dumps(student_data), content_type='application/json')


    @http.route('/api/student_create', type='json', auth='user', methods=['POST'])
    def create_student(self, **post):
        try:
            required_fields = ['first_name', 'last_name', 'gender', 'birth_date', 'birth_place', 'nis', 'nisn', 'mobile', 'email']
            missing_fields = [field for field in required_fields if field not in post]
            if missing_fields:
                return {
                    'status': 'error',
                    'message': 'Missing required fields',
                    'missing_fields': missing_fields
                }

            # Log the received data
            _logger.info("Received data: %s", json.dumps(post))
            
            # Combine first_name and last_name to create name
            name = post['first_name'] + ' ' + post['last_name']
            

            Student = request.env['op.student']
            new_student = Student.create({
                'first_name': post['first_name'],
                'last_name': post['last_name'],
                'gender': post['gender'],
                'birth_date': post['birth_date'],
                'birth_place': post['birth_place'],
                'nis': post['nis'],
                'nisn': post['nisn'],
                'mobile': post['mobile'],
                'email': post['email'],
                'name' : name
            })
            
            # Log the created student data
            _logger.info("Created student: %s", new_student)

            # Call the method to create the user for the new student
            new_student.create_student_user()
            
            return {
                'status': 'success',
                'message': 'Student created successfully',
                'student_id': new_student.id
            }
        except Exception as e:
            _logger.error("Error while creating student: %s", str(e))
            return {
                'status': 'error',
                'message': 'An error occurred',
                'error': str(e)
            }

class StudentCountController(http.Controller):

    @http.route('/api/student_count', type='http', auth='public', methods=['GET'])
    def student_count(self, **kwargs):
        Student = request.env['op.student']
        count = Student.search_count([])
        return f"Total number of students: {count}"
    
class StudentPrestasiListController(http.Controller):

    @http.route('/api/student_prestasi_list', type='http', auth='public', methods=['GET'])
    def student_prestasi_list(self, **kwargs):
        StudentPrestasi = request.env['op.student.prestasi']
        prestasis = StudentPrestasi.search([])
        prestasi_data = []
        for prestasi in prestasis:
            prestasi_data.append({
                'nama': prestasi.nama
            })
        return Response(json.dumps(prestasi_data), content_type='application/json')
    
    
class StudentController(http.Controller):

    @http.route('/api/get_students', type='json', auth='user', methods=['GET'])
    def get_students(self):
        students = request.env['op.student'].search([])
        students_data = []
        
        for student in students:
            students_data.append({
                'first_name': student.first_name,
                'middle_name': student.middle_name,
                'last_name': student.last_name,
                'grade': student.grade.name if student.grade else '',
                'rombel': student.rombel.name if student.rombel else '',
                'birth_date': student.birth_date,
                'age': student.age,
                'birth_place': student.birth_place,
                'nis': student.nis,
                'nisn': student.nisn,
                'blood_group': student.blood_group,
                'gender': student.gender,
                'nationality': student.nationality.name if student.nationality else '',
                'emergency_contact': student.emergency_contact.name if student.emergency_contact else '',
                'visa_info': student.visa_info,
                'id_number': student.id_number,
                'user_id': student.user_id.name if student.user_id else '',
                'gr_no': student.gr_no,
                'category_id': student.category_id.name if student.category_id else '',
                'active': student.active,
                'ayah_id': student.ayah_id.name if student.ayah_id else '',
                'ibu_id': student.ibu_id.name if student.ibu_id else '',
                'wali_id': student.wali_id.name if student.wali_id else '',
                'barcode': student.barcode,
                'nama_panggilan': student.nama_panggilan,
                'no_kk': student.no_kk,
                'nik': student.nik,
                'no_akta_lahir': student.no_akta_lahir,
                'agama': student.agama,
                'kewarganegaraan': student.kewarganegaraan,
                'rt_rw': student.rt_rw,
                'kecamatan_id': student.kecamatan_id.name if student.kecamatan_id else '',
                'kelurahan_id': student.kelurahan_id.name if student.kelurahan_id else '',
                'kode_pos': student.kode_pos,
                'tempat_tinggal': student.tempat_tinggal,
                'moda_transport': student.moda_transport,
                'anak_ke': student.anak_ke,
                'punya_kia': student.punya_kia,
                'tinggi_bdn': student.tinggi_bdn,
                'berat_bdn': student.berat_bdn,
                'lingkar_kpl': student.lingkar_kpl,
                'jrk_tmpt_plhn': student.jrk_tmpt_plhn,
                'jrk_tmpt_km': student.jrk_tmpt_km,
                'waktu_tempuh': student.waktu_tempuh,
                'jmlh_saudara_kandung': student.jmlh_saudara_kandung,
                'graduate': student.graduate,
                'status_graduasi': student.status_graduasi,
            })
        
        return json.dumps({'students': students_data})