import odoo.tests


@odoo.tests.common.at_install(True)
@odoo.tests.common.post_install(True)
class TestUi(odoo.tests.HttpCase):

    def test_01_check_timer(self):
        self.phantom_js("/", "odoo.__DEBUG__.services['web.Tour'].run('project_timelog', 'test')", "odoo.__DEBUG__.services['web.Tour'].tours.project_timelog", login="admin")
