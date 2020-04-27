
class BSONError(Exception):
    """Base class for all BSON exceptions.
    """


class InvalidDocument(BSONError):
    """Raised when trying to create a BSON object from an invalid document.
    """


class InvalidId(BSONError):
    """Raised when trying to create an ObjectId from invalid data.
    """


class MontyError(Exception):
    """Base class for all Montydb exceptions."""


class ConfigurationError(MontyError):
    """Raised when something is incorrectly configured.
    """


class OperationFailure(MontyError):
    """Raised when a database operation fails.
    """

    def __init__(self, error, code=None, details=None):
        self.__code = code
        self.__details = details
        MontyError.__init__(self, error)

    @property
    def code(self):
        return self.__code

    @property
    def details(self):
        return self.__details

    def has_label(self, label):
        if label == "TemporaryTxnFailure":
            # WriteConflict, TransactionAborted, and NoSuchTransaction.
            return self.__code in (112, 244, 251)
        return False


class InvalidOperation(MontyError):
    """Raised when a client attempts to perform an invalid operation."""


class InvalidName(MontyError):
    """Raised when an invalid name is used.
    """


class CollectionInvalid(MontyError):
    """Raised when collection validation fails.
    """


class DocumentTooLarge(InvalidDocument):
    """Raised when an encoded document is too large.
    """


class WriteError(OperationFailure):
    """Base exception type for errors raised during write operations.
    """


class DuplicateKeyError(WriteError):
    """Raised when an insert or update fails due to a duplicate key error."""


class BulkWriteError(OperationFailure):
    """Exception class for bulk write errors.

    .. versionadded:: 2.7
    """

    def __init__(self, results):
        OperationFailure.__init__(
            self, "batch op errors occurred", 65, results)
