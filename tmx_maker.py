import pandas as pd
import datetime


def tsv_t_tmx(myfile='data.csv', source_lang='en', target_lang='fa', seprator='\t'):
  now = datetime.datetime.now()
  d2 = now.strftime("%Y-%m-%d %H:%M:%S")
  df = pd.read_csv(myfile, sep=seprator)
  f = open("demofile2.xml", "w", encoding="UTF-8")

  f.write('''<?xml version="1.0" encoding="UTF-8" ?>
             <tmx version="1.4">''')
  f.write(f'''<header creationdate="{d2}"
             srclang= "{source_lang}"
             adminlang="en"
             o-tmf="unknown"
             segtype="sentence"
             creationtool="Uplug"
             creationtoolversion="unknown"
             datatype="PlainText" />
      <body>\n''')

  for index, row in df.iterrows():
    eng = row['English']
    per = row['Persian']
  	
    f.write(f'''
        <tu>
         <tuv xml:lang="{source_lang}">
            <seg>{eng}</seg>
         </tuv>
        <tuv xml:lang="{target_lang}">
           <seg>{per}</seg>
         </tuv>
        </tu>''')

  f.write('''
  	</body>
  	      </tmx>''')

  f.close()  
  base_file = "demofile2.xml"
  name, ext = base_file.split('.')
  new_file = '{}.{}'.format(name, 'tmx')

  with open(base_file , 'r') as f1:
      with open(new_file, 'w') as f2:
          f2.write(f1.read())  

if __name__ == "__main__":
  tsv_t_tmx()          	