from twocaptcha import TwoCaptcha

class CaptchaSolver:

    def __init__(self, captcha):
        # use your api key here from 2captcha
        api_key = ''
        self.solver = TwoCaptcha(api_key)
        self.result = self.solver.normal(captcha)

    def get_captcha(self):
        return self.result['code']

