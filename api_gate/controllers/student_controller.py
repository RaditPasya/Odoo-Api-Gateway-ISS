from odoo import http
from odoo.http import request, Response
import json

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



class HelloWorldController(http.Controller):

    @http.route('/api/hello_world', type='http', auth='public', methods=['GET'])
    def hello_world(self, **kwargs):
        return "Hello, World!"
    
class HelloWorldHeyController(http.Controller):

    @http.route('/api/hello_world/hey', type='http', auth='public', methods=['GET'])
    def hello_world(self, **kwargs):
        return "Hello, World! hey"


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