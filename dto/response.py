class ResultEntity:
    def __init__(self, data='', result=None):
        self.data = data
        if result is not None:
            self.message = result.message
            self.code = result.code
        else:
            self.message = 'success'
            self.code = '10000'

    def to_dict(self):
        return {
            'code': self.code,
            'message': self.message,
            'data': self.data
        }
