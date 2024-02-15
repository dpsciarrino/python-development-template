from data.database_operator import DatabaseOperator

class Application:
    """Application Class is to be utilized as the central class structure for
    the application being built.

    This class can be used as the "Controller" in an MVC framework.
    """
    def __init__(self):
        _db_operator: DatabaseOperator = DatabaseOperator(self)
        ...
    
    def db_operator(self):
        return self._db_operator

