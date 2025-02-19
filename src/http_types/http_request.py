class HttpRequest:
  def __init__(self, body: dict = None, params: dict = None, headers: dict = None) -> None:
    self.body = body
    self.params = params
    self.headers = headers