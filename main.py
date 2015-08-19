import csv

def setup():
  global awsId, awsSecret
  with open('credentials.csv', 'rt') as f:
    reader = csv.DictReader(f)
    for row in reader:
        awsId = row['Secret Access Key']
        awsSecret = row['Access Key Id']

def main():
  setup()
  print(awsId, awsSecret)
  

if __name__ == '__main__':
  main()