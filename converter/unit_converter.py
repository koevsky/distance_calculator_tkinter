class Converter:


    @staticmethod
    def formula(x, y):
        return x * y

    # METRIC
    @staticmethod
    def from_millimeters(value, unit_type):
        units = {
            'millimeter': 1,
            'centimeter': 0.1,
            'meter': 0.001,
            'kilometer': 0.000001,

            'inch': 0.0393700787,
            'feet': 0.0032808399,
            'yard': 0.0010936133,
            'mile': 0.000000621371192
        }

        return Converter.formula(value, units[unit_type])

    @staticmethod
    def from_centimeters(value, unit_type):
        units = {
            'millimeter': 10,
            'centimeter': 1,
            'meter': 0.01,
            'kilometer': 0.00001,

            'inch': 0.393700787,
            'feet': 0.032808399,
            'yard': 0.010936133,
            'mile': 0.00000621371192
        }

        return Converter.formula(value, units[unit_type])

    @staticmethod
    def from_meters(value, unit_type):
        units = {
            'millimeter': 1_000,
            'centimeter': 100,
            'meter': 1,
            'kilometer': 0.0001,

            'inch': 39.3700787,
            'feet': 3.2808399,
            'yard': 1.0936133,
            'mile': 0.000621371192
        }

        return Converter.formula(value, units[unit_type])

    @staticmethod
    def from_kilometers(value, unit_type):

        units = {
            'millimeter': 1_000_000,
            'centimeter': 100_000,
            'meter': 1000,
            'kilometer': 1,

            'inch': 39_370.0787,
            'feet': 3_280.8399,
            'yard': 1_093.6133,
            'mile': 0.621371192
                 }

        return Converter.formula(value, units[unit_type])

    # IMPERIAL
    @staticmethod
    def from_inches(value, unit_type):

        units = {
            'millimeter': 25.4,
            'centimeter': 2.54,
            'meter': 0.0254,
            'kilometer': 0.0000254,

            'inch': 1,
            'feet': 0.0833333333,
            'yard': 0.0277777778,
            'mile': 0.0000157828283

        }

        return Converter.formula(value, units[unit_type])

    @staticmethod
    def from_feet(value, unit_type):

        units = {
            'millimeter': 304.8,
            'centimeter': 30.48,
            'meter': 0.3048,
            'kilometer': 0.0003048,

            'inch': 12,
            'feet': 1,
            'yard': 0.333333333,
            'mile': 0.000189393939

        }

        return Converter.formula(value, units[unit_type])

    @staticmethod
    def from_yard(value, unit_type):

        units = {
            'millimeter': 914.4,
            'centimeter': 91.44,
            'meter': 0.9144,
            'kilometer': 0.0009144,

            'inch': 36,
            'feet': 3,
            'yard': 1,
            'mile': 0.000568181818

        }

        return Converter.formula(value, units[unit_type])

    def from_miles(self, value, unit_type):

        units = {
            'millimeter': 1_609_344,
            'centimeter': 160_934.4,
            'meter': 1_609.344,
            'kilometer': 1.609344,

            'inch': 63_360,
            'feet': 5280,
            'yard': 1760,
            'mile': 1

        }

        return Converter.formula(value, units[unit_type])

