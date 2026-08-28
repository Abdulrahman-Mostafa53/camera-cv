# Underwater Image Color Corrector 🎨

[![Python](https://img.shields.io/badge/Python-3.11.15-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5.0.0.93-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.4.6-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)

An automated Python tool designed to restore true colors, contrast, and fine details in underwater photography by mitigating light attenuation artifacts.

---

## 🌊 Overview

Water selectively absorbs light wavelengths as depth increases, causing red light to disappear first and leaving images dominated by blue/green casts.

This tool applies a 3-step color correction pipeline:

1. **Red Channel Compensation 🔴** — Recovers missing red intensity using weighted gains (`0.6` for green mean diff, `0.3` for blue mean diff).
2. **Gray World White Balance ⚖️** — Scales BGR channels to equalize global average intensity and remove blue/green casts.
3. **LAB Luminance CLAHE 🌗** — Enhances image sharpness strictly on the **Luminance (L)** channel without shifting colors.

---

## ⚡ Quick Start
run on the demo image in the root floder
```bash
python main.py
