class DatabaseOperator:
    """The Database Operator is responsible for all
    database controls, basic CRUD operations, and other
    database-related tasks.

    Examples:
    ---------
    > app = Application()
    > database_operator = DatabaseOperator(app)

    Parameters:
    -----------
    - app: Application - An instantiation of the Application object
    """
    def __init__(self, app):
        self._app = app
    
    def app(self):
        return self._app
