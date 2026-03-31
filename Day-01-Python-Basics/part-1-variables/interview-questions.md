# 🎯 Interview Questions — Variables

---

## Q1. Pass by value or reference?

Python uses **pass-by-object-reference**

---

## Q2. Difference between `is` and `==`

* `==` → value
* `is` → memory

---

## Q3. Why integer cache (-5 to 256)?

Performance optimization

---

## Q4. Does Python have constants?

❌ No (only convention)

---

## Q5. What does `del` do?

Removes variable binding

---

## 🔥 Output Question

```python
a = [1,2,3]
b = a
c = a[:]

a.append(4)

print(b)
print(c)
```

👉 Output:

```
[1,2,3,4]
[1,2,3]
```
