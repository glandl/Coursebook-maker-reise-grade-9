+++
title = "P1 Week 2 · Programming Skills"
weight = 1
+++

Five questions on the Python basics from [P1 Week 2 · Team, Requirements, Kanban]({{% relref "projekte/p1-code-gadget/woche-02-anforderungen" %}}): input/type conversion, branching, comparison/boolean operators and loops. The first three questions are identical to the quiz on the student page; the last two are additional questions for classroom use, e.g. as a starter for week 3 or a short test.

{{< quiz title="Quiz · P1 Week 2 · Programming Skills" >}}
{{< question correct="3" >}}
What happens with this code if you enter `15`?

```python
age = input("Age? ")
print(age + 1)
```
---
It prints `16`.
It prints `151`.
There is an error.
It prints `15`.
---
`input` returns text (`"15"`). Python cannot add text and a number (`TypeError`). Correct would be `age = int(input("Age? "))`.
{{< /question >}}
{{< question correct="2" >}}
Which numbers does `for i in range(3): print(i)` print?
---
1, 2, 3
0, 1, 2
0, 1, 2, 3
3, 2, 1
---
`range(3)` starts at 0 and ends **before** 3.
{{< /question >}}
{{< question correct="2" >}}
`temperature = 22`. What does the program print?

```python
if temperature > 25:
    print("hot")
elif temperature > 18:
    print("pleasant")
else:
    print("cold")
```
---
hot
pleasant
cold
pleasant and cold
---
22 > 25 is false, 22 > 18 is true. After the first matching branch, the block is finished.
{{< /question >}}
{{< question correct="2" >}}
`age = 16`, `has_ticket = False`. What does the program print?

```python
if age >= 18 or has_ticket:
    print("Entry granted")
else:
    print("Entry denied")
```
---
Entry granted
Entry denied
An error
Entry granted and Entry denied
---
`age >= 18` is false, `has_ticket` is false. With `or`, **at least one** side must be true for the condition to hold.
{{< /question >}}
{{< question correct="2" >}}
You enter `15` and then `3`. How many times in total does the program ask for a number?

```python
number = int(input("Number between 1 and 10: "))
while number < 1 or number > 10:
    number = int(input("Again: "))
print("OK:", number)
```
---
Once
Twice
Three times
Forever
---
The first entry (`15`) is outside 1–10, so the loop condition is true and it asks a second time. `3` is inside the range, the condition becomes false and the loop ends.
{{< /question >}}
{{< /quiz >}}
