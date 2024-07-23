import importlib
import unicourt
import json

def generate_json_file_from_unicourt_obj(unicourt_obj, filename):
    with open(filename, 'w') as wfp:
        unicourt_obj_and_meta = {
            'unicourt_obj': unicourt_obj.to_dict(),
            'composed_classes': [
                str(_class).replace("<class '", "").replace("'>", "") 
                        for _class in unicourt_obj._visited_composed_classes
            ]
        }
        json.dump(unicourt_obj_and_meta, wfp)

def load_unicourt_obj_from_json_file(filename):
    with open(filename, 'r') as rfp:
        unicourt_obj_and_meta = json.load(rfp)
        unicourt_obj_dict = unicourt_obj_and_meta['unicourt_obj']
        composed_classes = []
        for composed_class_meta in unicourt_obj_and_meta['composed_classes']:
            (class_file, _class) = composed_class_meta.rsplit('.', 1)
            class_file_import = importlib.import_module(class_file)
            composed_classes.append(getattr(class_file_import, _class ))
        
        return unicourt.model_utils.validate_and_convert_types(
            unicourt_obj_dict,
            composed_classes,
            ['received_data'],
            True,
            False,
            unicourt.api_client.configuration)