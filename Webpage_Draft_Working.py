
# coding: utf-8

# In[1]:

import numpy as np
import collections
import numpy.lib.recfunctions as rfn


# In[20]:

with open('webpage_draft2.html','w') as f:
  
    file_dict = collections.OrderedDict()
    file_dict['Neary Dwarf Irregulars'] = ('ndi_new.csv','ndi_p.csv','ndi_s.csv')
    file_dict['Nearby Giant Spirals'] = ('ngs_new.csv','ngs_p.csv','ngs_s.csv')
    file_dict['Background Giant Spirals'] = ('bgs_new.csv','bgs_p.csv','bgs_s.csv')
    file_dict['Nearby Giant Ellipticals and Lenticulars'] = ('ngel_new.csv','ngel_p.csv','ngel_s.csv')
    file_dict['Nearby Dwarf Ellipticals'] = ('nde_new.csv','nde_p.csv','nde_s.csv')
    file_dict['Background Giant Ellipticals and Lenticulars'] = ('bgel_new.csv','bgel_p.csv','bgel_s.csv')
    file_dict['Unknowns'] = ('unknowns_new.csv','unknowns_p.csv','unknowns_s.csv')
    dtype_dict = collections.OrderedDict([(0, [('objid', '<i8'), ('type', 'S6'), ('name', 'S12'), ('ra', '<f8'), ('dec', '<f8'), ('u', '<f8'), ('g', '<f8'), ('r', '<f8'), ('i', '<f8'), ('z', '<f8'), ('redshift', '<f8')]),(1,[('name','S12'),('objID','<i8'),('type','S8'),('petroMag_r','<f8'),('petroR50_r','<f8'),('petroR90_r','<f8')]),(2,[('name','S12'),('zErr','<i10'),('zWarning','<i8'),('class','S10')])])
    cat_list = file_dict.keys()
    for word in cat_list:
        for i in range(3):
            if i == 0:
                new_data = np.recfromcsv(file_dict[word][i],delimiter=',',dtype=dtype_dict[i])
            if i == 1:
                p_data = np.recfromcsv(file_dict[word][i],delimiter=',',dtype=dtype_dict[i])
            if i == 2:
                s_data = np.recfromcsv(file_dict[word][i],delimiter=',',dtype=dtype_dict[i])
        p_fields = p_data.dtype.names
        s_fields = s_data.dtype.names
        old_fields = new_data.dtype.names
        for i in range(6):
            if p_fields[i] in old_fields:
                pass
            else:
                new_data = rfn.append_fields(new_data,p_fields[i],p_data[p_fields[i]],dtypes=None,usemask=False)
        for i in range(4):
            if s_fields[i] in old_fields:
                pass
            else:
                new_data = rfn.append_fields(new_data,s_fields[i],s_data[s_fields[i]],dtypes=None,usemask=False)
        f.write('<table border="1">')
        f.write('<p><strong>{} </strong></p>'.format(word))
        f.write('<tbody>')
        f.write('<tr>')
        for i in range(len(new_data['ra'])):
            if i%5 ==0:
                f.write('</tr><tr>')
            petro = new_data['petror90_r'][i] / 19
            f.write('<td><a href="http://skyserver.sdss.org/dr12/en/tools/chart/navi.aspx?ra={}&amp;dec={}&amp;scale={}"><img src="http://skyservice.pha.jhu.edu/DR12/ImgCutout/getjpeg.aspx?ra={}&amp;dec={}&amp;scale={}&amp;width=120&amp;height=120&amp;opt="" alt="" width="120" height="120""></a><br>\n'.format(new_data['ra'][i],new_data['dec'][i],petro,new_data['ra'][i],new_data['dec'][i],petro))            
            ind_name = new_data['name'][i].decode('UTF-8')
            f.write('{}<br>\n'.format(ind_name))
            f.write('<em>u</em>-<em>r</em> = {:.4}<br>\n'.format(new_data['u'][i]-new_data['r'][i]))
            shift=new_data['redshift'][i]
            if shift <100: 
                f.write('<em>z</em>  = {:.4f}<br>\n'.format(shift))
            elif type(shift) != int:
                f.write('<em>z</em> = N/A<br>\n')
            f.write('Notes: <br>\n</td>')
        f.write('</tr>')
        f.write('</tbody>')


# In[4]:

data = np.recfromcsv('unknowns_new.csv',delimiter=',',dtype = [('objid', '<i8'), ('type', 'S6'), ('name', 'S12'), ('ra', '<f8'), ('dec', '<f8'), ('u', '<f8'), ('g', '<f8'), ('r', '<f8'), ('i', '<f8'), ('z', '<f8'), ('redshift', '<f8')])
x=data['name'][0]
x.decode('UTF-8')



# In[ ]:




# In[ ]:




# In[ ]:



