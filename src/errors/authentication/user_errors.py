
class UserErrors:

    def __init__(self):
        self.errors = {
            'AU_01': ['Invalid user email', 'email'],
            'AU_02': ['Invalid login details', 'password'],
            'AU_03': ['Invalid verification code', 'code'],
            'AU_04': ['Verifications code has already expired', 'code'],
            'AU_05': ['Username does not exits', 'username'],
            'AU_06': ['Email not verified', 'email'],
            'AU_07': ['User account is inactive', 'email'],
            "AU_08": ['Verification code already used', 'code'],
            'AU_09': ['Confirm password does not match with the password', 'confirm_password']
        }

    def get_error(self, error_code):
        error = self.errors.get(error_code)
        err = {error[1]: [error[0]]}
        return err

    def raise_invalid_email(self):
        return self.get_error('AU_01')

    def raise_login_failed(self):
        return self.get_error('AU_02')

    def raise_invalid_code(self):
        return self.get_error('AU_03')

    def raise_verification_code_expired(self):
        return self.get_error('AU_04')

    def raise_invalid_username(self):
        return self.get_error('AU_05')

    def raise_email_not_verified(self):
        return self.get_error('AU_06')

    def raise_account_inactive(self):
        return self.get_error('AU_07')

    def raise_code_used(self):
        return self.get_error('AU_08')

    def raise_password_do_not_match(self):
        return self.get_error('AU_09')
