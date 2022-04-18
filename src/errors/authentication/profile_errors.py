
class ProfileErrors:

    def __init__(self):
        self.errors = {
            'PR_01': ['Profile already exists', 'user']
        }

    def get_error(self, error_code):
        error = self.errors.get(error_code)
        err = {error[1]: [error[0]]}
        return err

    def raise_profile_exists(self):
        return self.get_error('PR_01')
