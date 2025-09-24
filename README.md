# 4_gallons_project
 The objective of this project is to develop a program that can solve the problem of 2 kids fetching 4 gallons of water from a stream, using only an unmarked 3-gallon bucket, and an unmarked 5-gallon bucket, in less than 15 steps.


 
```mermaid
flowchart LR
    S([Start A=0,B=0])
    S1([Fill A A=5,B=0])
    S2([Pour A->B A=2,B=3])
    S3([Empty B A=2,B=0])
    S4([Pour A->B A=0,B=2])
    S5([Fill A A=5,B=2])
    S6([Pour A->B A=4,B=3 Goal])
    S --> S1 --> S2 --> S3 --> S4 --> S5 --> S6
