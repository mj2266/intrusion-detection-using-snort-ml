# intrusion-detection-using-snort-ml
- Snort IDS is an open-source network security tool. It can search and match rules
with network traffic data in order to detect attacks and generate an alert. One
of the greatest challenges of today’s rule-based network intrusion detection system
(NIDS) is the largest value of its false-positive rate which makes the rule-based NIDS
system unreliable. Our main goal is to deliver an intrusion detection system with
lower false-positive rate
- Implemented different ML classification algorithms for intrusion detection
using SNORT
- Demonstrated and evaluation of the live working of our modified NIDS by
performing attacks from Kali Linux Machine to Ubuntu Machine
- Integrated ML model with SNORT for Intrusion Detection 

The project is coded in Python 3.9.7 and requires the installation of the following packages :
    -> pandas
    -> sklearn
    -> datetime

---------
CONTENTS
---------
The folder CODE contains 1 folder and a few files:
    1. NSL-KDD: The dataset used for training
    2. Jupyter Notebooks
        2.1. cross_validation.ipynb: contains cross validation results
        2.2. Prediction_snort_logs.ipynb: Notebook for detecting attacks
        2.3. tcptrace_processlogs.ipynb: Preprocess the packet trace logs
        2.4. generateNewCol.ipynb
    3. Python File 
        3.1. models.py
    4. CSV files (Processed TCP trace Logs)
        4.1. tcplogWithCount_attack.csv
        4.2. tcplogWithCount_non_attack.csv
    5. Text files(TCP Trace)
        5.1. ddos.txt
        5.2. normal.txt
-------------
INSTRUCTIONS
-------------
All the code files are Jupyter notebooks. To execute the files install Jupyter Notebooks.
Refer: https://jupyter.org/install

Results are visible in the notebook itself.

-------------
DEPENDENCIES
-------------
cross_validation.ipynb uses models.py
