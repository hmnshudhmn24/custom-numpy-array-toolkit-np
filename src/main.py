import numpy as np

class MaskedArray(np.ndarray):
    def __new__(cls, input_array, mask=None):
        obj = np.asarray(input_array).view(cls)
        if mask is None:
            mask = np.zeros_like(input_array, dtype=bool)
        obj.mask = mask
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return
        self.mask = getattr(obj, 'mask', None)

    def masked_mean(self):
        valid = ~self.mask
        return self[valid].mean() if np.any(valid) else np.nan

    def __str__(self):
        return f"MaskedArray(data={np.array(self)}, mask={self.mask})"


class UnitArray(np.ndarray):
    def __new__(cls, input_array, unit="unitless"):
        obj = np.asarray(input_array).view(cls)
        obj.unit = unit
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return
        self.unit = getattr(obj, 'unit', "unitless")

    def convert_to(self, factor, new_unit):
        return UnitArray(self * factor, new_unit)

    def __str__(self):
        return f"{np.array(self)} [{self.unit}]"

# Example usage
if __name__ == "__main__":
    print("🔶 MaskedArray Example:")
    data = MaskedArray([1, 2, 3, 4, 5], mask=[0, 1, 0, 0, 1])
    print(data)
    print("Masked mean:", data.masked_mean())

    print("\n🔷 UnitArray Example:")
    distance = UnitArray([1, 2, 3], unit="meters")
    print(distance)
    km = distance.convert_to(0.001, "km")
    print("Converted to km:", km)