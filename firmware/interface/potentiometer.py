import board
import analogio

class Potentiometer:
    def __init__(self, pin_name=board.IO9, samples=8):
        self.adc = analogio.AnalogIn(pin_name)
        self.samples = samples
        
        # Real hardware limits observed on ESP32 CircuitPython:
        # Near 0V raw reading sits around 800, saturation happens around 62814.
        self.raw_min = 800
        self.raw_max = 62814
        
        # Multi-point calibration map to straighten the curve:
        # Format: (Raw ADC Value, Corrected Target Ratio 0.0 - 1.0)
        self.lut = [
            (self.raw_min, 0.00),
            (8000,         0.10),
            (18000,        0.25),
            (32000,        0.50), # Forces real physical halfway to output 512
            (48000,        0.75),
            (58000,        0.90),
            (self.raw_max, 1.00)
        ]

    def _get_raw_average(self):
        """Takes a fast hardware multi-sample average to eliminate ADC jitter."""
        total = 0
        for _ in range(self.samples):
            total += self.adc.value
        return total // self.samples

    def read(self):
        """Returns a calibrated integer strictly between 0 and 1024."""
        raw = self._get_raw_average()

        # Clamp lower and upper dead zones
        if raw <= self.raw_min:
            return 0
        if raw >= self.raw_max:
            return 1024

        # Piecewise Linear Interpolation through the Lookup Table
        for i in range(len(self.lut) - 1):
            x0, y0 = self.lut[i]
            x1, y1 = self.lut[i + 1]

            if x0 <= raw <= x1:
                # Interpolate where the raw reading falls between table points
                ratio = y0 + (raw - x0) * (y1 - y0) / (x1 - x0)
                return int(ratio * 1024)

        return 1024

# Module-level convenience functions to match your original interface structure
_pot_instance = None

def init(pin_name=board.IO9):
    global _pot_instance
    _pot_instance = Potentiometer(pin_name)
    print("Potentiometer Module Initialized")

def read():
    global _pot_instance
    return _pot_instance.read()
init()