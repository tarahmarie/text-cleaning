#
#             *
#            * *
#           *   *
#          *     *
#           *   *
#            * *
#             *
#
# March Twenty-Fifth, Two Thousand Twenty-One
# Red Queen
# tarah@redqueentech.com
#
# The digital humanities only looks like it's computational. Actually, it's data cleaning. Forever.
#
# Use me for cleaning Gutentag XML exports to get down to the nested paragraphs
# that project found here: https://gutentag.sdsu.edu/

from xml.etree.ElementTree import ElementTree
import pandas as pd


def xml_to_dataframe():
    f_path = 'Frankenstein.xml'
    root = ElementTree.parse(f_path).getroot()
    elements = root.getchildren()[0][-1]
    f_dict = {'paragraph': []}
    for b in elements:
        if b.attrib.get('type', None) == 'chapter':
            for t in b.getchildren():
                try:
                    if len(t.text.strip()) > 30:
                        f_dict['paragraph'].append(t.text)
                except:
                    continue
        else:
            if len(b.text.strip()) > 30:
                f_dict['paragraph'].append(b.text)
    df = pd.DataFrame.from_dict(f_dict)
    print(df)
    return df


xml_to_dataframe()
