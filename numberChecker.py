class numberChecker:
    def check(input):
        try:
            # Convert it into integer
            val = int(input)
            return True
        except ValueError:
            try:
                # Convert it into float
                val = float(input)
                return True
            except ValueError:
                return False