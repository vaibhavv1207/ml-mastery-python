# 📖 Day 01 — Python Basics | Part 1: Variables

---

## 🔹 What is a Variable?

A variable in Python is a **name (reference)** bound to an object in memory.
It is NOT a container — it's a **label/tag**.

---

## 🔹 First Principles (Important)

```python
x = 10
```

What happens internally:

1. Python creates an integer object `10` in memory
2. That object has a memory address
3. `x` is just a label pointing to that object

---

## 🏠 Real-World Analogy

* Object → House 🏠
* Variable → Name plate 🏷️

```python
x = 10
y = x
```

Both `x` and `y` point to the SAME object.

---

## 🔬 Proof using `id()`

```python
x = 10
y = x

print(id(x))
print(id(y))   # same → same object
```

---

## 🧠 Variables are References (NOT Copies)

```python
a = [1, 2, 3]
b = a

b.append(4)
print(a)   # [1,2,3,4]
```

Because both point to SAME object.

---

## 🔹 Dynamic Typing

```python
x = 10
x = "hello"
x = [1,2]
```

✔ Variable has NO type
✔ Object has type

---

## 🔹 Integer Interning (-5 to 256)

```python
a = 256; b = 256
print(a is b)   # True

a = 257; b = 257
print(a is b)   # False
```

---

## 🔹 Multiple Assignment

```python
x, y, z = 1, 2, 3
a = b = c = 0
x, y = y, x
```

---

## 🔹 Naming Rules

| Rule                | Valid     | Invalid   |
| ------------------- | --------- | --------- |
| Start with letter/_ | name      | 1name     |
| No spaces           | user_name | user name |
| Not keyword         | my_var    | class     |

---

## 🔹 `is` vs `==`

```python
a = [1,2]
b = [1,2]

print(a == b)  # True
print(a is b)  # False
```

---

## 🔹 `del` Statement

```python
x = 10
del x
```

Removes variable binding (not object directly)

---

## ⚡ Cheatsheet

```python
type(x)
id(x)
x is y
x == y
del x
```

---

## ⚠️ Common Traps

* `b = a` → NOT copy
* `is ≠ ==`
* Integer cache (-5 to 256)
* No real constants
* Variables are references

---

## ✅ Part 1 Complete
