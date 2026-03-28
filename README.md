# 🛒 E-commerce API Testing Framework

A scalable and production-style API automation testing framework built using **Python**, **Requests**, and **Pytest**.

This project simulates real-world API testing scenarios for an e-commerce system, covering core business flows such as authentication, product retrieval, and cart operations.

It is designed with modular architecture and reusable components to support maintainability and scalability in real QA environments.

---

## 🚀 Features

- REST API testing using Python Requests
- Pytest framework with fixtures
- Token-based authentication handling
- Modular API layer design
- Reusable request utilities
- Data-driven testing support (JSON)
- HTML test reports generation
- CI/CD ready structure

---

## 🧠 Tech Stack

- Python
- Pytest
- Requests
- JSON
- Git & GitHub

---

## 🔑 Test Scenarios

### 🔐 Authentication API
- ✅ Valid login
- ❌ Invalid credentials
- ❌ Missing fields

### 📦 Products API
- ✅ Get all products
- ❌ Invalid endpoint handling

### 🛒 Cart API
- ✅ Authorized access with token
- ❌ Unauthorized access

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/api-testing-framework.git
cd api-testing-framework
pip install -r requirements.txt
