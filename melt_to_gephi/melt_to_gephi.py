# -*- coding: utf-8 -*-
import os
import pandas as pd
from glob import glob
import sys

def clean_df(frame):
  """Restructure the dataframe to a friedlier state
  Args:
      frame : a dataframe with camel cased columns, duplicates
  Returns:
      frame: a friendlier and cleaner dataframe
  """
  #edit colnames
  frame.columns = frame.columns.str.lower().str.replace(" ", "_")
  #drop nulls
  frame.dropna(how = 'all', axis =1 , inplace = True)
  return frame

def read_file(trend_file):
        """Read meltwater files and open with proper encoding
        and assign trend
        Args:
            file (csv): The Downloaded data file from meltwater
        Returns:
            dataframe : A dataframe with an additional column corresponding to the twitter
                        trend / keyword collected by.
        """
        df_raw = pd.read_csv(trend_file,parse_dates = ['Date'],
                               encoding='utf-16',
                               error_bad_lines=False,sep='\t')
        hashtag = str(trend_file).split('/')[-1].split('.')[0]
        df = clean_df(df_raw).assign(trend=hashtag)
        return df

def collate_amplifyers():
  """Grab the RT and QT columns then concat assign post type and hashtag
  Returns:
      amplifyers: A dataframe with a filtered columns bearing the fields with the
                  network
  """
  frame = read_file(file)
  df_rt = frame[frame['hit_sentence'].str.startswith("RT")].assign(post_type='RT')
  df_qt = frame[frame['hit_sentence'].str.startswith("QT")].assign(post_type='QT')
  df_net = pd.concat([df_rt,df_qt])
  amplifyers = df_net[['hit_sentence','influencer','post_type','url','date','trend']]

  return amplifyers

def get_source_target():
  """  Grab the source and target columns for the networks for the source file
  Returns:
      frame : A dataframe with assigned columns and the corresponding tweet
  """
  frame = collate_amplifyers()
  # source = frame['hit_sentence'].split(':')[0].split(' ')[1]
  source = frame['hit_sentence'].apply(lambda x: x.split(':')[0].split(' ')[1])
  frame.rename(columns={"influencer": "target",'hit_sentence' :'tweet'},inplace=True)
  frame['source'] = source

  return frame

def prep_gephi_file():

    """[summary]
    """
    list_of_df = []
    gephi_ready_file = os.path.join(clean_folder,fileName)
    for item in raw_files:
        with open(str(item), 'r') as f:
            file  = open(f,'r')
        frame = get_source_target()
        list_of_df.append(frame)
        gephi_file = pd.concat(list_of_df, ignore_index=True)
        gephi_file.to_csv(gephi_ready_file)

if __name__ == "__main__":
    fileName = 'tigray_crisis.csv'
    raw_files = glob('data/*.csv')
    clean_folder =  'data/gephi_ready' #'cleaned_nodes_edges/'
    # main()
    prep_gephi_file(raw_files)
