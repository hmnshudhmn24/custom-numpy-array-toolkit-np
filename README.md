# 🧩 Custom NumPy Array Extension Toolkit

This project demonstrates how to build custom NumPy array types for specific use cases like masking and unit tracking by subclassing `np.ndarray`.

## 🚀 Features

- `MaskedArray`: Supports element-wise masking and custom mean calculations
- `UnitArray`: Tracks physical units (e.g., meters, seconds) and supports unit conversion
- Plug-and-play: Use like regular NumPy arrays with additional methods

## 🧠 Why This Project?

Subclassing `np.ndarray` is an advanced NumPy technique. This project helps demonstrate internal NumPy mechanics and customization for real-world scenarios.

## 💡 Innovative Twist

The toolkit is designed for chaining and extension — build more array types as modules and compose transformations (e.g., MaskedUnitArray 🚀).

## 📦 How to Run

```bash
python src/main.py
```

## 📂 Project Structure

```
custom_numpy_array_toolkit_np/
├── src/
│   └── main.py         # Custom NumPy subclasses
├── README.md           # Documentation
```

## 📚 Learn More

- [NumPy Subclassing Guide](https://numpy.org/doc/stable/user/basics.subclassing.html)
- [Advanced NumPy Patterns](https://jakevdp.github.io/PythonDataScienceHandbook/)

---

✨ Extend NumPy with purpose — make your data arrays smarter and context-aware!