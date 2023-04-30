cat $1 | sed '0, /```python/d; /```/Q' | python
