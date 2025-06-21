# 🔔 Smart Cane for Visually Impaired Individuals

A Raspberry Pi-powered assistive device designed to **enhance mobility and safety** for visually impaired individuals. The smart cane detects nearby obstacles and alerts the user through a buzzer. It also includes a tilt detection mechanism to notify in case of a potential fall.

---

## 🚀 Overview

This project was built during a hackathon with the aim of developing a **lightweight, cost-effective, and reliable smart mobility aid**. The device mounts on a traditional walking cane and leverages sensors to:

- **Detect obstacles** using:
  - An **IR sensor** for short-range detection
  - An **ultrasonic sensor** for mid-range distance sensing
- **Detect falls or sudden tilts** using a **tilt switch**
- **Alert the user** using a **buzzer** if any sensor is triggered

---

## 🧠 How It Works

The Raspberry Pi continuously monitors:
- The IR sensor (obstacles at very close range)
- The ultrasonic sensor (objects < 15 cm)
- The tilt switch (indicative of a fall or cane being dropped)

When **any of these conditions** are detected:
- A **buzzer activates** to alert the user.

---

## 🛠 Hardware Used

- Raspberry Pi (tested on Raspberry Pi 4)
- HC-SR04 Ultrasonic Distance Sensor
- IR Obstacle Detection Sensor
- Tilt Switch Sensor
- Active Buzzer Module
- Jumper Wires & Breadboard
- Portable power source (e.g. USB power bank)
- Traditional walking cane for mounting

---

## 🧾 GPIO Pin Configuration

| Component        | GPIO Pin (BCM) | Physical Pin |
| ---------------- | -------------- | ------------ |
| IR Sensor        | 17             | 11           |
| Buzzer           | 23             | 16           |
| Ultrasonic TRIG  | 22             | 15           |
| Ultrasonic ECHO  | 27             | 13           |
| Tilt Switch      | 24             | 18           |
| Touch Switch     | 25             | 22           |

---

## 💻 Software & Code

The script is written in **Python 3** and uses the `RPi.GPIO` library to control GPIO pins.

### ➤ Run the script:

```bash
chmod +x smart_cane.py
python3 smart_cane.py
