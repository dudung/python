cat $1 | sed '0, /```/d; /```/Q' | python
