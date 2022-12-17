from odoo import api, fields, models, exceptions

class MasterComponent(models.Model):
    _name = "components.master"
    _description = "Master Component"

    name = fields.Char(string='Nama Komponen')
    processing_time = fields.Integer(string='Waktu Pengerjaan Komponen')

class MasterItem(models.Model):
    _name = "items.master"
    _description = "Master Item"

    name = fields.Char(string='Nama Item')
    # components = fields.Many2one('components.master.name',
    #                              'Pemilihan Komponen',
    #                              ondelete='cascade')
    percentage = fields.Float(string='Bobot Presentase Komponen (%)', digits=(4,2))
    starting_time = fields.Integer(string='Tanggal Mulai Pengerjaan')
    # expected_finished_time = starting_time + MasterComponent.processing_time
    real_finished_time = fields.Integer(string='Real Tanggal Selesai')

    @api.constrains('percentage')
    def _check_percent(self):
        print('_check_percent')
        if self.percentage >= 100:
            raise exceptions.ValidationError("Maaf, bobot presentasi harus dalam range 0-100%.")


# class CustomImport(models.Model):
#     _name =





