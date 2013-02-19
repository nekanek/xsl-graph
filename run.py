# -*- coding: utf-8 -*-

import pyxsl.analyze
from pyxsl.parse import get_data_and_index
from pyxsl.draw import draw_outside, draw_inside
from pyxsl.pick import pickle_data_and_index, get_data_index_from_pickle


start_dir = '/home/apertsev/workspace/hh.sites.main/xhh/xsl'

files_to_search = [
                    '/home/apertsev/workspace/hh.sites.main/xhh/xsl/ambient/blocks/applicant/login.xsl',
                  ]

if __name__ == "__main__":
    '''
       Usage examples:
         data, index = get_data_and_index(start_dir=start_dir)
         pickle_data_and_index(data, index)
         data, index = get_data_index_from_pickle()

         draw_outside(index, files_to_search, start_dir=start_dir)
         draw_inside(data, start_dir=start_dir)
    '''

    #data, index = get_data_and_index(start_dir=start_dir)
    #pickle_data_and_index(data, index)
    data, index = get_data_index_from_pickle()
    modes = pyxsl.analyze.analyze_modes_usage(data)
