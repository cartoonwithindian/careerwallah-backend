from fastapi import HTTPException, status


class AppError(Exception):
    def __init__(self, message: str, code: str = "INTERNAL_ERROR", details: list | None = None):
        self.message = message
        self.code = code
        self.details = details or []
        super().__init__(self.message)


class NotFoundError(AppError):
    def __init__(self, message: str = "Not found"):
        super().__init__(message, code="NOT_FOUND")


class ValidationError(AppError):
    def __init__(self, message: str = "Validation error", details: list | None = None):
        super().__init__(message, code="VALIDATION_ERROR", details=details)


class ConflictError(AppError):
    def __init__(self, message: str = "Conflict"):
        super().__init__(message, code="CONFLICT")


class ForbiddenError(AppError):
    def __init__(self, message: str = "Forbidden"):
        super().__init__(message, code="FORBIDDEN")


class UnauthorizedError(AppError):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, code="UNAUTHORIZED")
