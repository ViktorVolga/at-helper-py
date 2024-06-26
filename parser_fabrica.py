class ParserFabrica :
    m_parsers = None
    def __init__(self, modem_model):
        if modem_model == 'A7600':
            import A7600_parser as parsers
            self.m_parsers = parsers

    