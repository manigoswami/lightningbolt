__author__ = 'manishankargoswami'
"""
This file holds all model related configurations,
please note, the order of definition is important
here

v0.0.1
"""

from collections import OrderedDict

models = OrderedDict()

models = {
    'FCVOIMETRO': 'Fcvoi/Metro/model.m',
    # 'FCVOINONMETRO': 'Fcvoi/NonMetro/model.m',
    # 'FCVOIREMAINING': 'Fcvoi/Remaining/model.m',
    # 'DROPSHIPMETRO': 'Dropship/Metro/model.m',
    # 'DROPSHIPSEMIMETRO':'Dropship/SemiMetro/model.m',
    # 'DROPSHIPNONMETRO':'Dropship/NonMetro/model.m',
    # 'DROPSHIPREMAINING':'Dropship/Remaining/model.m',
    # 'OCMETRO': 'Oneship/Metro/model.m',
    # 'OCNONMETRO1':'Oneship/NonMetro1/model.m',
    # 'OCNONMETRO2':'Oneship/NonMetro2/model.m',
    #  'OCNONMETRO3':'Oneship/NonMetro3/model.m',
    #  'OCREMAINING':'Oneship/Remaining/model.m'
}

features = {

    'FCVOIMETRO':
        {
            'feature_properties': OrderedDict([
                ('fp_code', ['machinable', 'convertToFloat']),
                ('dest_city', ['machinable', 'convertToFloat']),
                ('dest_tier', ['donothing']),
                ('shippingMode', ['machinable', 'convertToFloat']),
                ('timeOfTheDay', ['donothing']),
                ('dayOfTheWeek', ['donothing']),
                ('product_category', ['machinable', 'convertToFloat']),
                ('weight_category', ['donothing']),
                ('makeToOder', ['donothing']),
                ('isHeavy', ['donothing']),
                ('bucket_category', ['donothing']),
                ('courier', ['machinable', 'convertToFloat'])
            ]),
            'window_properties':
                {
                    'defaultrange': "{\"min\": 9, \"max\": 15}",
                    'initialcutoff': 1.03,
                    'range1cutoff': 0,
                    'range2cutoff': 0,
                    'minwindowsize': 3,
                    'maxwindowsize': 3,
                    'finaldefaultwindowsize': 3
                },
            'plugin': {
                'class': "FindBestClass",
                'import_path': "src.engine.plugins import plugin_controller"
            }
        },
    'FCVOINONMETRO':
        {
            'feature_properties': OrderedDict([
                ('fp_code', ['machinable', 'convertToFloat']),
                ('dest_city', ['machinable', 'convertToFloat']),
                ('dest_tier', ['machinable', 'convertToFloat']),
                ('shippingMode', ['machinable', 'convertToFloat']),
                ('timeOfTheDay', ['donothing']),
                ('dayOfTheWeek', ['donothing']),
                ('product_category', ['machinable', 'convertToFloat']),
                ('weight_category', ['donothing']),
                ('makeToOder', ['donothing']),
                ('VolWt', ['machinable', 'convertToFloat']),
                ('isHeavy', ['donothing']),
                ('bucket_category', ['donothing'])
            ]),
            'window_properties':
                {
                    'defaultrange': "{\"min\": 9, \"max\": 15}",
                    'initialcutoff': 1.03,
                    'range1cutoff': 0,
                    'range2cutoff': 0,
                    'minwindowsize': 3,
                    'maxwindowsize': 3,
                    'finaldefaultwindowsize': 3
                }
        },
    'FCVOIREMAINING':
        {
            'feature_properties': OrderedDict([
                ('fp_code', ['machinable', 'convertToFloat']),
                ('dest_city', ['machinable', 'convertToFloat']),
                ('dest_tier', ['machinable', 'convertToFloat']),
                ('shippingMode', ['machinable', 'convertToFloat']),
                ('timeOfTheDay', ['donothing']),
                ('dayOfTheWeek', ['donothing']),
                ('product_category', ['machinable', 'convertToFloat']),
                ('weight_category', ['donothing']),
                ('makeToOder', ['donothing']),
                ('VolWt', ['machinable', 'convertToFloat']),
                ('isHeavy', ['donothing']),
                ('bucket_category', ['donothing'])
            ]),
            'window_properties':
                {
                    'defaultrange': "{\"min\": 9, \"max\": 15}",
                    'initialcutoff': 1.03,
                    'range1cutoff': 0,
                    'range2cutoff': 0,
                    'minwindowsize': 3,
                    'maxwindowsize': 3,
                    'finaldefaultwindowsize': 3
                }
        },
    'DROPSHIPMETRO':
        {
            'feature_properties': OrderedDict([
                ('vendor_code', ['machinable', 'convertToFloat']),
                ('origin_city', ['machinable', 'convertToFloat']),
                ('dest_city', ['machinable', 'convertToFloat']),
                ('dest_tier', ['machinable', 'convertToFloat']),
                ('shippingMode', ['machinable', 'convertToFloat']),
                ('timeOfTheDay', ['donothing']),
                ('dayOfTheWeek', ['donothing']),
                ('product_category', ['machinable', 'convertToFloat']),
                ('weight_category', ['donothing']),
                ('makeToOder', ['donothing']),
                ('VolWt', ['machinable', 'convertToFloat']),
                ('isHeavy', ['donothing']),
                ('bucket_category', ['donothing'])
            ]),
            'window_properties':
                {
                    'defaultrange': "{\"min\": 9, \"max\": 15}",
                    'initialcutoff': 1.03,
                    'range1cutoff': 0,
                    'range2cutoff': 0,
                    'minwindowsize': 3,
                    'maxwindowsize': 3,
                    'finaldefaultwindowsize': 3
                }
        },
    'DROPSHIPSEMIMETRO':
        {
            'feature_properties': OrderedDict([
                ('vendor_code', ['machinable', 'convertToFloat']),
                ('origin_city', ['machinable', 'convertToFloat']),
                ('dest_city', ['machinable', 'convertToFloat']),
                ('dest_tier', ['machinable', 'convertToFloat']),
                ('shippingMode', ['machinable', 'convertToFloat']),
                ('timeOfTheDay', ['donothing']),
                ('dayOfTheWeek', ['donothing']),
                ('product_category', ['machinable', 'convertToFloat']),
                ('weight_category', ['donothing']),
                ('makeToOder', ['donothing']),
                ('VolWt', ['machinable', 'convertToFloat']),
                ('isHeavy', ['donothing']),
                ('bucket_category', ['donothing'])
            ]),
            'window_properties':
                {
                    'defaultrange': "{\"min\": 9, \"max\": 15}",
                    'initialcutoff': 1.03,
                    'range1cutoff': 0,
                    'range2cutoff': 0,
                    'minwindowsize': 3,
                    'maxwindowsize': 3,
                    'finaldefaultwindowsize': 3
                }
        },
    'DROPSHIPNONMETRO':
        {
            'feature_properties': OrderedDict([
                ('vendor_code', ['machinable', 'convertToFloat']),
                ('origin_city', ['machinable', 'convertToFloat']),
                ('dest_city', ['machinable', 'convertToFloat']),
                ('dest_tier', ['machinable', 'convertToFloat']),
                ('shippingMode', ['machinable', 'convertToFloat']),
                ('timeOfTheDay', ['donothing']),
                ('dayOfTheWeek', ['donothing']),
                ('product_category', ['machinable', 'convertToFloat']),
                ('weight_category', ['donothing']),
                ('makeToOder', ['donothing']),
                ('VolWt', ['machinable', 'convertToFloat']),
                ('isHeavy', ['donothing']),
                ('bucket_category', ['donothing'])
            ]),
            'window_properties':
                {
                    'defaultrange': "{\"min\": 9, \"max\": 15}",
                    'initialcutoff': 1.03,
                    'range1cutoff': 0,
                    'range2cutoff': 0,
                    'minwindowsize': 3,
                    'maxwindowsize': 3,
                    'finaldefaultwindowsize': 3
                }
        },
    'DROPSHIPREMAINING':
        {
            'feature_properties': OrderedDict([
                ('vendor_code', ['machinable', 'convertToFloat']),
                ('origin_city', ['machinable', 'convertToFloat']),
                ('dest_city', ['machinable', 'convertToFloat']),
                ('dest_tier', ['machinable', 'convertToFloat']),
                ('shippingMode', ['machinable', 'convertToFloat']),
                ('timeOfTheDay', ['donothing']),
                ('dayOfTheWeek', ['donothing']),
                ('product_category', ['machinable', 'convertToFloat']),
                ('weight_category', ['donothing']),
                ('makeToOder', ['donothing']),
                ('VolWt', ['machinable', 'convertToFloat']),
                ('isHeavy', ['donothing']),
                ('bucket_category', ['donothing'])
            ]),
            'window_properties':
                {
                    'defaultrange': "{\"min\": 9, \"max\": 15}",
                    'initialcutoff': 1.03,
                    'range1cutoff': 0,
                    'range2cutoff': 0,
                    'minwindowsize': 3,
                    'maxwindowsize': 3,
                    'finaldefaultwindowsize': 3
                }
        },
    'OCMETRO':
        {
            'feature_properties': OrderedDict([
                ('fp_code', ['machinable', 'convertToFloat']),
                ('dest_city', ['machinable', 'convertToFloat']),
                ('vendor_code', ['machinable', 'convertToFloat']),
                ('dest_tier', ['donothing']),
                ('origin_city', ['machinable', 'convertToFloat']),
                ('shippingMode', ['machinable', 'convertToFloat']),
                ('timeOfTheDay', ['donothing']),
                ('dayOfTheWeek', ['donothing']),
                ('product_category', ['machinable', 'convertToFloat']),
                ('weight_category', ['donothing']),
                ('makeToOder', ['donothing']),
                ('VolWt', ['machinable', 'convertToFloat']),
                ('SameCity', ['donothing']),
                ('InterMetro', ['donothing'])
            ]),
            'window_properties':
                {
                    'defaultrange': "{\"min\": 9, \"max\": 15}",
                    'initialcutoff': 1.03,
                    'range1cutoff': 0,
                    'range2cutoff': 0,
                    'minwindowsize': 3,
                    'maxwindowsize': 3,
                    'finaldefaultwindowsize': 3
                }
        },
    'OCNONMETRO1':
        {
            'feature_properties': OrderedDict([
                ('fp_code', ['machinable', 'convertToFloat']),
                ('dest_city', ['machinable', 'convertToFloat']),
                ('vendor_code', ['machinable', 'convertToFloat']),
                ('dest_tier', ['donothing']),
                ('origin_city', ['machinable', 'convertToFloat']),
                ('shippingMode', ['machinable', 'convertToFloat']),
                ('timeOfTheDay', ['donothing']),
                ('dayOfTheWeek', ['donothing']),
                ('product_category', ['machinable', 'convertToFloat']),
                ('weight_category', ['donothing']),
                ('makeToOder', ['donothing']),
                ('VolWt', ['machinable', 'convertToFloat']),
                ('SameCity', ['donothing']),
                ('BucketFeature', ['donothing'])
            ]),
            'window_properties':
                {
                    'defaultrange': "{\"min\": 9, \"max\": 15}",
                    'initialcutoff': 1.03,
                    'range1cutoff': 0,
                    'range2cutoff': 0,
                    'minwindowsize': 3,
                    'maxwindowsize': 3,
                    'finaldefaultwindowsize': 3
                }
        },
    'OCNONMETRO2':
        {
            'feature_properties': OrderedDict([
                ('fp_code', ['machinable', 'convertToFloat']),
                ('dest_city', ['machinable', 'convertToFloat']),
                ('vendor_code', ['machinable', 'convertToFloat']),
                ('dest_tier', ['donothing']),
                ('origin_city', ['machinable', 'convertToFloat']),
                ('shippingMode', ['machinable', 'convertToFloat']),
                ('timeOfTheDay', ['donothing']),
                ('dayOfTheWeek', ['donothing']),
                ('product_category', ['machinable', 'convertToFloat']),
                ('weight_category', ['donothing']),
                ('makeToOder', ['donothing']),
                ('VolWt', ['machinable', 'convertToFloat']),
                ('SameCity', ['donothing'])

            ]),
            'window_properties':
                {
                    'defaultrange': "{\"min\": 9, \"max\": 15}",
                    'initialcutoff': 1.03,
                    'range1cutoff': 0,
                    'range2cutoff': 0,
                    'minwindowsize': 3,
                    'maxwindowsize': 3,
                    'finaldefaultwindowsize': 3
                }
        },
    'OCNONMETRO3':
        {
            'feature_properties': OrderedDict([
                ('fp_code', ['machinable', 'convertToFloat']),
                ('dest_city', ['machinable', 'convertToFloat']),
                ('vendor_code', ['machinable', 'convertToFloat']),
                ('dest_tier', ['donothing']),
                ('origin_city', ['machinable', 'convertToFloat']),
                ('shippingMode', ['machinable', 'convertToFloat']),
                ('timeOfTheDay', ['donothing']),
                ('dayOfTheWeek', ['donothing']),
                ('product_category', ['machinable', 'convertToFloat']),
                ('weight_category', ['donothing']),
                ('makeToOder', ['donothing']),
                ('VolWt', ['machinable', 'convertToFloat']),
                ('SameCity', ['donothing'])
            ]),
            'window_properties':
                {
                    'defaultrange': "{\"min\": 9, \"max\": 15}",
                    'initialcutoff': 1.03,
                    'range1cutoff': 0,
                    'range2cutoff': 0,
                    'minwindowsize': 3,
                    'maxwindowsize': 3,
                    'finaldefaultwindowsize': 3
                }
        },
    'OCREMAINING':
        {
            'feature_properties': OrderedDict([
                ('fp_code', ['machinable', 'convertToFloat']),
                ('dest_city', ['machinable', 'convertToFloat']),
                ('vendor_code', ['machinable', 'convertToFloat'])
            ]),
            'window_properties':
                {
                    'defaultrange': "{\"min\": 9, \"max\": 15}",
                    'initialcutoff': 1.03,
                    'range1cutoff': 0,
                    'range2cutoff': 0,
                    'minwindowsize': 3,
                    'maxwindowsize': 3,
                    'finaldefaultwindowsize': 3
                }
        }
}
