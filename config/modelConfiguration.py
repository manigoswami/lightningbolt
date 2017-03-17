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
    'MODEL1': 'MODEL1/model.m'  # ,
    # 'MODEL2': 'Fcvoi/NonMetro/model.m'
}

features = {

    'MODEL1':
        {
            'feature_properties': OrderedDict([
                ('f1', ['machinable', 'convertToFloat']),
                ('f2', ['machinable', 'convertToFloat']),
                ('f3', ['donothing']),
                ('f4', ['machinable', 'convertToFloat']),
                ('f5', ['donothing']),
                ('f6', ['donothing']),
                ('f7', ['machinable', 'convertToFloat']),
                ('f8', ['donothing']),
                ('f9', ['donothing']),
                ('f10', ['donothing']),
                ('f11', ['donothing']),
                ('f12', ['machinable', 'convertToFloat'])
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
            'plugin':
                {
                   'class': "src.engine.plugins.find_best_class.FindBestClass",
                   'import_path': "src.engine.plugins import plugin_controller"
                }
        },
    'M2':
        {
            'feature_properties': OrderedDict([
                ('f1', ['machinable', 'convertToFloat']),
                ('f2', ['machinable', 'convertToFloat']),
                ('f3', ['machinable', 'convertToFloat']),
                ('f4', ['machinable', 'convertToFloat']),
                ('f5', ['donothing']),
                ('f6', ['donothing']),
                ('f7', ['machinable', 'convertToFloat']),
                ('f8', ['donothing']),
                ('f9', ['donothing']),
                ('f10', ['machinable', 'convertToFloat']),
                ('f11', ['donothing']),
                ('f12', ['donothing'])
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
