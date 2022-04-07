class Utils:
    @staticmethod
    def cast_to_type_with_default_value(input_value, cast_type, default_value):
        try:
            return cast_type(input_value)
        except:
            return default_value
