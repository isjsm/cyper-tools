class WiFiSecurity:
    @staticmethod
    def check_weak_password(password):
        weak_patterns = ["12345678", "admin123", "password"]
        return any(pattern in password.lower() for pattern in weak_patterns)
