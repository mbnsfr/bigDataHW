# bigDataHW

to start mongo on local before running files 

`sudo systemctl restart mongod.service`

then install packages using requirements 

```
pip install -r requirements.txt
```

if needed add data from [link](https://www.kaggle.com/datasets/nsrose7224/crowdedness-at-the-campus-gym) to your mongo by 

`python insertCSV.py `

now uncomment the parts that you want to get result and run

`python mongoExample.py `
