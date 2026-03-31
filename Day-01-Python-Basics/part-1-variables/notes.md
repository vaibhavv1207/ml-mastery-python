# ============================================================
# 📅 DAY 01 — PYTHON BASICS
# 📌 PART 1 — VARIABLES
# 🎯 ML Mastery — Zero to FAANG-Level ML Engineer
# ============================================================

---

# 📖 CONCEPT EXPLANATION

---

## 🔹 What is a Variable?

A variable in Python is a **name (reference/label)** bound to an object in memory.

> ⚠️ IMPORTANT: A variable is NOT a box that holds a value.
> It is a **sticky note / tag** attached to an object in memory.

### How it works internally:

```python
x = 10

Step-by-step what happens in memory:
Step 1 → Python creates an integer object 10 in memory
Step 2 → That object gets a memory address (e.g., 140732856543408)
Step 3 → The name 'x' is just a LABEL pointing to that address

Visual:

    Variable Name          Memory (RAM)
    ┌─────┐               ┌──────────────┐
    │  x  │ ───────────►  │  int obj: 10 │
    └─────┘               │  id: 14073.. │
                           └──────────────┘

                    

🔹 Real-World Analogy
Think of it like this:

🏠 HOUSE     = The actual object (10) sitting in memory
🏷️ NAME PLATE = The variable name (x) — just a tag on the house

You can put MULTIPLE name plates on the SAME house:

    x = 10
    y = x    → both x and y are plates on the SAME house

You can MOVE a name plate to a different house:

    x = 20   → x plate moves to house "20"
               y plate still on house "10"


🔹 Proof — Variables are References

a = [1, 2, 3]
b = a                # b points to the SAME list object

print(id(a))         # e.g., 140234567890
print(id(b))         # e.g., 140234567890  ← SAME!
print(a is b)        # True — same object

b.append(4)
print(a)             # [1, 2, 3, 4] — a is also changed!

Why? Because b = a does NOT copy. It makes b point to the same object.

    ┌─────┐
    │  a  │ ──────┐
    └─────┘       │     ┌──────────────────┐
                  ├──►  │ list: [1, 2, 3]  │
    ┌─────┐       │     └──────────────────┘
    │  b  │ ──────┘
    └─────┘

🔹 Reassignment — What Really Happens

x = 10     # x points to object 10
x = 20     # x NOW points to object 20 (new object created)
           # object 10 still exists if something else points to it
           # if nothing points to it → garbage collector removes it

BEFORE:
    x ──────► int(10)

AFTER x = 20:
    x ──────► int(20)     ← x moved to new object
              int(10)     ← orphaned → garbage collected


🔹 Dynamic Typing
Python is dynamically typed — variables DON'T have types, OBJECTS do.

x = 10          # x points to int object
x = "hello"     # x now points to str object — NO ERROR
x = [1, 2, 3]   # x now points to list object — NO ERROR
x = True        # x now points to bool object — NO ERROR

Compare with C/Java (statically typed):

int x = 10;
x = "hello";    // ERROR! x is locked to int type

e
🔑 KEY INSIGHT: In Python, the OBJECT has a type. The VARIABLE is just a name tag.


🔹 Variable Naming Rules
#	Rule	✅ Valid	❌ Invalid
1	Must start with letter or _	name, _count	1name, @val
2	Can contain letters, digits, _	val_2, my_var	my-var, my var
3	Case sensitive	Name ≠ name ≠ NAME	—
4	Cannot be a Python keyword	my_class	class, for, if
5	No spaces allowed	first_name	first name
6	No special characters	count_1	count@1, val#2